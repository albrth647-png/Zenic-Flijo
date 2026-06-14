# Zenic-Flujo — Fase 1: Código y Calidad — Reporte de Errores Reales

**Fecha:** 2026-06-13
**Proyecto:** Zenic-Flujo
**Directorio analizado:** `src/` (350+ archivos Python)

---

## 📋 Resumen Ejecutivo

| Herramienta | Errores Críticos | Errores Altos | Warnings | Total |
|-------------|------------------|---------------|----------|-------|
| **Ruff** | 0 | 1 | 1 | 2 |
| **Semgrep** | 1 | 11 | 0 | 36* |
| **Vulture** (100% conf.) | 0 | 10 | 0 | 10 |
| **Ty (Type checking)** | 0 | 0 | 0 | 0 |
| **TOTAL** | **1** | **22** | **1** | **48** |

> *Semgrep reporta 36 findings totales, algunos duplicados del mismo patrón en distintos archivos.

---

## 1. RUFF — Linting y Formateo

**Configuración:** `ruff.toml` (target py312, line-length 120)
**Reglas:** E, W, F, I, N, UP, B, SIM, C4, T20, RUF

### Hallazgos (2)

| # | Archivo | Línea | Código | Descripción | Fixable |
|---|---------|-------|--------|-------------|---------|
| 1 | `src/partnership/models.py` | 6:36 | **F401** | `dataclasses.field` importado pero no usado | ✅ Sí |
| 2 | *(varios)* | — | **W292** | No newline at end of file | ✅ Sí |

---

## 2. SEMGREP — Patrones de Seguridad y Bugs

**Reglaset:** `auto` (1059 reglas community)
**Archivos escaneados:** 350

### Hallazgos CRÍTICOS y ALTOS

| # | Severidad | Regla | Archivo | Línea | Descripción |
|---|-----------|-------|---------|-------|-------------|
| 1 | 🔴 CRITICAL | `eval-detected` | `src/agents/memory.py` | 310 | `eval(row[6])` — RCE potential si input de BD controlable |
| 2 | 🔴 HIGH | `wildcard-cors` | `src/api_v2/app.py` | 202 | `allow_origins=["*"]` — CORS wildcard inseguro |
| 3 | 🔴 HIGH | `non-literal-import` | `src/cli/commands/helpers.py` | 95 | `importlib.import_module(module_name)` sin whitelist |
| 4 | 🔴 HIGH | `non-literal-import` | `src/cli/commands/helpers.py` | 122 | `importlib.import_module(module_name)` duplicado |
| 5 | 🔴 HIGH | `sqlalchemy-execute-raw-query` | `src/connectors/mysql_connector.py` | 329 | SQL concatenado sin prepared statements |
| 6 | 🔴 HIGH | `formatted-sql-query` | `src/connectors/mysql_connector.py` | 382 | Formatted SQL query |
| 7 | 🔴 HIGH | `sqlalchemy-execute-raw-query` | `src/connectors/mysql_connector.py` | 193 | f-string en PRAGMA table_info |
| 8 | 🔴 HIGH | `formatted-sql-query` | `src/connectors/mysql_connector.py` | 230 | f-string en PRAGMA table_info |
| 9 | 🔴 HIGH | `sqlalchemy-execute-raw-query` | `src/connectors/mysql_connector.py` | 262 | f-string en UPDATE |
| 10 | 🔴 HIGH | `sqlalchemy-execute-raw-query` | `src/connectors/mysql_connector.py` | 280 | f-string en DELETE |
| 11 | 🔴 HIGH | `sqlalchemy-execute-raw-query` | `src/tools/integrations/postgresql_service.py` | 150 | Raw query sin parametrizar |
| 12 | 🔴 HIGH | `sqlalchemy-execute-raw-query` | `src/tools/integrations/postgresql_service.py` | 206 | Raw query sin parametrizar |
| 13 | 🔴 HIGH | `sqlalchemy-execute-raw-query` | `src/tools/inventory/repository.py` | 64 | f-string en UPDATE products |
| 14 | 🔴 HIGH | `sqlalchemy-execute-raw-query` | `src/workflow/repository.py` | 216 | f-string en UPDATE workflow_definitions |
| 15 | 🟡 MEDIUM | `logger-credential-leak` | `src/agents/token_tracking.py` | 291 | Log de tokens/costos |
| 16 | 🟡 MEDIUM | `logger-credential-leak` | `src/agents/token_tracking.py` | 330 | Log de error con exc |

### Categorías de riesgo

