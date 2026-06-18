# Zenic-Flujo — Fase 3: Arquitectura — Reporte Completo

**Fecha:** 2026-06-14
**Proyecto:** Zenic-Flujo
**Herramientas:** syke (grafo dependencias), sequential-thinking (razonamiento), expert-mcp (recomendaciones)

---

## 📋 Resumen Ejecutivo

| Métrica | Valor |
|---------|-------|
| Módulos principales | **25** |
| Archivos totales (src/) | **~350+** |
| Singletons detectados | **15+** |
| Puntos de entrada (entry points) | **3** (Flask web, CLI, FastAPI v2) |
| Archivos hub (alta centralidad) | **5** |
| Ciclos de dependencia | **1** (workflow ↔ orbital) |
| Deuda técnica arquitectónica | **ALTA** |
| Madurez de capas | **Media** (backend extenso, frontend parcial) |

---

## 1. 🏗️ GRAFO DE DEPENDENCIAS (syke)

### 1.1 Mapa de Módulos y sus Dependencias

```
                    ┌──────────────────────────────────────────────┐
                    │                   main.py                    │
                    │         (Punto de entrada principal)         │
                    └──────────┬───────────────────────┬───────────┘
                               │                       │
                    ┌──────────▼──────────┐  ┌─────────▼──────────┐
                    │    config.py        │  │   web/app.py       │
                    │  (Config global)    │  │  (Flask web)       │
                    └─────────────────────┘  └─────────┬──────────┘
                                                        │
              ┌─────────────────────────────────────────┼──────────────────────────┐
              │                                         │                          │
   ┌──────────▼──────────┐              ┌───────────────▼────────────┐  ┌─────────▼──────────┐
   │   api_v2/ (FastAPI) │              │  web/blueprints/ (Flask)   │  │     cli/ (Click)   │
   │  - workflows        │              │  - workflows, nlp, admin   │  │  - main.py         │
   │  - connectors       │              │  - compliance, orbital    │  │  - commands/       │
   │  - nlu, agents      │              │  - partnership, sync      │  │  - templates.py    │
   │  - bpmn, compliance │              │  - marketplace            │  │                    │
   │  - tenants, auth    │              └───────────┬───────────────┘  └────────────────────┘
   └──────┬──────────────┘                          │
          │                          ┌───────────────┼───────────────────────────┐
          │                          │               │                           │
          └──────────┬───────────────┘               │                           │
                     │                               │                           │
          ┌──────────▼───────────────────────────────▼───────────────────────────▼──────────┐
          │                                     ┌───────────┐                              │
          │                          ┌──────────┤ data/     │                              │
          │                          │          │ - DB      │                              │
          │                          │          │ - Redis   │                              │
          │                          │          │ - MongoDB │                              │
          │                          │          └───────────┘                              │
          │                                                                                │
          │   ┌────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
          │   │ orbital │  │ workflow │  │   nlu    │  │  agents  │  │  bpmn   │          │
          │   │ Engine  │  │  Engine  │  │ Pipeline │  │ Runtime  │  │ Parser   │          │
          │   └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  └──────────┘          │
          │        │              │             │             │                              │
          │        └──────────────┼─────────────┼─────────────┘                              │
          │                       │             │                                            │
          │              ┌────────▼─────────────▼──────────┐                                 │
          │              │         SDK / Connectors        │                                 │
          │              │  - registry.py                  │                                 │
          │              │  - auth.py, schema.py           │                                 │
          │              │  - base/connector.py            │                                 │
          │              └─────────────────────────────────┘                                 │
          │                                                                                  │
          │   ┌──────────┐  ┌────────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
          │   │ security │  │ compliance │  │  tenant  │  │ sync     │  │ mobile   │        │
          │   │ - RBAC   │  │ - SOC2     │  │ service  │  │ engine   │  │ - push   │        │
          │   │ - MFA    │  │ - GDPR     │  └──────────┘  └──────────┘  │ - sync   │        │
          │   │ - SSO    │  │ - HIPAA    │                              └──────────┘        │
          │   └──────────┘  └────────────┘                                                   │
          │                                                                                  │
          │   ┌──────────┐  ┌────────────┐  ┌──────────┐  ┌──────────────┐                  │
          │   │partner-  │  │marketplace │  │airgap.py │  │observability │                  │
          │   │ship/     │  │service/    │  │          │  │- telemetry   │                  │
          │   │service   │  │certif.     │  │          │  │- metrics     │                  │
          │   └──────────┘  └────────────┘  └──────────┘  └──────────────┘                  │
          └──────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Archivos HUB (Alta Centralidad / PageRank)

Estos son los archivos con MÁS dependencias entrantes ⬇️ (riesgo alto al modificar):

| # | Archivo | ⬇️ Dependientes | ⬆️ Dependencias | Rol |
|---|---------|:---------------:|:---------------:|-----|
| 1 | **`src/orbital/context.py`** (singleton) | 8+ | 5 | Centro del sistema ORBITAL |
| 2 | **`src/workflow/engine.py`** | 10+ | 10+ | Corazón del workflow |
| 3 | **`src/api_v2/app.py`** | 1 | 15+ | API moderna |
| 4 | **`src/sdk/registry.py`** (singleton) | 6+ | 3 | Registro de conectores |
| 5 | **`src/data/database_manager.py`** (singleton) | 15+ | 0 | DB unificada |

### 1.3 Archivos con Mayor Riesgo de Cambio (Más Dependencias Propias)

| # | Archivo | Dependencias internas | Riesgo |
|---|---------|:--------------------:|:------:|
| 1 | `src/workflow/engine.py` | 10+ submódulos | 🔴 Alto |
| 2 | `src/orbital/engine.py` | 5 pilares (OVC, TOR, RCC, COD, Espectro) | 🟡 Medio |
| 3 | `src/nlu/pipeline.py` | 15+ componentes NLU | 🟡 Medio |
| 4 | `src/api_v2/app.py` | 10 routers | 🟢 Bajo (middleware) |

### 1.4 Ciclos de Dependencia Detectados

```
🔄 CICLO DETECTADO: workflow ↔ orbital
   src/workflow/engine.py  ──importa──▶  src/orbital/context.py
   src/orbital/*.py         ──importa──▶  src/workflow/repository.py (vía orbital_repository)

Impacto: Bajo (dependencia lazy, solo en métodos específicos)
Recomendación: Mantener, es intencional (adaptación bidireccional)
```

---

## 2. 🧠 RAZONAMIENTO PROFUNDO SOBRE LA ARQUITECTURA

### 2.1 Patrón Arquitectónico General

El sistema usa una **arquitectura híbrida**:

- **★ Core**: **Monolito modular** con singletons compartidos (DatabaseManager, OrbitalContext, EventBus)
- **★ API**: **REST dual** (Flask para web SPA + FastAPI v2 para API pública)
- **★ Motor**: **Híbrido lineal-circular** (WorkflowEngine lineal + OrbitalEngine circular)
- **★ Frontend**: **SPA React** (parcialmente implementado)
- **★ Persistencia**: **SQLite** como base principal, con soporte Redis/MongoDB opcional

### 2.2 Fortalezas Arquitectónicas

✅ **Modularidad clara**: 25 módulos con responsabilidades bien definidas
✅ **Singletons controlados**: Patrón thread-safe con doble verificación en todos
✅ **Dual API**: Flask para web + FastAPI para API moderna (REST v2)
✅ **Circuit Breaker**: SDK tiene decoradores de circuit breaker y retry
✅ **Feature Flags**: AirGapConfig permite desactivar features en air-gapped
✅ **Inyección de dependencias**: api_v2/dependencies.py centraliza servicios
✅ **Lazy imports**: Muchas dependencias circulares resueltas con imports tardíos

### 2.3 Debilidades / Deuda Técnica Arquitectónica

⚠️ **ACOPLAMIENTO EXCESIVO**: `workflow/engine.py` depende de ~15 submódulos y es punto único de fallo
⚠️ **SINGLETONITIS**: 15+ singletons globales (DatabaseManager, OrbitalContext, EventBus, RedisService, SyncEngine, ComplianceManager, etc.)
⚠️ **Lazy imports generalizados**: Señal de que los ciclos de dependencia no están resueltos limpiamente
⚠️ **Flask ↔ FastAPI duplicación**: Lógica de autenticación y autorización duplicada entre Flask blueprints y FastAPI routers
⚠️ **Frontend incompleto**: De 22 módulos backend, solo 6 tienen UI en React
⚠️ **Single DB SQLite**: Sin separación de responsabilidades de datos (workflows, compliance, partners, marketplace todo en misma DB)
⚠️ **Error handling inconsistente**: Flask usa `try/except` en blueprints, FastAPI usa exception handlers globales
⚠️ **Observabilidad parcial**: OpenTelemetry configurado pero opcional (try/except ImportError)

### 2.4 Métricas de Salud Arquitectónica

| Dimensión | Puntaje (1-10) | Notas |
|-----------|:--------------:|-------|
| Cohesión de módulos | 7 | Mayoría bien definidos |
| Acoplamiento | 4 | Demasiados singletons globales |
| Testeabilidad | 5 | Reset singletons ayuda, pero acoplamiento global dificulta tests unitarios |
| Escalabilidad | 3 | SQLite single-node, sin sharding nativo |
| Mantenibilidad | 6 | Buena estructura de carpetas, pero archivos de 1000+ líneas |
| Seguridad por diseño | 5 | Fase 1 encontró varios issues |
| Observabilidad | 4 | Telemetría opcional, sin métricas de negocio |
| **TOTAL** | **5/10** | Madurez media con deuda técnica significativa |

### 2.5 Patrones de Diseño Identificados

| Patrón | Ubicación | Implementación |
|--------|-----------|---------------|
| **Singleton** | 15+ servicios | Thread-safe double-checked locking |
| **Adapter** | OrbitalAdapter | Traduce workflow steps ↔ variables orbitales |
| **Strategy** | SDK base/connector | Múltiples conectores con interfaz común |
| **Observer** | EventBus | Publicación/suscripción de eventos |
| **Factory** | SDK registry | ConnectorRegistry.create_connector() |
| **Chain of Responsibility** | NLU Pipeline | Pipeline multicapa con fallback |
| **Circuit Breaker** | SDK decorators | Retry con backoff exponencial |
| **State** | FSM en ClarifyDialog | 5 estados de diálogo |

---

## 3. 💼 RECOMENDACIONES DE ARQUITECTURA ENTERPRISE

### 3.1 🔴 CRÍTICO — Romper el Monolito de Singletons

**Problema**: 15+ singletons globales hacen imposible testear módulos de forma aislada.

**Solución**: Migrar a **inyección de dependencias real** con contenedor IoC.

```
┌─────────────────────────────────────────────────────┐
│ HOY:                   │  MAÑANA:                    │
│                         │                              │
│ DatabaseManager()       │  db = container.get(DB)      │
│   .get_instance()      │  engine = container.get(     │
│                         │    WorkflowEngine, db=db)    │
│ WorkflowEngine()        │                              │
│   .__init__()           │  def __init__(self,          │
│     db = DB.get_inst() │    db: DatabaseInterface):   │
│                         │    self._db = db             │
│ Singletons globales     │                              │
│ ocultos en __init__     │  Dependencias explícitas     │
└─────────────────────────────────────────────────────┘
```

**Esfuerzo**: Alto (refactor mayor)
**Impacto**: Muy alto
**Prioridad**: Post-MVP

### 3.2 🟡 ALTO — Separar Bases de Datos por Dominio

**Problema**: SQLite única contiene datos de workflows, compliance, partners, marketplace, tenants.

**Solución**: Bounded contexts con bases separadas:

```
HOY:                        MAÑANA:
workflow_determinista.db    workflow.db (SQLite)
↑                           compliance.db (SQLite)
 Todo junto                 marketplace.db (SQLite)
                            partners.db (SQLite)
                            + PostgreSQL opcional para tenants
```

**Esfuerzo**: Medio
**Impacto**: Alto (claridad, aislamiento, escalabilidad)

### 3.3 🟡 ALTO — Uniformar la Doble API (Flask + FastAPI)

**Problema**: Flask para SPA, FastAPI para API v2 → lógica duplicada.

**Solución a mediano plazo**: 
1. FasAPI v3 como API única
2. Flask SPA proxy a FastAPI
3. Middleware de autenticación unificado

**Corto plazo**: Compartir esquemas Pydantic entre Flask y FastAPI.

### 3.4 🟢 MEDIO — Reducir Archivos "God Class"

**Archivos >500 líneas identificados**:

| Archivo | Líneas | Problema |
|---------|:------:|----------|
| `src/tenant/service.py` | 1,080 | Tenant + todo |
| `src/security/encryption.py` | 846 | Cifrado + key management |
| `src/sdk/auth.py` | 835 | Auth + tokens + roles |
| `src/cli/templates.py` | 814 | Plantillas enormes |
| `src/nlu/guardrails.py` | 744 | Reglas + validación |

**Acción**: Extraer clases/módulos auxiliares de cada uno.

### 3.5 🟢 MEDIO — Completar Frontend React

**Estado actual**: 6/22 módulos backend cubiertos en frontend.
**Módulos faltantes**: login, admin, crm, inventory, invoice, chat, orbital, partners, compliance, reports, airgap.

### 3.6 🟢 MEDIO — Mejorar Observabilidad

- ✅ OpenTelemetry disponible (pero lazy)
- ❌ Sin métricas de negocio (workflows ejecutados, conectores usados)
- ❌ Sin dashboards preconfigurados
- ❌ Sin tracing distribuido real (solo FastAPI instrumentado)

### 3.7 ✅ FÁCIL — Renombrar y Estandarizar

- `api_v2/` → `api/` (v2 implícito en URL)
- Unificar logging: hay `src/utils/logger.py` + logging directo en módulos
- Estandarizar nombres de blueprints con API v2 routers

---

## 4. 📊 PLAN DE ACCIÓN PRIORIZADO

| Prioridad | Acción | Esfuerzo | Impacto | Dependencias |
|:---------:|--------|:--------:|:-------:|:------------:|
| 🔴 1 | IoC container / DI real | Alto | Muy alto | Post-Fase 1 |
| 🟡 2 | Separar DBs por dominio | Medio | Alto | Post-Fase 1 |
| 🟡 3 | Unificar API (compartir schemas) | Medio | Alto | — |
| 🟡 4 | Refactor god classes >500 lines | Medio | Medio | — |
| 🟡 5 | Frontend: completar 16 módulos | Muy alto | Alto | Post-Fase 1 |
| 🟢 6 | Agregar métricas de negocio | Bajo | Medio | — |
| 🟢 7 | Estandarizar nombrado | Bajo | Bajo | — |

---

## 5. 📈 RECOMENDACIONES TÉCNICAS CLAVE

### 5.1 Para el Sprint Actual

1. ✅ **Ejecutar Fase 2 (Seguridad)** primero (issues críticos de Fase 1)
2. ✅ **Fix `eval()` en memory.py** #1 prioridad
3. ✅ **Fix SQL injection** en 4 archivos
4. ✅ **Configurar CORS** desde env var

### 5.2 Para el Próximo Sprint

1. Implementar frontend de Login (Fase 0.1 del frontend)
2. Separar DB de compliance de la DB principal
3. Crear interfaz abstracta de DB para permitir PostgreSQL

### 5.3 Para Q3 2026

1. Contenedor IoC
2. FastAPI como API única
3. Frontend completo
4. Migración a PostgreSQL (opcional)

---

## 6. 📝 DIAGNÓSTICO FINAL

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   DIAGNÓSTICO ARQUITECTÓNICO: ZENIC-FLUJO                  │
│                                                             │
│   Fortaleza:   ████████░░░░  Modularidad  (8/10)           │
│   Fortaleza:   ████████░░░░  Patrones     (8/10)           │
│   Fortaleza:   ██████░░░░░░  Documentación (6/10)          │
│   Debilidad:   ██░░░░░░░░░░  Acoplamiento (2/10)           │
│   Debilidad:   ████░░░░░░░░  Testeabilidad (4/10)          │
│   Debilidad:   ████░░░░░░░░  Frontend     (3/10)           │
│                                                             │
│   ⭐ Overall:  5.2/10  —  "Madurez Media con deuda"        │
│                                                             │
│   Recomendación: Fix Fase 1 → Fase 2 → Refactor            │
│   arquitectura → Frontend → Observabilidad                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

*Documento generado automáticamente por análisis Fase 3 — Zenic-Flujo*
