# Plan de Rollout: Code-Forge al Proyecto Completo

> **Versión**: 1.1
> **Proyecto**: Zenic-Flujo v3.2.0 (~176K LOC, Python + TypeScript, 781 `.py` + 147 frontend)
> **Objetivo**: Homologar todo el proyecto bajo el estándar Code-Forge (8 fases, 12 gates, RunLedger, Sandbox, Memoria Cross-Session)
> **Última actualización**: 2026-06-27

---

## 📍 Estado Actual (Fase 0 — COMPLETA ✅)

| Subfase | Estado | Detalle |
|---------|--------|---------|
| 0.1 Tests unitarios | ✅ COMPLETO | test_sandbox.py (23 tests), test_gates.py (76 tests + 1 skip), test_run_ledger.py (48 tests) — **147 tests total** |
| 0.2 Self-test | ✅ COMPLETO | `python -m forge self-test` funciona. EXPENSIVE_GATES excluídos por lentitud. TS gates no corren sin node_modules |
| 0.3 Referencias | ✅ COMPLETO | 6 docs en forge/references/ (1442 líneas) revisados y coherentes |
| 0.4 CLI | ✅ COMPLETO | forge/cli.py (5 comandos: init, verify, check-module, report, self-test) + forge/__main__.py |
| Any→TypedDict | ✅ COMPLETO | gates.py, run_ledger.py, memory.py, sandbox.py — sin `Any` residual |
| RuntimeWarning | ✅ FIXED | Eliminado `__name__ == "__main__"` de gates.py. Entry point via `python -m forge` |
| self_test() fix | ✅ FIXED | No crea frontend/ temp dir (colgaba con npx) |

### Próximo: Fase 1 (Python Gates) — PENDIENTE

| Componente | Estado | Observación |
|---|---|---|
| `forge/` módulos | ✅ Existen (4/4) | RunLedger, PersistentMemory, ForgeSandbox, GateRunner |
| `run_ledger.py` | ✅ Implementado | 294 LOC, JSON persistence, integrity checks |
| `memory.py` | ✅ Implementado | Jaccard similarity, cross-session |
| `sandbox.py` | ✅ Implementado | Dual sandbox, rlimits, env sanitization |
| `gates.py` | ✅ Implementado | 12 gates, SecurityScanner, concurrent execution |
| **pytest** | ✅ Instalado | Python tests runner |
| **tsc** | ✅ Instalado | TypeScript compiler |
| **ruff** | ❌ No instalado | Python linter |
| **mypy** | ❌ No instalado | Python type checker |
| **radon** | ❌ No instalado | Python complexity analyzer |
| **mutmut** | ❌ No instalado | Python mutation testing |
| **coverage** | ❌ No instalado | Python coverage |
| **vitest** | ❌ node_modules faltante | TS test runner |
| **eslint** | ❌ node_modules faltante | TS linter |
| **madge** | ❌ node_modules faltante | Circular deps detector |
| **stryker** | ❌ node_modules faltante | TS mutation testing |
| **2088 tests Python** | ✅ Existentes | 107 test files |
| **Frontend tests** | ⚠️ Sin node_modules | Vitest no puede correr |
| **Python gates tests** | ⚠️ Parcial | workflow determinista presente |

---

## 📋 Fases del Rollout

### Fase 0: Fundación — Hardening de forge/

**Duración estimada**: 2-3 días  
**Riesgo**: Bajo  
**Dependencias**: Ninguna  
**Estado**: ✅ COMPLETA

#### 0.1 Tests unitarios de forge/
- [x] Tests para `RunLedger` (creación, append action, rollback, integrity check, corrupted ledger detection) — **48 tests**
- [x] Tests para `PersistentMemory` (add_reflection, find_similar, Jaccard correctness, persistence) — _integrados en tests de gates_
- [x] Tests para `ForgeSandbox` (run, isolation, cleanup) — **23 tests**
- [x] Tests para `GateRunner` (run_all, each individual gate) — **76 tests + 1 skip**

#### 0.2 GateRunner auto-test
- [x] Self-test vía CLI: `python -m forge self-test`
- [x] EXPENSIVE_GATES (`mutation_score`, `coverage_branch`) excluídos de self-test por lentitud
- [x] TS gates no corren sin node_modules (detectado automáticamente)

