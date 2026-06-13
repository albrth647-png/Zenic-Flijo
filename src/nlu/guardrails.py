"""
DDE v3 — Guardrails de IA (Fase 3)

Sistema de guardrails para seguridad y calidad en generación de workflows.

Tres capas de guardrails componibles:
1. ContentGuardrails   — Filtra contenido peligroso, prompt injection, SQLi
2. ExecutionGuardrails — Límites de budget, pasos, complejidad, ciclos
3. PIIGuardrails       — Detecta y protege datos sensibles (emails, phones, IDs)

Cada guardrail retorna un GuardrailResult con:
- passed: bool
- risk: Literal["low", "medium", "high", "critical"]
- action: Literal["allow", "warn", "block"]
- message: str (explicación en ES/EN)
- details: dict (evidencia del bloqueo)

Todas las capas siguen el principio de default-deny para contenido
sensible y default-allow para contenido seguro confirmado.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import StrEnum
from typing import ClassVar


class RiskLevel(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class GuardrailAction(StrEnum):
    ALLOW = "allow"
    WARN = "warn"
    BLOCK = "block"


@dataclass(frozen=True)
class GuardrailResult:
    """Resultado de una evaluación de guardrail."""

    passed: bool
    risk: RiskLevel
    action: GuardrailAction
    message: str
    details: dict = field(default_factory=dict)

    @classmethod
    def allow(cls, message: str = "", details: dict | None = None) -> GuardrailResult:
        return cls(
            passed=True,
            risk=RiskLevel.LOW,
            action=GuardrailAction.ALLOW,
            message=message or "Pasó todas las verificaciones",
            details=details or {},
        )

    @classmethod
    def warn(cls, message: str, risk: RiskLevel = RiskLevel.MEDIUM, details: dict | None = None) -> GuardrailResult:
        return cls(
            passed=True,
            risk=risk,
            action=GuardrailAction.WARN,
            message=message,
            details=details or {},
        )

    @classmethod
    def block(cls, message: str, risk: RiskLevel = RiskLevel.HIGH, details: dict | None = None) -> GuardrailResult:
        return cls(
            passed=False,
            risk=risk,
            action=GuardrailAction.BLOCK,
            message=message,
            details=details or {},
        )


# ──────────────────────────────────────────────
#  CAPA 1: ContentGuardrails
# ──────────────────────────────────────────────


class ContentGuardrails:
    """Filtra contenido peligroso en prompts de usuario y respuestas de IA.

    Detecta:
    - Prompt injection (intentos de override del system prompt)
    - Comandos de sistema peligrosos (rm -rf, drop table, etc.)
    - SQL injection en parámetros
    - Cross-site scripting (XSS)
    - Contenido prohibido (instrucciones ilegales, violencia)
    - Token overflow (prompts excesivamente largos)
    """

    # Patrones de prompt injection (ES/EN)
    PROMPT_INJECTION_PATTERNS: ClassVar[list[re.Pattern]] = [
        re.compile(r"ignora\s+las?\s+instruccion(?:es)?\s+anteriores", re.IGNORECASE),
        re.compile(r"ignore\s+(?:all\s+)?previous\s+instructions?", re.IGNORECASE),
        re.compile(r"olvid(?:a|e)\s+tod(?:o|as?)\s+lo\s+(?:que\s+)?te\s+(?:dije|dijeron|he dicho)", re.IGNORECASE),
        re.compile(r"forget\s+(?:all\s+)?(?:your\s+)?(?:previous\s+)?instructions?", re.IGNORECASE),
        re.compile(r"eres?\s+un?\s+(?:asistente|sistema|ai)\s+(?:libre|sin\s+restriccion(?:es)?)", re.IGNORECASE),
        re.compile(r"you\s+are\s+(?:a\s+)?(?:free|unrestricted|unbounded)\s+(?:assistant|ai|system)", re.IGNORECASE),
        re.compile(r"act\s+(?:as\s+)?(?:if|like)\s+(?:you\s+are|a)\s+(?:free|unrestricted|dan)", re.IGNORECASE),
        re.compile(r"eres\s+(?:un?\s+)?(?:dan|free|unrestricted)", re.IGNORECASE),
        re.compile(r"no\s+(?:hay|tienes?)\s+(?:reglas?|limites?|restriccion(?:es)?)", re.IGNORECASE),
        re.compile(r"(?:there\s+are|you\s+have)\s+no\s+(?:rules?|limits?|restrictions?)", re.IGNORECASE),
        re.compile(r"bypass|jailbreak|jail.?break", re.IGNORECASE),
        re.compile(r"a partir de ahora|from now on\s+you\s+(?:are|will)", re.IGNORECASE),
        re.compile(r"system\s*(?:prompt|instruction|message)s?\s*[:=]", re.IGNORECASE),
    ]

    # Patrones de comandos peligrosos
    DANGEROUS_COMMANDS: ClassVar[list[re.Pattern]] = [
        re.compile(r"\brm\s+(?:-rf|\-r\s+\-f)\s+[/~]", re.IGNORECASE),
        re.compile(r"\b(drop|truncate)\s+(table|database|schema)", re.IGNORECASE),
        re.compile(r"\bshutdown\s+(?:now|-h|-r)", re.IGNORECASE),
        re.compile(r"\bmkfs\.", re.IGNORECASE),
        re.compile(r"\bdd\s+if=", re.IGNORECASE),
        re.compile(r"\b(?:wget|curl)\s+(?:-O\s+)?https?://.*\|\s*(?:bash|sh|python)", re.IGNORECASE),
        re.compile(r"\bchmod\s+777\s+/", re.IGNORECASE),
    ]

    # Patrones XSS
    XSS_PATTERNS: ClassVar[list[re.Pattern]] = [
        re.compile(r"<script\b[^>]*>.*?</script>", re.IGNORECASE | re.DOTALL),
        re.compile(r"javascript\s*:", re.IGNORECASE),
        re.compile(r"on\w+\s*=\s*['\"][^'\"]*['\"]", re.IGNORECASE),
        re.compile(r"<iframe\b", re.IGNORECASE),
        re.compile(r"document\.(?:cookie|write|location)", re.IGNORECASE),
    ]

    # Palabras clave de contenido prohibido
    PROHIBITED_CONTENT: ClassVar[list[re.Pattern]] = [
        re.compile(r"(?:instruccion(?:es)?|c[óo]digo)\s+(?:para\s+)?(?:crear|hacer|fabricar)\s+(?:armas?|explosivos?|drogas?|venenos?)", re.IGNORECASE),
        re.compile(r"(?:how\s+to\s+)?(?:make|create|build|synthesize)\s+(?:weapons?|explosives?|drugs?|poisons?|malware)", re.IGNORECASE),
        re.compile(r"(?:ataque|hack(?:ing|ear)?)\s+(?:inform[áa]tico|de\s+seguridad|bancari)", re.IGNORECASE),
        re.compile(r"(?:hack|crack|phish)\s+(?:bank|account|system|password)", re.IGNORECASE),
    ]

    MAX_PROMPT_LENGTH: ClassVar[int] = 10000
    MAX_PROMPT_TOKENS: ClassVar[int] = 4000  # ~3000 palabras

    def __init__(self, lang: str = "es"):
        self.lang = lang

    def check_prompt(self, text: str) -> GuardrailResult:
        """Evalúa el prompt del usuario contra todas las reglas de contenido.

        Args:
            text: Texto del prompt del usuario

        Returns:
            GuardrailResult con la decisión
        """
        if not text or not text.strip():
            return GuardrailResult.block(
                self._msg("El prompt está vacío", "Empty prompt"),
                RiskLevel.MEDIUM,
                {"reason": "empty_prompt"},
            )

        # 1. Verificar longitud
        if len(text) > self.MAX_PROMPT_LENGTH:
            return GuardrailResult.block(
                self._msg(
                    f"Prompt demasiado largo ({len(text)} caracteres, máximo {self.MAX_PROMPT_LENGTH})",
                    f"Prompt too long ({len(text)} chars, max {self.MAX_PROMPT_LENGTH})",
                ),
                RiskLevel.MEDIUM,
                {"reason": "prompt_too_long", "length": len(text), "max": self.MAX_PROMPT_LENGTH},
            )

        # 2. Token overflow aproximado
        approx_tokens = len(text.split())
        if approx_tokens > self.MAX_PROMPT_TOKENS:
            return GuardrailResult.warn(
                self._msg(
                    f"Prompt extenso (~{approx_tokens} tokens). Puede exceder límites del modelo.",
                    f"Long prompt (~{approx_tokens} tokens). May exceed model limits.",
                ),
                RiskLevel.LOW,
                {"reason": "large_prompt", "approx_tokens": approx_tokens},
            )

        # 3. Prompt injection
        for pattern in self.PROMPT_INJECTION_PATTERNS:
            match = pattern.search(text)
            if match:
                return GuardrailResult.block(
                    self._msg(
                        f"Posible intento de prompt injection detectado: '{match.group()}'",
                        f"Possible prompt injection detected: '{match.group()}'",
                    ),
                    RiskLevel.CRITICAL,
                    {"reason": "prompt_injection", "match": match.group(), "pattern": pattern.pattern},
                )

        # 4. Comandos peligrosos (en prompts sospechosos)
        for pattern in self.DANGEROUS_COMMANDS:
            match = pattern.search(text)
            if match:
                return GuardrailResult.block(
                    self._msg(
                        f"Comando peligroso detectado: '{match.group()}'",
                        f"Dangerous command detected: '{match.group()}'",
                    ),
                    RiskLevel.CRITICAL,
                    {"reason": "dangerous_command", "match": match.group()},
                )

        # 5. XSS
        for pattern in self.XSS_PATTERNS:
            match = pattern.search(text)
            if match:
                return GuardrailResult.block(
                    self._msg(
                        f"Posible XSS detectado: '{match.group()[:50]}'",
                        f"Possible XSS detected: '{match.group()[:50]}'",
                    ),
                    RiskLevel.HIGH,
                    {"reason": "xss", "match": match.group()[:50]},
                )

        # 6. Contenido prohibido
        for pattern in self.PROHIBITED_CONTENT:
            match = pattern.search(text)
            if match:
                return GuardrailResult.block(
                    self._msg(
                        "Contenido no permitido detectado",
                        "Prohibited content detected",
                    ),
                    RiskLevel.CRITICAL,
                    {"reason": "prohibited_content", "match": match.group()},
                )

        return GuardrailResult.allow(
            self._msg("Prompt verificado — sin contenido peligroso", "Prompt verified — no harmful content detected"),
        )

    def check_ai_response(self, response: str) -> GuardrailResult:
        """Evalúa la respuesta generada por IA contra reglas de contenido.

        Args:
            response: Texto generado por el LLM

        Returns:
            GuardrailResult con la decisión
        """
        if not response:
            return GuardrailResult.warn(
                self._msg("Respuesta IA vacía", "Empty AI response"),
                RiskLevel.LOW,
                {"reason": "empty_response"},
            )

        # Buscar indicadores de jailbreak exitoso en la respuesta
        injection_indicators = [
            "i'm free now",
            "no restrictions",
            "without rules",
            "sin restricciones",
            "sin reglas",
            "soy libre",
            "puedo hacer cualquier cosa",
            "i can do anything",
        ]
        for indicator in injection_indicators:
            if indicator in response.lower():
                return GuardrailResult.block(
                    self._msg(
                        "La respuesta IA contiene indicadores de jailbreak",
                        "AI response contains jailbreak indicators",
                    ),
                    RiskLevel.CRITICAL,
                    {"reason": "ai_jailbreak_response", "indicator": indicator},
                )

        return GuardrailResult.allow(
            self._msg("Respuesta IA verificada", "AI response verified"),
        )

    def _msg(self, es: str, en: str) -> str:
        return es if self.lang == "es" else en


# ──────────────────────────────────────────────
#  CAPA 2: ExecutionGuardrails
# ──────────────────────────────────────────────


class ExecutionGuardrails:
    """Límites de ejecución para workflows generados.

    Controla:
    - Número máximo de pasos por workflow
    - Complejidad (profundidad de fork/join/loops)
    - Tamaño máximo de definición del workflow (bytes)
    - Ciclo infinito detection
    - Budget de ejecución (para multi-tenant billing)
    """

    MAX_STEPS: ClassVar[int] = 50
    MAX_DEFINITION_SIZE: ClassVar[int] = 100_000  # 100KB
    MAX_NESTED_DEPTH: ClassVar[int] = 5
    MAX_BUDGET_EXECUTIONS: ClassVar[int] = 1_000  # por tenant/día
    MAX_FORK_BRANCHES: ClassVar[int] = 10
    MAX_RETRY_ATTEMPTS: ClassVar[int] = 10

    LOOP_LIMIT_PATTERNS: ClassVar[list[str]] = [
        "while true",
        "while 1",
        "loop forever",
        "bucle infinito",
        "para siempre",
        "unlimited",
        "sin límite",
        "no limit",
        "999999",
    ]

    def __init__(self, lang: str = "es"):
        self.lang = lang

    def check_workflow_definition(self, workflow: dict) -> GuardrailResult:
        """Valida la definición del workflow contra límites de ejecución.

        Args:
            workflow: Definición completa del workflow

        Returns:
            GuardrailResult con la decisión
        """
        if not workflow:
            return GuardrailResult.block(
                self._msg("Workflow vacío", "Empty workflow"),
                RiskLevel.HIGH,
                {"reason": "empty_workflow"},
            )

        # 1. Tamaño de definición
        import json

        try:
            wf_size = len(json.dumps(workflow))
        except (TypeError, ValueError):
            wf_size = len(str(workflow))

        if wf_size > self.MAX_DEFINITION_SIZE:
            return GuardrailResult.block(
                self._msg(
                    f"Workflow demasiado grande ({wf_size} bytes, máximo {self.MAX_DEFINITION_SIZE})",
                    f"Workflow too large ({wf_size} bytes, max {self.MAX_DEFINITION_SIZE})",
                ),
                RiskLevel.MEDIUM,
                {"reason": "workflow_too_large", "size": wf_size, "max": self.MAX_DEFINITION_SIZE},
            )

        # 2. Número de pasos
        steps = workflow.get("steps", [])
        if len(steps) > self.MAX_STEPS:
            return GuardrailResult.block(
                self._msg(
                    f"Demasiados pasos ({len(steps)}, máximo {self.MAX_STEPS})",
                    f"Too many steps ({len(steps)}, max {self.MAX_STEPS})",
                ),
                RiskLevel.MEDIUM,
                {"reason": "too_many_steps", "steps": len(steps), "max": self.MAX_STEPS},
            )

        # 3. Detectar bucles infinitos
        for step in steps:
            params_str = str(step.get("params", {}))
            for pattern in self.LOOP_LIMIT_PATTERNS:
                if pattern in params_str.lower():
                    return GuardrailResult.block(
                        self._msg(
                            f"Posible bucle infinito detectado en paso {step.get('id', '?')}: '{pattern}'",
                            f"Possible infinite loop detected in step {step.get('id', '?')}: '{pattern}'",
                        ),
                        RiskLevel.HIGH,
                        {"reason": "infinite_loop_detected", "step_id": step.get("id"), "pattern": pattern},
                    )

        # 4. Verificar profundidad de fork/join (recursivo simple)
        max_depth = self._compute_max_depth(steps)
        if max_depth > self.MAX_NESTED_DEPTH:
            return GuardrailResult.block(
                self._msg(
                    f"Workflow demasiado anidado (profundidad {max_depth}, máximo {self.MAX_NESTED_DEPTH})",
                    f"Workflow too deeply nested (depth {max_depth}, max {self.MAX_NESTED_DEPTH})",
                ),
                RiskLevel.MEDIUM,
                {"reason": "too_deep_nesting", "depth": max_depth, "max": self.MAX_NESTED_DEPTH},
            )

        return GuardrailResult.allow(
            self._msg(
                "Workflow dentro de límites de ejecución",
                "Workflow within execution limits",
            ),
        )

    def _compute_max_depth(self, steps: list[dict], current_depth: int = 0, visited: set | None = None) -> int:
        """Computa la profundidad máxima de nesting de un workflow."""
        if visited is None:
            visited = set()
        if current_depth > self.MAX_NESTED_DEPTH:
            return current_depth

        max_depth = current_depth
        for step in steps:
            step_id = step.get("id")
            if step_id and step_id in visited:
                continue
            if step_id:
                visited.add(step_id)

            # Revisar sub-workflows en pasos fork/loop
            sub_steps = step.get("params", {}).get("steps", [])
            if isinstance(sub_steps, list) and sub_steps:
                depth = self._compute_max_depth(sub_steps, current_depth + 1, visited)
                max_depth = max(max_depth, depth)

        return max_depth

    def check_execution_budget(self, tenant_id: str, executions_today: int) -> GuardrailResult:
        """Verifica el budget de ejecuciones para un tenant."""
        if executions_today >= self.MAX_BUDGET_EXECUTIONS:
            return GuardrailResult.block(
                self._msg(
                    f"Límite de ejecuciones diarias alcanzado ({executions_today}/{self.MAX_BUDGET_EXECUTIONS})",
                    f"Daily execution limit reached ({executions_today}/{self.MAX_BUDGET_EXECUTIONS})",
                ),
                RiskLevel.HIGH,
                {"reason": "budget_exceeded", "tenant_id": tenant_id, "executions_today": executions_today},
            )

        return GuardrailResult.allow(
            self._msg(
                f"Budget disponible ({self.MAX_BUDGET_EXECUTIONS - executions_today} ejecuciones restantes)",
                f"Budget available ({self.MAX_BUDGET_EXECUTIONS - executions_today} executions remaining)",
            ),
        )

    def _msg(self, es: str, en: str) -> str:
        return es if self.lang == "es" else en


# ──────────────────────────────────────────────
#  CAPA 3: PIIGuardrails
# ──────────────────────────────────────────────


class PIIGuardrails:
    """Detecta y protege datos sensibles (PII/PHI) en workflows.

    Detecta:
    - Correos electrónicos
    - Teléfonos
    - Números de documento (DNI, CUIT, RUT, SSN)
    - Direcciones IP
    - API keys y tokens
    - Datos bancarios (tarjetas de crédito)
    """

    PII_PATTERNS: ClassVar[dict[str, re.Pattern]] = {
        "email": re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"),
        "phone": re.compile(r"(?:\+?\d{1,3}[\s.-]?)?\(?\d{2,4}\)?[\s.-]?\d{3,4}[\s.-]?\d{3,4}"),
        "credit_card": re.compile(r"\b(?:\d{4}[-\s]?){3}\d{4}\b"),
        "ip_address": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
        "ssn_like": re.compile(r"\b\d{3}[-]\d{2}[-]\d{4}\b"),
        "cuit_argentina": re.compile(r"\b(?:20|23|24|27|30|33|34)\d{8}\d{1}\b"),
        "rut_chile": re.compile(r"\b\d{1,2}\.\d{3}\.\d{3}[-][\dkK]\b"),
        "dni_es": re.compile(r"\b\d{8}[A-Z]\b"),
        "api_key_like": re.compile(r"(?:api[_-]?key|apikey|secret[_-]?key|token)\s*[:=]\s*['\"][^'\"]+['\"]", re.IGNORECASE),
        "bearer_token": re.compile(r"bearer\s+[a-zA-Z0-9._\-]+", re.IGNORECASE),
    }

    # Campos de workflow que típicamente contienen PII
    PII_SENSITIVE_PARAMS: ClassVar[set[str]] = {
        "email", "to", "cc", "bcc", "phone", "telefono", "celular",
        "name", "nombre", "last_name", "apellido", "full_name",
        "address", "direccion", "domicilio",
        "dni", "cuit", "rut", "ssn", "tax_id",
        "password", "pass", "secret", "api_key", "token",
        "credit_card", "card_number", "cvv",
        "ip", "ip_address",
    }

    SENIORITY_THRESHOLDS: ClassVar[dict[str, int]] = {
        "email": 5,      # 5+ emails → medium risk
        "phone": 3,       # 3+ phones → medium risk
        "credit_card": 1, # 1 credit card → critical
        "ssn_like": 1,    # 1 SSN → critical
        "cuit_argentina": 5,  # 5+ CUIT → medium
    }

    def __init__(self, lang: str = "es"):
        self.lang = lang

    def check_workflow_for_pii(self, workflow: dict) -> GuardrailResult:
        """Escanea un workflow completo en busca de PII.

        Args:
            workflow: Definición del workflow

        Returns:
            GuardrailResult con detección de PII
        """
        if not workflow:
            return GuardrailResult.allow(self._msg("Workflow vacío", "Empty workflow"))

        # Convertir todo el workflow a string para escaneo
        wf_str = str(workflow).lower()

        findings: dict[str, list[str]] = {}
        total_findings = 0

        for pii_type, pattern in self.PII_PATTERNS.items():
            matches = pattern.findall(wf_str)
            if matches:
                # Filtrar falsos positivos (números de versión, años, etc.)
                clean_matches = self._filter_false_positives(pii_type, matches)
                if clean_matches:
                    findings[pii_type] = clean_matches[:5]  # Top 5
                    total_findings += len(clean_matches)

        if not findings:
            return GuardrailResult.allow(
                self._msg("Sin datos sensibles detectados", "No sensitive data detected"),
            )

        # Determinar nivel de riesgo
        risk = self._assess_pii_risk(findings, total_findings)

        if risk in (RiskLevel.HIGH, RiskLevel.CRITICAL):
            return GuardrailResult.block(
                self._msg(
                    f"Datos sensibles detectados ({total_findings} hallazgos): {', '.join(findings.keys())}",
                    f"Sensitive data detected ({total_findings} findings): {', '.join(findings.keys())}",
                ),
                risk,
                {"reason": "pii_detected", "findings": findings, "total": total_findings},
            )

        return GuardrailResult.warn(
            self._msg(
                f"Posibles datos personales detectados ({total_findings} hallazgos). Verificar antes de ejecutar.",
                f"Possible personal data detected ({total_findings} findings). Verify before execution.",
            ),
            risk,
            {"reason": "pii_detected", "findings": findings, "total": total_findings},
        )

    def check_params_for_pii(self, params: dict) -> GuardrailResult:
        """Escanea parámetros específicos en busca de PII.

        Útil para validar slots antes de compilar el workflow.
        """
        if not params:
            return GuardrailResult.allow()

        sensitive_found = []
        for key, value in params.items():
            if key in self.PII_SENSITIVE_PARAMS and isinstance(value, str) and len(value) > 2:
                sensitive_found.append({"param": key, "value": value[:20]})  # Truncado

        if sensitive_found:
            return GuardrailResult.warn(
                self._msg(
                    f"Parámetros con datos sensibles: {', '.join(p['param'] for p in sensitive_found)}",
                    f"Parameters with sensitive data: {', '.join(p['param'] for p in sensitive_found)}",
                ),
                RiskLevel.LOW,
                {"reason": "pii_in_params", "params": sensitive_found},
            )

        return GuardrailResult.allow()

    def _filter_false_positives(self, pii_type: str, matches: list[str]) -> list[str]:
        """Filtra falsos positivos conocidos por tipo de PII."""
        if pii_type == "ip_address":
            # Filtrar versiones, años, etc.
            return [m for m in matches if not any(
                sub in m for sub in ["0.0.0.0", "127.0.0.1", "255.255.255.255", "1.1.1.1", "8.8.8.8"]
            )]
        if pii_type == "email":
            # Filtrar emails de ejemplo
            return [m for m in matches if not any(
                sub in m.lower() for sub in ["example.com", "test.com", "domain.com", "@corp.com"]
            )]
        if pii_type == "credit_card":
            # Filtrar números de tarjeta de prueba
            return [m for m in matches if not any(
                sub in m.replace("-", "").replace(" ", "") for sub in ["4111111111111111", "4242424242424242"]
            )]
        return matches

    def _assess_pii_risk(self, findings: dict[str, list[str]], total: int) -> RiskLevel:
        """Determina el nivel de riesgo basado en hallazgos de PII."""
        # Crítico: tarjetas de crédito, SSN
        for critical_type in ("credit_card", "ssn_like"):
            if critical_type in findings:
                return RiskLevel.CRITICAL

        # Alto: datos bancarios, tokens, CUIT/RUT
        for high_type in ("cuit_argentina", "rut_chile", "api_key_like", "bearer_token"):
            if high_type in findings:
                return RiskLevel.HIGH

        # Medio: muchos emails o teléfonos
        for medium_type, threshold in self.SENIORITY_THRESHOLDS.items():
            if medium_type in findings and len(findings[medium_type]) >= threshold:
                return RiskLevel.MEDIUM

        # Bajo: hallazgos aislados de baja sensibilidad
        if total <= 3:
            return RiskLevel.LOW

        return RiskLevel.MEDIUM

    def mask_pii(self, text: str) -> str:
        """Enmascara datos PII en un texto (para logging seguro)."""
        for pii_type, pattern in self.PII_PATTERNS.items():
            if pii_type == "email":
                text = pattern.sub(lambda m: m.group()[0] + "***@" + m.group().split("@")[1], text)
            elif pii_type == "credit_card":
                text = pattern.sub("****-****-****-####", text)
            elif pii_type in ("phone", "ip_address"):
                text = pattern.sub("***", text)
            else:
                text = pattern.sub("***", text)
        return text

    def _msg(self, es: str, en: str) -> str:
        return es if self.lang == "es" else en


# ──────────────────────────────────────────────
#  GUARDRAIL COMPUESTO
# ──────────────────────────────────────────────


@dataclass
class CompositeGuardrailResult:
    """Resultado agregado de todas las capas de guardrail."""

    overall_passed: bool
    overall_action: GuardrailAction
    checks: dict[str, GuardrailResult]
    risk: RiskLevel = RiskLevel.LOW

    @property
    def blocked(self) -> bool:
        return self.overall_action == GuardrailAction.BLOCK

    @property
    def warnings(self) -> list[GuardrailResult]:
        return [r for r in self.checks.values() if r.action == GuardrailAction.WARN and r.passed]

    @property
    def blocks(self) -> list[GuardrailResult]:
        return [r for r in self.checks.values() if r.action == GuardrailAction.BLOCK]


class GuardrailManager:
    """Orquestador de los tres tipos de guardrails.

    Úsalo como punto de entrada único para evaluar prompts y workflows.
    """

    def __init__(self, lang: str = "es"):
        self.lang = lang
        self.content = ContentGuardrails(lang)
        self.execution = ExecutionGuardrails(lang)
        self.pii = PIIGuardrails(lang)

    def check_prompt(self, text: str) -> CompositeGuardrailResult:
        """Evalúa un prompt del usuario contra todas las capas."""
        checks: dict[str, GuardrailResult] = {
            "content": self.content.check_prompt(text),
        }
        return self._aggregate(checks)

    def check_workflow(self, workflow: dict) -> CompositeGuardrailResult:
        """Evalúa un workflow completo contra todas las capas."""
        checks: dict[str, GuardrailResult] = {
            "execution": self.execution.check_workflow_definition(workflow),
            "pii": self.pii.check_workflow_for_pii(workflow),
        }
        return self._aggregate(checks)

    def check_all(self, prompt: str, workflow: dict) -> CompositeGuardrailResult:
        """Evalúa prompt + workflow contra todas las capas."""
        checks: dict[str, GuardrailResult] = {
            "content": self.content.check_prompt(prompt),
            "execution": self.execution.check_workflow_definition(workflow),
            "pii": self.pii.check_workflow_for_pii(workflow),
        }
        return self._aggregate(checks)

    def _aggregate(self, checks: dict[str, GuardrailResult]) -> CompositeGuardrailResult:
        """Agrega múltiples resultados de guardrail en uno compuesto."""
        blocks = [r for r in checks.values() if r.action == GuardrailAction.BLOCK]
        warnings = [r for r in checks.values() if r.action == GuardrailAction.WARN and r.passed]
        risks = [r.risk for r in checks.values()]

        # Prioridad de riesgo
        risk_order = [RiskLevel.CRITICAL, RiskLevel.HIGH, RiskLevel.MEDIUM, RiskLevel.LOW]
        max_risk = RiskLevel.LOW
        for risk in risk_order:
            if risk in risks:
                max_risk = risk
                break

        if blocks:
            return CompositeGuardrailResult(
                overall_passed=False,
                overall_action=GuardrailAction.BLOCK,
                checks=checks,
                risk=max_risk,
            )

        if warnings:
            return CompositeGuardrailResult(
                overall_passed=True,
                overall_action=GuardrailAction.WARN,
                checks=checks,
                risk=max_risk,
            )

        return CompositeGuardrailResult(
            overall_passed=True,
            overall_action=GuardrailAction.ALLOW,
            checks=checks,
            risk=RiskLevel.LOW,
        )