| Categoría | Count | Archivos afectados |
|-----------|-------|-------------------|
| RCE / Code Injection | 3 | `agents/memory.py`, `cli/commands/helpers.py` (x2) |
| SQL Injection | 9 | `mysql_connector.py` (x5), `postgresql_service.py` (x2), `inventory/repository.py`, `workflow/repository.py` |
| CORS Inseguro | 1 | `api_v2/app.py` |
| Credential Leak | 2 | `agents/token_tracking.py` (x2) |

---

## 3. VULTURE — Dead Code (100% Confianza)

**Min confidence:** 80% | **Scope:** `src/`

### Variables asignadas pero nunca leídas (10 reales)

| # | Archivo | Línea | Variable | Contexto |
|---|---------|-------|----------|----------|
| 1 | `src/agents/token_tracking.py` | 359 | `new_cost` | Asignada en cálculo, nunca usada |
| 2 | `src/bpmn/exporter.py` | 16 | `pretty` | Parámetro de función no usado |
| 3 | `src/cli/commands/helpers.py` | 441 | `old_version` | Capturada en except, no usada |
| 4 | `src/mobile/api.py` | 329 | `changes` | Variable local no usada |
| 5 | `src/mobile/api.py` | 401 | `preferences` | Variable local no usada |
| 6 | `src/observability/metrics.py` | 312 | `exc_tb` | Traceback capturado, no usado |
| 7 | `src/sdk/base/connector.py` | 197 | `exc_tb` | Traceback capturado, no usado |
| 8 | `src/sdk/http_client.py` | 490 | `exc_tb` | Traceback capturado, no usado |
| 9 | `src/tools/code_runner/sandbox.py` | 123 | `frame` | Signal handler param no usado |
| 10 | `src/tools/code_runner/sandbox.py` | 123 | `signum` | Signal handler param no usado |

> A 60% confianza vulture reporta ~400 items, mayormente falsos positivos (rutas Flask/FastAPI registradas dinámicamente).

---

## 4. TY — Type Checking

```
0 diagnostics
0 errors
0 warnings
```

---

## 5. ANALIZADOR COMBINADO

| Métrica | Valor |
|---------|-------|
| Ruff issues | 2 (1 fixable) |
| Ty diagnostics | 0 |
| Vulture unused (100%) | 10 |
| **Code Quality Score** | **98/100** |

---

## 🎯 Plan de Acción Priorizado

### 🔴 Prioridad CRÍTICA

| # | Acción | Archivo | Esfuerzo |
|---|--------|---------|----------|
| 1 | Reemplazar `eval()` por `json.loads()` / `ast.literal_eval()` | `src/agents/memory.py:310` | Bajo |
| 2 | Configurar CORS origins desde env var | `src/api_v2/app.py:202` | Bajo |
| 3 | Añadir whitelist a `importlib.import_module()` | `src/cli/commands/helpers.py:95,122` | Medio |

### 🟡 Prioridad ALTA

| # | Acción | Archivos | Esfuerzo |
|---|--------|----------|----------|
| 4 | Prepared statements en todos los SQL | mysql, postgres, inventory, workflow | Alto |
| 5 | Sanitizar logs de tokens | `src/agents/token_tracking.py` | Bajo |

### 🟢 Prioridad MEDIA

| # | Acción | Archivos | Esfuerzo |
|---|--------|----------|----------|
| 6 | Eliminar 10 variables dead code | Ver tabla Vulture | Bajo |
| 7 | Fix F401 import unused | `src/partnership/models.py:6` | Trivial |
| 8 | Fix W292 newline EOF | varios | Trivial |

---

## 📦 Lista de Archivos a Modificar (17 archivos)

```
src/agents/memory.py                      # eval -> literal_eval
src/api_v2/app.py                         # CORS wildcard -> env var
src/cli/commands/helpers.py               # importlib whitelist
src/connectors/mysql_connector.py         # 5x SQL injection fixes
src/tools/integrations/postgresql_service.py  # 2x SQL fixes
src/tools/inventory/repository.py         # 1x SQL fix
src/workflow/repository.py                # 1x SQL fix
src/agents/token_tracking.py              # log sanitization + dead var
src/partnership/models.py                 # F401 unused import
src/bpmn/exporter.py                      # pretty param unused
src/mobile/api.py                         # changes, preferences unused
src/observability/metrics.py              # exc_tb unused
src/sdk/base/connector.py                 # exc_tb unused
src/sdk/http_client.py                    # exc_tb unused
src/tools/code_runner/sandbox.py          # frame, signum unused
```

---

## 🔍 Comandos de Verificación Post-Fix

```bash
ruff check src/ --config ruff.toml
semgrep --config=auto src/
vulture src/ --min-confidence 80
```

---

*Documento generado automáticamente por análisis Fase 1 — Zenic-Flujo*