#### 0.3 Referencias y best-practices
- [x] Revisar/actualizar `forge/references/` (6 docs existentes, 1442 líneas)
- [x] Coherentes con código actual

#### 0.4 Entry point CLI
- [x] `forge/cli.py` con 5 comandos:
  ```bash
  python -m forge init          # Inicializa ledger en directorio
  python -m forge verify        # Corre 12 gates sobre el proyecto
  python -m forge check-module src/hat/  # Gates sobre un módulo específico
  python -m forge report        # Genera reporte de estado
  python -m forge self-test     # Auto-test de gates
  ```
- [x] `forge/__main__.py` — entry point

#### 0.5 Migración Any → TypedDict
- [x] `gates.py`: ScanIssue, CmdResult, GateResultDict, HardGateReport, SoftGoalReport, OverallReport, EvalReport
- [x] `run_ledger.py`: LedgerAction, Approval, GateProof, LedgerMetadata, LedgerData, LedgerSummary
- [x] `memory.py`: Reflection, MemoryData, MemoryStats
- [x] `sandbox.py`: RunResult, StopStats, LogEvent
- [x] **0 ocurrencias de `Any` en forge/** ✅

---

### Fase 1: Python Gates — Instalación y Primera Pasada

**Duración estimada**: 3-5 días  
**Riesgo**: Medio  
**Dependencias**: Fase 0  

#### 1.1 Instalar herramientas Python
```bash
pip install ruff mypy radon mutmut pytest-cov pytest-mock
```

#### 1.2 Gate: `lint_clean` (ruff)
- [ ] Correr `ruff check src/` — diagnosticar estado actual
- [ ] Clasificar errores por severidad (E/W/F/I/N/UP/B/SIM/C4/RUF)
- [ ] **Subfase 1.2A**: Auto-fix de reglas seguras (`ruff check --fix src/`)
- [ ] **Subfase 1.2B**: Fix manual de reglas restantes (organizado por módulo)
- [ ] **Subfase 1.2C**: Configurar ruff en CI como gate bloqueante
- [ ] **Métrica target**: `ruff check src/ --quiet` → exit 0

#### 1.3 Gate: `types_clean` (mypy)
- [ ] Correr `mypy src/` — diagnosticar estado actual
- [ ] Crear `mypy.ini` con configuración gradual:
  ```ini
  [mypy]
  python_version = 3.12
  strict = true
  ignore_missing_imports = true
  
  [mypy-src.hat.level5_tools.*]
  # Nivel 4 tools tienen menos presión de tipos
  disallow_untyped_defs = false
  ```
- [ ] **Subfase 1.3A**: Módulos core (src/core/, src/orbital/) — strict primero
- [ ] **Subfase 1.3B**: HAT (src/hat/) — strict en level0 y level1
- [ ] **Subfase 1.3C**: Resto de módulos — gradual con config por módulo
- [ ] **Métrica target**: `mypy src/` → exit 0

#### 1.4 Gate: `complexity_max` (radon)
- [ ] Correr `radon cc src/ -s -n C` para detectar módulos con alta complejidad
- [ ] Identificar God Classes / funciones > 50 LOC / cyclomatic > 15
- [ ] Refactorizar top-10 módulos más complejos
- [ ] **Métrica target**: `radon cc src/ -s -n C` → 0 resultados (nada > C)

#### 1.5 Gate: `mutation_score` (mutmut)
- [ ] Correr `mutmut run --paths-to-source src/ --paths-to-tests src/tests/`
- [ ] Diagnosticar score actual (baseline)
- [ ] Añadir tests para matar mutantes en módulos core
- [ ] **Métrica target**: score ≥ 80% en módulos core, ≥ 60% global

#### 1.6 Gate: `no_security_issues`
- [ ] Verificar que SecurityScanner (ya existe en gates.py) funciona correctamente
- [ ] Correr sobre todo `src/` y listar hallazgos
- [ ] Remediar: eliminar eval/exec/pickle/shell=True donde existan
- [ ] **Métrica target**: 0 hallazgos de seguridad

#### 1.7 Gate: `no_broken_imports` + `no_circular_imports`
- [ ] Verificar imports: `python -c "import src.core; import src.orbital; ..."`
- [ ] Circular imports: AST DFS scan (ya implementado en gates.py)
- [ ] **Métrica target**: 0 broken imports, 0 circular deps

---

### Fase 2: TypeScript Gates — Frontend al Estándar

**Duración estimada**: 3-5 días  
**Riesgo**: Medio-Alto  
**Dependencias**: Fase 0  

#### 2.1 Instalar dependencias frontend
```bash
cd frontend && npm install
```

#### 2.2 Gate: `lint_clean` (eslint)
- [ ] Correr `npx eslint .` — diagnosticar estado actual
- [ ] Fix automático: `npx eslint . --fix`
- [ ] Fix manual de reglas restantes
- [ ] **Métrica target**: `npx eslint . --max-warnings=0` → exit 0

#### 2.3 Gate: `types_clean` (tsc)
- [ ] Correr `npx tsc --noEmit` — diagnosticar errores
- [ ] Clasificar por severidad (strict mode vs standard)
- [ ] Fix gradual por módulo
- [ ] **Métrica target**: `npx tsc --noEmit --strict` → exit 0

#### 2.4 Gate: `tests_pass` (vitest)
- [ ] Escribir tests faltantes para frontend
- [ ] Verificar que `npx vitest run` pasa
- [ ] **Métrica target**: `vitest run` → exit 0

#### 2.5 Gate: `no_circular_imports` (madge)
- [ ] Correr `npx madge --circular frontend/src/`
- [ ] Resolver circular dependencies encontradas
- [ ] **Métrica target**: `madge --circular frontend/src/` → 0 results

#### 2.6 Gate: `mutation_score` (stryker)
- [ ] Configurar Stryker con `npx stryker init`
- [ ] Correr mutation testing sobre módulos core del frontend
- [ ] Añadir tests para matar mutantes
- [ ] **Métrica target**: score ≥ 75% en módulos core

#### 2.7 Gate: `coverage_branch`
- [ ] Configurar vitest con `--coverage`
- [ ] **Métrica target**: branch coverage ≥ 85% en módulos core

#### 2.8 Gate: `complexity_max`
- [ ] Configurar eslint complexity rule
- [ ] Refactorizar componentes > 200 LOC o con cyclomatic > 10
- [ ] **Métrica target**: max cyclomatic complexity ≤ 10

---

### Fase 3: Sandbox — Entorno de Ejecución Aislado

**Duración estimada**: 2 días  
**Riesgo**: Bajo  
**Dependencias**: Fase 0  

#### 3.1 Verificar ForgeSandbox
- [ ] Tests de fs isolation: crear archivo temporal, verificar que no afecta project_root
- [ ] Tests de network allowlist: intentar conexión a dominio no permitido → debe bloquear
- [ ] Tests de rlimits: verificar límites de CPU/RAM/filesize
- [ ] Tests de env sanitization: verificar que secrets no se filtran

#### 3.2 Integrar sandbox en gates.py
- [ ] Hacer que GateRunner ejecute gates dentro del sandbox
- [ ] `ForgeSandbox` como context manager en `GateRunner.run_all()`

#### 3.3 Modo airgap para sandbox
- [ ] Detectar si el sandbox corre en modo offline (sin red)
- [ ] Desactivar gates que requieran red (npm install, pip install)
- [ ] **Target**: sandbox funcional 100% offline

---

### Fase 4: RunLedger — Trazabilidad Total

**Duración estimada**: 2-3 días  
**Riesgo**: Bajo  
**Dependencias**: Fase 0  

#### 4.1 Verificar RunLedger
- [ ] Tests de integridad: crear ledger, añadir acciones, verificar persistencia
- [ ] Tests de rollback: simular acción, ejecutar rollback, verificar estado
- [ ] Tests de corrupción: modificar ledger manualmente → detectar corrupción
- [ ] Tests de handoff: serializar/deserializar ledger entre sesiones

#### 4.2 Template de ledger para el proyecto
- [ ] Crear `forge/templates/run_ledger.json` con estructura canónica
- [ ] Documentar campos obligatorios por tipo de acción:
  - `edit_file`: before_sha, after_sha, rollback, stack (python/ts)
  - `create_file`: content_hash, rollback (delete)
  - `delete_file`: content_backup, rollback (restore)
  - `refactor`: before_sha_glob, after_sha_glob, blast_radius

#### 4.3 Integrar ledger en el flujo de trabajo
- [ ] Pre-commit hook: verificar que run_ledger.json está actualizado
- [ ] CI check: verificar integridad del ledger en cada PR
- [ ] **Target**: cada cambio al proyecto tiene ledger asociado

---

### Fase 5: Memoria Cross-Session — Aprendizaje Continuo

**Duración estimada**: 1-2 días  
**Riesgo**: Bajo  
**Dependencias**: Fase 0  

#### 5.1 Verificar PersistentMemory
- [ ] Tests de Jaccard similarity: añadir reflexiones, buscar similares
- [ ] Tests de persistencia: guardar/cargar entre sesiones
- [ ] Tests de scoring: score alto debe priorizarse en búsqueda

#### 5.2 Poblar memoria inicial
- [ ] Extraer lecciones aprendidas de commits pasados (git log)
- [ ] Poblar `memory.json` con reflexiones iniciales:
  - Errores comunes de import
  - Patrones de tipo que fallan
  - Security hotspots conocidos
  - Decisiones arquitectónicas pasadas

#### 5.3 Integrar memory en GateRunner
- [ ] Cuando un gate falla, generar reflexión automática
- [ ] Guardar en `forge/memory.json`
- [ ] **Target**: cada iteración de gates genera reflexión utilizable

---

### Fase 6: Homologación por Módulo

**Duración estimada**: 5-8 días  
**Riesgo**: Alto  
**Dependencias**: Fases 1-5  

Aplicar el ciclo completo code-forge a cada módulo del proyecto, en orden de criticidad:

```
Orden de homologación:
  1. src/core/          ← infraestructura base (dependencia de todo)
  2. src/orbital/       ← motor determinista (diferenciador competitivo)
  3. src/hat/           ← HAT 5 niveles (orquestación)
  4. src/events/        ← EventBus (cross-cutting)
  5. src/nlu/           ← NLU pipeline
  6. src/workflow/      ← motor de workflows
  7. src/hat/level5_tools/  ← 19 tools ZF
  8. src/web/           ← Flask UI
  9. src/api_v2/        ← FastAPI
  10. frontend/src/     ← SPA React
  11. src/connectors/   ← 65 conectores externos
  12. src/tools/        ← tools legacy (migrar o eliminar)
```

**Por cada módulo**:
1. `forge init` — crear ledger
2. `forge verify --module src/<modulo>/` — correr 12 gates
3. Si falla → ciclo CRITIQUE → FIX hasta pasar
4. Documentar reflexiones en memory
5. Marcar módulo como HOMOLOGADO

---

### Fase 7: CI/CD — Automatización de Gates

**Duración estimada**: 2 días  
**Riesgo**: Bajo  
**Dependencias**: Fases 1-2  

#### 7.1 GitHub Actions workflow
- [ ] Crear `.github/workflows/code-forge.yml`
- [ ] Triggers: push a main, PR a main
- [ ] Pasos:
  1. `forge verify --quick` (lint + types + imports — 2 min)
  2. `forge verify --full` (12 gates completos — 15 min)
  3. `forge report` → comentario en PR

#### 7.2 Pre-commit hooks
- [ ] Crear `.pre-commit-config.yaml`
- [ ] Hooks: ruff, eslint, tsc, madge
- [ ] `forge check-staged` → fast path para staged files

#### 7.3 Dashboard de calidad
- [ ] `forge dashboard` → HTML report con:
  - Score por módulo (radar chart)
  - Gates pasando/fallando
  - Historial de scores (últimas 10 ejecuciones)
  - Tendencias de calidad

---

### Fase 8: Documentación y Onboarding

**Duración estimada**: 2 días  
**Riesgo**: Bajo  
**Dependencias**: Fases 0-7  

#### 8.1 Quickstart
- [ ] `docs/code-forge-quickstart.md` — cómo empezar a usar code-forge
  ```bash
  # Después de clonar
  pip install -r requirements.txt
  cd frontend && npm install
  
  # Verificar que todo está listo
  python -m forge verify --quick
  
  # Para un cambio:
  python -m forge start "descripción del cambio"
  ```

#### 8.2 Workflow de desarrollo
- [ ] `docs/code-forge-workflow.md`:

```
1. python -m forge start "mi feature"   → crea ledger + spec
2. Haces cambios...
3. python -m forge verify               → corre 12 gates
4. Si falla → python -m forge fix       → CRITIQUE + FIX loop
5. python -m forge commit "mensaje"     → ledger + commit
6. python -m forge pr                    → ledger + PR
```

#### 8.3 Training
- [ ] Ejemplos concretos en `docs/code-forge-examples/`:
  - `01-fix-bug-crm.md` — fix de bug con ciclo completo
  - `02-add-tool.md` — añadir una tool N4 paso a paso
  - `03-refactor-module.md` — refactor con gates y rollback

---

## 📈 Métricas de Éxito

| Fase | Métrica | Target | Cómo se mide |
|------|---------|--------|-------------|
| F1 | ruff clean | `ruff check src/ --quiet` → exit 0 | `ruff check` |
| F1 | mypy clean | `mypy src/` → exit 0 | `mypy` |
| F1 | radon clean | `radon cc src/ -s -n C` → 0 | `radon` |
| F1 | mutmut score | ≥ 80% core, ≥ 60% global | `mutmut run` |
| F2 | eslint clean | `eslint frontend/src/` → exit 0 | `eslint` |
| F2 | tsc clean | `tsc --noEmit --strict` → exit 0 | `tsc` |
| F2 | vitest pass | `vitest run` → exit 0 | `vitest` |
| F2 | madge clean | `madge --circular` → 0 | `madge` |
| F2 | stryker score | ≥ 75% core | `stryker run` |
| F6 | módulos homologados | 12/12 módulos | `forge list-homologated` |
| F7 | CI gates | 100% PRs con gates verdes | GitHub Checks |
| Global | Score compuesto | ≥ 8.5/10 | `forge score` |

---

## 🗺️ Roadmap Temporal

```
Semana 1-2:  Fase 0 (Fundación forge) + Fase 1 (Python Gates)
Semana 3-4:  Fase 2 (TypeScript Gates)
Semana 5:    Fase 3 (Sandbox) + Fase 4 (RunLedger) + Fase 5 (Memory)
Semana 6-8:  Fase 6 (Homologación por módulo)
Semana 9:    Fase 7 (CI/CD) + Fase 8 (Docs)

Total: ~9 semanas (2 meses)
```

**Quick win** (primeros 3 días): Fase 0 + Fase 1.1-1.2 (ruff auto-fix) — resultado visible inmediato.

---

## 🛑 Riesgos y Mitigaciones

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| mutmut extremadamente lento (2088 tests) | Alta | Alto | Ejecutar mutmut por módulo, no global. Usar `--timeout-factor`. Parallel execution |
| mypy strict rompe todo el codebase | Alta | Medio | Config gradual por módulo. Empezar con core/ y orbital/ |
| stryker timeout en CI | Media | Medio | Limitar a módulos core. Timeout generoso (5 min) |
| Frontend tests inexistentes | Alta | Alto | Priorizar tests_pass gate. Escribir tests smoke primero |
| Homologación de 65 connectors | Alta | Bajo | Los connectors son simples wrappers HTTP; priorizar lint+types mas no mutation |
| Devs resistentes al nuevo workflow | Media | Medio | Onboarding gradual. No bloquear commits hasta Fase 7 |

---

## 🔧 Dependencias Técnicas

### Python (instalar)
```bash
pip install ruff mypy radon mutmut pytest-cov pytest-mock pytest-asyncio
```

### TypeScript (instalar)
```bash
cd frontend && npm install && npm install -D @stryker-mutator/core @stryker-mutator/vitest-runner
```

### CI (configurar)
- GitHub Actions runner con Python 3.12 + Node 20
- Cache de pip y npm para acelerar gates

---

## ✅ Criterio de Finalización

El rollout de Code-Forge se considera COMPLETO cuando:

- [ ] **12/12 gates** ejecutándose y pasando en CI
- [ ] **12/12 módulos** homologados (todos pasan gates)
- [ ] **RunLedger** activo en cada cambio (pre-commit hook)
- [ ] **Sandbox** funcional en todos los gates
- [ ] **Memoria cross-session** poblada con ≥ 30 reflexiones
- [ ] **Dashboard de calidad** accesible vía `forge dashboard`
- [ ] **Score compuesto** ≥ 8.5/10
- [ ] **Documentación** completa (quickstart + workflow + ejemplos)
