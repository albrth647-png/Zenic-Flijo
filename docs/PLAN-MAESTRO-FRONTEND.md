# PLAN MAESTRO — Implementación Completa del Frontend (Zenic-Flujo)

> **Versión:** 1.0  
> **Backend:** Python Flask + FastAPI (api_v2)  
> **Frontend:** React 19 + TypeScript + Vite + Tailwind CSS v4 + Radix UI  
> **Objetivo:** Cobertura del 100% de los módulos del backend en el frontend React SPA

---

## 📋 RESUMEN EJECUTIVO

| Concepto | Cantidad |
|----------|----------|
| Módulos backend totales | **22** |
| Módulos frontend existentes | **6** (Dashboard, Editor, Workflows, Settings parcial, Plugins, Compliance, SyncCloud, Deployments) |
| Módulos frontend a implementar | **16** |
| Páginas React nuevas | **~12** |
| Componentes nuevos | **~40** |
| Archivos a crear | **~70** |
| Archivos a modificar | **~10** |

---

## 🏗️ ARQUITECTURA DEL FRONTEND (Estructura de Archivos)

```
frontend/src/
├── main.tsx                          # Entry point
├── App.tsx                           # Router principal
├── App.css
├── index.css                         # Tailwind + variables CSS
├── lib/
│   └── utils.ts                      # cn() helper
│
├── types/
│   ├── workflow.ts                   # ✅ Existente
│   ├── auth.ts                       # 🔴 NUEVO
│   ├── compliance.ts                 # 🔴 NUEVO (GDPR, HIPAA, SOC2)
│   ├── admin.ts                      # 🔴 NUEVO (users, queue, dead-letter)
│   ├── crm.ts                        # 🔴 NUEVO (leads)
│   ├── inventory.ts                  # 🔴 NUEVO (products)
│   ├── invoice.ts                    # 🔴 NUEVO (invoices)
│   ├── orbital.ts                    # 🔴 NUEVO (ORBITAL types)
│   ├── partners.ts                   # 🔴 NUEVO (partnership)
│   ├── airgap.ts                     # 🔴 NUEVO (air-gapped)
│   ├── license.ts                    # 🔴 NUEVO (license)
│   ├── sync.ts                       # 🔴 NUEVO (sync cloud)
│   └── reports.ts                    # 🔴 NUEVO (reports)
│
├── hooks/
│   ├── useApi.ts                     # ✅ Existente (mejorar)
│   ├── useSSE.ts                     # ✅ Existente
│   ├── useAuth.ts                    # 🔴 NUEVO (login/logout/session)
│   ├── useToast.ts                   # 🔴 NUEVO (toast system)
│   ├── useConfirm.ts                 # 🔴 NUEVO (confirm dialogs)
│   └── usePagination.ts             # 🔴 NUEVO (paginación)
│
├── contexts/
│   ├── AuthContext.tsx                # 🔴 NUEVO (estado de auth global)
│   └── ThemeContext.tsx               # 🔴 NUEVO (tema oscuro/claro)
│
├── components/
│   ├── ui/                           # ✅ Existente (shadcn-style)
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── badge.tsx
│   │   ├── dialog.tsx
│   │   ├── input.tsx
│   │   ├── label.tsx
│   │   ├── separator.tsx
│   │   ├── scroll-area.tsx
│   │   ├── toast.tsx
│   │   ├── select.tsx                # 🔴 NUEVO (dropdown select)
│   │   ├── table.tsx                 # 🔴 NUEVO (data table)
│   │   ├── tabs.tsx                  # 🔴 NUEVO (tab navigation)
│   │   ├── switch.tsx                # 🔴 NUEVO (toggle switch)
│   │   ├── checkbox.tsx              # 🔴 NUEVO (checkbox)
│   │   ├── dropdown-menu.tsx         # 🔴 NUEVO (dropdown menu)
│   │   ├── tooltip.tsx               # 🔴 NUEVO (tooltip)
│   │   ├── popover.tsx               # 🔴 NUEVO (popover)
│   │   ├── skeleton.tsx              # 🔴 NUEVO (skeleton loading)
│   │   ├── progress.tsx              # 🔴 NUEVO (progress bar)
│   │   ├── pagination.tsx            # 🔴 NUEVO (pagination)
│   │   └── empty-state.tsx           # 🔴 NUEVO (empty state)
│   │
│   ├── AppLayout.tsx                  # ✅ Existente (mejorar con auth)
│   ├── StatusBadge.tsx                # ✅ Existente
│   ├── ProtectedRoute.tsx            # 🔴 NUEVO (ruta protegida)
│   ├── DataTable.tsx                 # 🔴 NUEVO (tabla genérica)
│   ├── PageHeader.tsx                # 🔴 NUEVO (header de página)
│   ├── StatsCard.tsx                 # 🔴 NUEVO (card de estadísticas)
│   └── ErrorBoundary.tsx             # 🔴 NUEVO (error boundary global)
│
│   ├── editor/                       # ✅ Existente
│   ├── dashboard/                    # ✅ Existente
│   ├── login/                        # 🔴 NUEVO
│   │   ├── LoginPage.tsx
│   │   └── LoginForm.tsx
│   ├── admin/                        # 🔴 NUEVO
│   │   ├── UsersTab.tsx
│   │   ├── DeadLetterTab.tsx
│   │   └── QueueTab.tsx
│   ├── crm/                          # 🔴 NUEVO
│   │   └── LeadList.tsx
│   ├── inventory/                    # 🔴 NUEVO
│   │   └── ProductList.tsx
│   ├── invoice/                      # 🔴 NUEVO
│   │   └── InvoiceList.tsx
│   ├── chat/                         # 🔴 NUEVO
│   │   ├── ChatInterface.tsx
│   │   ├── MessageBubble.tsx
│   │   └── WorkflowPreview.tsx
│   ├── orbital/                      # 🔴 NUEVO
│   │   ├── OrbitalViz.tsx
│   │   └── VariableCard.tsx
│   ├── partners/                     # 🔴 NUEVO
│   │   ├── PartnerList.tsx
│   │   └── PartnerForm.tsx
│   ├── compliance/                   # 🔴 NUEVO
│   │   ├── soc2/                     # SOC 2 Type II
│   │   ├── gdpr/                     # GDPR
│   │   └── hipaa/                    # HIPAA
│   └── reports/                      # 🔴 NUEVO
│       └── ReportExport.tsx
│
└── pages/
    ├── Dashboard.tsx                  # ✅ Existente
    ├── Editor.tsx                     # ✅ Existente
    ├── Workflows.tsx                  # ✅ Existente
    ├── Settings.tsx                   # ✅ Existente (EXPANDIR)
    ├── Plugins.tsx                    # ✅ Existente
    ├── Compliance.tsx                 # ✅ Existente (EXPANDIR)
    ├── SyncCloud.tsx                  # ✅ Existente
    ├── Deployments.tsx                # ✅ Existente
    ├── LoginPage.tsx                  # 🔴 NUEVO
    ├── ChatPage.tsx                   # 🔴 NUEVO
    ├── AdminPage.tsx                  # 🔴 NUEVO
    ├── CrmPage.tsx                    # 🔴 NUEVO
    ├── InventoryPage.tsx              # 🔴 NUEVO
    ├── InvoicePage.tsx                # 🔴 NUEVO
    ├── OrbitalPage.tsx                # 🔴 NUEVO
    ├── PartnersPage.tsx               # 🔴 NUEVO
    ├── AirgapPage.tsx                 # 🔴 NUEVO
    ├── ReportsPage.tsx                # 🔴 NUEVO
    └── NotFoundPage.tsx               # 🔴 NUEVO
```

---

## 📦 FASE 0: FUNDACIÓN Y ARQUITECTURA

### F0.1 — Sistema de Autenticación (AuthContext + Login)

**Endpoints backend:**
- `POST /api/auth/login` → `{ status, user, role }`
- `POST /api/auth/logout` → `{ status }`
- `GET /api/auth/status` → `{ authenticated }`

**Archivos a crear:**
```
frontend/src/
├── contexts/AuthContext.tsx
├── hooks/useAuth.ts
├── types/auth.ts
├── pages/LoginPage.tsx
├── components/ProtectedRoute.tsx
├── components/login/LoginForm.tsx
└── components/login/LoginPage.tsx
```

**Archivos a modificar:**
```
frontend/src/
├── main.tsx                    # Envolver con AuthProvider
├── App.tsx                     # Añadir ruta /login, ProtectedRoute
├── components/AppLayout.tsx    # Añadir user info + logout
├── hooks/useApi.ts             # Integrar con AuthContext
└── package.json                # (si se necesita algo)
```

**Criterios de aceptación:**
- [ ] Usuario puede iniciar sesión con username + password
- [ ] Usuario puede cerrar sesión
- [ ] Sesión persiste en localStorage/tokens
- [ ] Rutas protegidas redirigen a `/login`
- [ ] Botón de logout en el sidebar
- [ ] Indicador visual del rol del usuario
- [ ] Manejo de errores: credenciales inválidas, usuario bloqueado, rate limiting

---

### F0.2 — UI Components Faltantes

**Paquetes ya instalados** (verificar en `package.json`): `@radix-ui/react-select`, `@radix-ui/react-switch`, `@radix-ui/react-tabs`, `@radix-ui/react-checkbox`, `@radix-ui/react-dropdown-menu`, `@radix-ui/react-tooltip`, `@radix-ui/react-popover`

**Archivos a crear:**
```
frontend/src/components/ui/
├── select.tsx                  # Basado en @radix-ui/react-select
├── table.tsx                   # Tabla con sort y filtros
├── tabs.tsx                    # Basado en @radix-ui/react-tabs
├── switch.tsx                  # Basado en @radix-ui/react-switch
├── checkbox.tsx                # Basado en @radix-ui/react-checkbox
├── dropdown-menu.tsx          # Basado en @radix-ui/react-dropdown-menu
├── tooltip.tsx                 # Basado en @radix-ui/react-tooltip
├── popover.tsx                 # Basado en @radix-ui/react-popover
├── skeleton.tsx                # Skeleton loading
├── progress.tsx                # Progress bar
├── pagination.tsx              # Paginación
├── empty-state.tsx             # Empty state reutilizable
└── form-field.tsx              # Form field wrapper con label + error
```

---

## 📦 FASE 1: MÓDULOS CRÍTICOS (Prioridad 🔴)

### F1.1 — Settings Completo + WhatsApp + Password Change

**Endpoints backend:**
- `GET /api/settings` → settings actuales
- `PUT /api/settings` → actualizar settings
- `POST /api/settings/change-password` → cambiar contraseña
- `GET/POST /api/settings/api-key` → regenerar API key
- `GET /api/settings/whatsapp` → WhatsApp config
- `PUT /api/settings/whatsapp` → actualizar WhatsApp
- `POST /api/settings/whatsapp/test` → test WhatsApp
- `POST /api/settings/test-email` → test email

**Archivos a crear:**
```
frontend/src/
├── pages/Settings.tsx          # 🟡 EXPANDIR (más pestañas)
├── components/settings/
│   ├── SettingsSmtpTab.tsx     # SMTP config (existente, mejorar)
│   ├── SettingsWhatsAppTab.tsx # WhatsApp config
│   ├── SettingsPasswordTab.tsx # Cambiar contraseña
│   ├── SettingsApiKeyTab.tsx   # API Key management
│   └── SettingsSystemTab.tsx   # System info + backup
```

**Criterios de aceptación:**
- [ ] Settings con tabs (SMTP, WhatsApp, Password, API Key, Sistema)
- [ ] Cambiar contraseña con validación y confirmación
- [ ] WhatsApp: configurar token + phone_number_id + test
- [ ] Regenerar API Key con confirmación
- [ ] Test email con feedback visual
- [ ] Indicador de licencia + Free Tier info

---

### F1.2 — NLP Chat Interface

**Endpoints backend:**
- `POST /api/nlu/understand` → análisis semántico (3 modos)
- `POST /api/workflows/chat` → sugerencias de workflows
- `POST /api/nlu/ai-generate` → generación por IA (3 modos)

**Archivos a crear:**
```
frontend/src/
├── pages/ChatPage.tsx
├── components/chat/
│   ├── ChatInterface.tsx      # Chat conversacional
│   ├── MessageBubble.tsx       # Burbuja de mensaje
│   ├── ChatInput.tsx           # Input con sugerencias
│   ├── WorkflowPreview.tsx     # Preview del workflow generado
│   ├── ModeSelector.tsx        # Modo: analyze/compile/simulate
│   └── TemplateSuggestion.tsx  # Tarjeta de sugerencia
```

**Criterios de aceptación:**
- [ ] Chat conversacional con historial
- [ ] 3 modos: Analyze (analizar texto), Compile (compilar a workflow), Simulate (simular)
- [ ] Sugerencias de templates al escribir
- [ ] Preview visual del workflow generado
- [ ] Botón "Crear workflow" que abre el editor con el workflow cargado
- [ ] Indicador de confianza y modo de generación (determinista vs IA)
- [ ] Botón para regenerar con IA si falla el modo determinista

---

### F1.3 — Admin Panel (Usuarios, Dead Letter, Work Queue)

**Endpoints backend:**
- `GET/POST /api/users`, `PUT/DELETE /api/users/<id>` → CRUD usuarios
- `GET /api/dead-letter`, `/stats`, retry, discard, retry-all, discard-all
- `GET /api/queue/status`, `/workers`, `/enqueue`, `/cleanup`

**Archivos a crear:**
```
frontend/src/
├── pages/AdminPage.tsx
├── components/admin/
│   ├── AdminTabs.tsx           # Tab container
│   ├── UsersTab.tsx            # CRUD de usuarios
│   ├── UserForm.tsx            # Crear/editar usuario
│   ├── DeadLetterTab.tsx       # Dead Letter Queue
│   ├── DeadLetterEntry.tsx     # Una entrada de DLQ
│   ├── QueueTab.tsx            # Work Queue status
│   ├── WorkersTab.tsx          # Workers status
│   └── SystemTab.tsx           # System backup + logs
```

**Criterios de aceptación:**
- [ ] Lista de usuarios con roles (admin, editor, viewer)
- [ ] Crear, editar, desactivar usuarios
- [ ] Dead Letter Queue: listar, filtrar, retry individual/batch, discard
- [ ] Work Queue: items pendientes, workers activos
- [ ] Backup manual del sistema
- [ ] Audit logs con filtros
- [ ] Stats de la cola

---

## 📦 FASE 2: MÓDULOS DE NEGOCIO (Prioridad 🟠)

### F2.1 — CRM (Leads)

**Endpoints backend:**
- `GET /api/tools/crm/leads` → lista con filtros
- `POST /api/tools/crm/leads` → crear lead

**Archivos a crear:**
```
frontend/src/
├── pages/CrmPage.tsx
├── types/crm.ts
├── components/crm/
│   ├── LeadList.tsx            # Tabla de leads
│   ├── LeadForm.tsx            # Crear/editar lead
│   ├── LeadDetail.tsx          # Detalle de lead
│   ├── LeadFilters.tsx         # Filtros por stage
│   └── LeadStageBadge.tsx      # Badge de etapa
```

**Criterios de aceptación:**
- [ ] Tabla de leads con columnas: nombre, email, teléfono, empresa, stage, source
- [ ] Filtrar por stage (new, contacted, qualified, won, lost)
- [ ] Crear lead con formulario
- [ ] Mover lead entre stages (drag o botón)
- [ ] Búsqueda por texto
- [ ] Paginación

---

### F2.2 — Inventario (Products)

**Endpoints backend:**
- `GET /api/tools/inventory/products` → lista con filtro low_stock
- `POST /api/tools/inventory/products` → crear producto
- `POST /api/tools/inventory/stock-movement` → movimiento de stock
- `GET /api/tools/inventory/low-stock` → alertas

**Archivos a crear:**
```
frontend/src/
├── pages/InventoryPage.tsx
├── types/inventory.ts
├── components/inventory/
│   ├── ProductList.tsx         # Tabla de productos
│   ├── ProductForm.tsx         # Crear producto
│   ├── ProductDetail.tsx       # Detalle + movimientos
│   ├── StockMovementForm.tsx   # Ajuste de stock
│   ├── LowStockAlerts.tsx      # Alertas de stock bajo
│   └── ProductFilters.tsx      # Filtros
```

**Criterios de aceptación:**
- [ ] Tabla de productos con SKU, nombre, categoría, stock, precio
- [ ] Indicador visual de stock bajo (rojo/ámbar)
- [ ] Crear producto con formulario
- [ ] Ajuste de stock con tipo (entrada/salida/ajuste) y razón
- [ ] Sección de alertas de stock bajo
- [ ] Búsqueda y filtros

---

### F2.3 — Facturación (Invoices)

**Endpoints backend:**
- `POST /api/tools/invoice/create` → crear factura
- `GET /api/tools/invoice/list` → listar facturas

**Archivos a crear:**
```
frontend/src/
├── pages/InvoicePage.tsx
├── types/invoice.ts
├── components/invoice/
│   ├── InvoiceList.tsx         # Tabla de facturas
│   ├── InvoiceForm.tsx         # Crear factura
│   ├── InvoiceDetail.tsx       # Detalle de factura
│   ├── InvoiceFilters.tsx      # Filtros por estado
│   └── InvoiceStatusBadge.tsx  # Badge de estado
```

**Criterios de aceptación:**
- [ ] Lista de facturas con cliente, monto, fecha, estado
- [ ] Crear factura con items, impuesto, descuento
- [ ] Filtrar por estado (pending, paid, overdue, cancelled)
- [ ] Marcar como pagada
- [ ] Cálculo automático de totales

---

## 📦 FASE 3: MÓDULOS TÉCNICOS (Prioridad 🟡)

### F3.1 — ORBITAL Monitor

**Endpoints backend:**
- `GET /api/orbital/status` → estado completo
- `POST /api/orbital/tick` → ejecutar tick
- `POST /api/orbital/variable` → crear variable
- `DELETE /api/orbital/variable/<name>` → eliminar variable
- `POST /api/orbital/cycle` → crear ciclo
- `POST /api/orbital/reset` → reset

**Archivos a crear:**
```
frontend/src/
├── pages/OrbitalPage.tsx
├── types/orbital.ts
├── components/orbital/
│   ├── OrbitalStatusPanel.tsx  # Panel de estado general
│   ├── OrbitalVariables.tsx    # Lista de variables
│   ├── OrbitalVariableCard.tsx # Card de una variable
│   ├── OrbitalTorMatrix.tsx    # Visualización matriz TOR
│   ├── OrbitalRccPanel.tsx    # Resonancia RCC
│   ├── OrbitalCiclosList.tsx   # Lista de ciclos
│   ├── OrbitalEspectro.tsx     # Espectro orbital
│   ├── OrbitalControls.tsx     # Botones: tick, reset, crear
│   └── OrbitalHistory.tsx      # Historial de ticks
```

**Criterios de aceptación:**
- [ ] Dashboard con variables orbitales (theta, amplitud, velocidad, valor)
- [ ] Matriz TOR visual (tabla con colores por intensidad)
- [ ] Paneles RCC (ciclos resonantes vs no resonantes)
- [ ] Botón "Run Tick" que ejecuta y actualiza todo
- [ ] Crear/eliminar variables orbitales
- [ ] Crear ciclos orbitales
- [ ] Historial de ticks
- [ ] Reset del motor

---

### F3.2 — Compliance Avanzado (SOC 2, GDPR, HIPAA)

**Endpoints backend (SOC 2 Type II):**
- `GET/POST /api/compliance/typeii/periods` → periodos de monitoreo
- `POST /api/compliance/typeii/periods/<id>/bridge-letter` → bridge letter
- `GET /api/compliance/typeii/periods/<id>/tests` → test results
- `POST/DELETE /api/compliance/typeii/subservices` → subservicios

**Endpoints backend (GDPR):**
- `GET /api/compliance/gdpr/consents` → consentimientos
- `GET /api/compliance/gdpr/dsars` → DSARs
- `GET /api/compliance/gdpr/stats` → estadísticas

**Endpoints backend (HIPAA):**
- `GET /api/compliance/hipaa/baas` → BAAs
- `GET /api/compliance/hipaa/phi` → inventario PHI
- `GET /api/compliance/hipaa/stats` → estadísticas

**Endpoints adicionales:**
- `GET /api/compliance/policies` → políticas
- `GET /api/compliance/audit` → audit trail
- `GET /api/compliance/report` → reporte

**Archivos a crear:**
```
frontend/src/
├── types/compliance.ts         # 🟡 EXPANDIR con tipos GDPR/HIPAA/SOC2
├── pages/Compliance.tsx        # 🟡 EXPANDIR con tabs
├── components/compliance/
│   ├── soc2/
│   │   ├── Soc2PeriodsList.tsx       # Lista de periodos
│   │   ├── Soc2PeriodForm.tsx        # Crear periodo
│   │   ├── Soc2Subservices.tsx       # Subservicios
│   │   ├── Soc2BridgeLetter.tsx      # Bridge letter
│   │   └── Soc2TestResults.tsx       # Resultados de tests
│   ├── gdpr/
│   │   ├── GdprConsents.tsx          # Consentimientos
│   │   ├── GdprDsars.tsx             # DSARs
│   │   └── GdprStats.tsx             # Estadísticas
│   ├── hipaa/
│   │   ├── HipaaBaas.tsx             # BAAs
│   │   ├── HipaaPhiInventory.tsx     # Inventario PHI
│   │   └── HipaaStats.tsx            # Estadísticas
│   └── compliance-common/
│       ├── PoliciesList.tsx          # Políticas
│       └── AuditTrail.tsx            # Audit trail
├── components/reports/
│   └── ComplianceReport.tsx          # Reporte descargable
```

---

## 📦 FASE 4: MÓDULOS DE INTEGRACIÓN (Prioridad 🟢)

### F4.1 — Partnership Program

**Endpoints backend:**
- `GET /api/partners/overview` → lista + stats
- `POST /api/partners/register` → registrar partner
- `POST /api/partners/<id>/approve` → aprobar
- `POST /api/partners/<id>/promote` → promocionar tier
- `GET /api/partners/tiers` → definiciones de tiers
- `GET/POST /api/partners/benefits` → beneficios
- `POST /api/partners/benefits/<id>/revoke` → revocar beneficio
- `GET /api/partners/activity` → timeline

**Archivos a crear:**
```
frontend/src/
├── pages/PartnersPage.tsx
├── types/partners.ts
├── components/partners/
│   ├── PartnerList.tsx         # Lista con tiers y badges
│   ├── PartnerForm.tsx         # Registro de partner
│   ├── PartnerDetail.tsx       # Detalle + stats
│   ├── PartnerTiersCards.tsx   # Cards de tiers (Community→Platinum)
│   ├── PartnerApproval.tsx     # Aprobación + promoción
│   ├── PartnerBenefits.tsx     # Beneficios por partner
│   └── PartnerActivity.tsx     # Timeline de actividad
```

---

### F4.2 — Air-Gapped Mode

**Endpoints backend:**
- `GET /api/airgap/status` → estado de validación
- `GET /api/airgap/config` → configuración
- `POST /api/airgap/license` → crear licencia offline
- `POST /api/airgap/license/verify` → verificar licencia

**Archivos a crear:**
```
frontend/src/
├── pages/AirgapPage.tsx
├── types/airgap.ts
├── components/airgap/
│   ├── AirgapStatus.tsx       # Checks de validación
│   ├── AirgapConfig.tsx       # Configuración
│   ├── AirgapLicenseForm.tsx  # Crear licencia offline
│   └── AirgapVerifyForm.tsx   # Verificar licencia
```

---

### F4.3 — License Management

**Endpoints backend:**
- `POST /api/license/validate` → validar clave
- `GET /api/license/info` → info de licencia + Free Tier

**Archivos a crear:**
```frontend/src/
├── pages/Settings.tsx         # 🟡 Añadir tab de Licencia
├── components/settings/
│   └── SettingsLicenseTab.tsx # Info de licencia + validar clave
```

---

### F4.4 — Reports (CSV/PDF Export)

**Endpoints backend:**
- `GET /api/reports/workflows/<fmt>` → exportar workflows
- `GET /api/reports/crm/<fmt>` → exportar CRM
- `GET /api/reports/inventory/<fmt>` → exportar inventario
- `GET /api/reports/invoices/<fmt>` → exportar facturas

**Archivos a crear:**
```
frontend/src/
├── pages/ReportsPage.tsx
├── components/reports/
│   ├── ReportCard.tsx         # Card de un tipo de reporte
│   └── ReportExport.tsx       # Botón de exportación
```

---

### F4.5 — System Admin (Backup, Logs, Status)

**Endpoints backend:**
- `POST /api/system/backup` → backup manual
- `GET /api/system/logs` → audit logs
- `GET /api/system/status` → estado del sistema

**Archivos a crear:**
```
frontend/src/
├── pages/AdminPage.tsx        # 🟡 Añadir SystemTab
├── components/admin/
│   └── SystemTab.tsx          # Backup, logs, status
```

---

## 📦 FASE 5: MEJORAS TRANSVERSALES

### F5.1 — Mejoras Globales

**Archivos a modificar:**
```
frontend/src/
├── App.tsx
│   ├── 🟡 Agregar: ErrorBoundary global
│   ├── 🟡 Agregar: Ruta /login (sin ProtectedRoute)
│   └── 🟡 Agregar: Ruta 404
│
├── components/AppLayout.tsx
│   ├── 🟡 Agregar: User info + avatar + logout en sidebar
│   ├── 🟡 Agregar: Indicador de licencia (trial/active)
│   ├── 🟡 Agregar: Links a nuevas páginas en navegación
│   └── 🟡 Agregar: Switch dark/light mode
│
├── hooks/useApi.ts
│   ├── 🟡 Mejorar: Integrar con AuthContext
│   ├── 🟡 Mejorar: Refresh automático en 401
│   └── 🟡 Mejorar: Tipado genérico
│
├── index.css
│   └── 🟡 Agregar: Animaciones para skeleton, transitions
│
└── package.json
    └── Verificar paquetes instalados (Radix UI, etc.)
```

### F5.2 — Estado Global con Context API

**Contextos a crear:**
```
frontend/src/contexts/
├── AuthContext.tsx     # Auth state (user, role, token, login/logout)
└── ThemeContext.tsx    # Dark/light mode
```

---

## 📊 CRONOGRAMA DE IMPLEMENTACIÓN

| Fase | Semana | Módulos | Archivos | Dependencias |
|------|--------|---------|----------|--------------|
| **F0** | Semana 1 | Auth + UI Components | ~18 | Ninguna |
| **F1.1** | Semana 2 | Settings Completo | ~6 | F0 |
| **F1.2** | Semana 2-3 | NLP Chat | ~7 | F0 |
| **F1.3** | Semana 3-4 | Admin Panel | ~8 | F0 |
| **F2.1** | Semana 4 | CRM | ~7 | F0 |
| **F2.2** | Semana 5 | Inventario | ~8 | F0 |
| **F2.3** | Semana 5 | Facturación | ~7 | F0 |
| **F3.1** | Semana 6 | ORBITAL | ~10 | F0 |
| **F3.2** | Semana 6-7 | Compliance Avanzado | ~12 | F0 |
| **F4.1** | Semana 7 | Partners | ~8 | F0 |
| **F4.2** | Semana 7 | AirGap | ~5 | F0 |
| **F4.3** | Semana 8 | Licencias | ~2 | F0 |
| **F4.4** | Semana 8 | Reportes | ~3 | F2.1, F2.2, F2.3 |
| **F4.5** | Semana 8 | System Admin | ~2 | F0 |
| **F5** | Semana 8-9 | Mejoras Globales | ~5 | Todas |

**Total estimado:** ~8-9 semanas de trabajo continuo

---

## 🔌 API ENDPOINTS — MAPA COMPLETO BACKEND → FRONTEND

```
AUTH (3 endpoints)
  └── POST /api/auth/login          → 🔴 F0.1 LoginPage
  └── POST /api/auth/logout         → 🔴 F0.1 LoginPage
  └── GET  /api/auth/status         → 🔴 F0.1 AuthContext

DASHBOARD (2 endpoints) ✅
  └── GET  /api/dashboard/stats      → ✅ Dashboard
  └── GET  /api/dashboard/timeline   → ✅ Dashboard

WORKFLOWS (10 endpoints) ✅
  └── GET/POST /api/workflows            → ✅ Workflows + Editor
  └── GET/PUT/DELETE /api/workflows/<id> → ✅ Editor
  └── POST /api/workflows/<id>/activate  → ✅ Workflows
  └── POST /api/workflows/<id>/pause     → ✅ Workflows
  └── GET  /api/workflows/<id>/history   → 🔴 F1.3 WorkflowDetail
  └── GET  /api/workflows/<id>/export    → 🟡 Añadir a Editor
  └── POST /api/workflows/import         → 🟡 Añadir a Editor
  └── POST /api/workflows/<id>/retry     → ✅ Editor

NLP CHAT (3 endpoints)
  └── POST /api/nlu/understand      → 🔴 F1.2 ChatPage
  └── POST /api/workflows/chat      → 🔴 F1.2 ChatPage
  └── POST /api/nlu/ai-generate     → 🔴 F1.2 ChatPage

CRM (2 endpoints)
  └── GET/POST /api/tools/crm/leads → 🟠 F2.1 CrmPage

INVENTORY (4 endpoints)
  └── GET/POST /api/tools/inventory/products      → 🟠 F2.2 InventoryPage
  └── POST /api/tools/inventory/stock-movement     → 🟠 F2.2 InventoryPage
  └── GET  /api/tools/inventory/low-stock          → 🟠 F2.2 InventoryPage

INVOICE (2 endpoints)
  └── POST /api/tools/invoice/create → 🟠 F2.3 InvoicePage
  └── GET  /api/tools/invoice/list   → 🟠 F2.3 InvoicePage

SETTINGS (8 endpoints)
  └── GET/PUT /api/settings              → 🟡 Settings (SMTP) ✅ → 🔴 F1.1 Expandir
  └── GET/POST /api/settings/api-key     → 🔴 F1.1 Settings
  └── POST /api/settings/change-password → 🔴 F1.1 Settings
  └── POST /api/settings/test-email      → 🔴 F1.1 Settings
  └── GET/PUT /api/settings/whatsapp     → 🔴 F1.1 Settings
  └── POST /api/settings/whatsapp/test   → 🔴 F1.1 Settings

USERS / ADMIN (10+ endpoints)
  └── GET/POST /api/users                   → 🔴 F1.3 Admin
  └── PUT/DELETE /api/users/<id>            → 🔴 F1.3 Admin
  └── GET  /api/dead-letter + /stats        → 🔴 F1.3 Admin
  └── POST /api/dead-letter/<id>/retry      → 🔴 F1.3 Admin
  └── POST /api/dead-letter/<id>/discard    → 🔴 F1.3 Admin
  └── POST /api/dead-letter/retry-all       → 🔴 F1.3 Admin
  └── POST /api/dead-letter/discard-all     → 🔴 F1.3 Admin
  └── GET  /api/queue/status, /workers      → 🔴 F1.3 Admin
  └── POST /api/queue/enqueue, /cleanup     → 🔴 F1.3 Admin

MARKETPLACE (5 endpoints) ✅
  └── GET  /api/marketplace/connectors      → ✅ Plugins
  └── GET  /api/marketplace/categories      → ✅ Plugins
  └── POST /api/marketplace/connectors/install/uninstall → ✅ Plugins
  └── GET  /api/marketplace/stats           → 🟡 Mejorar Plugins

COMPLIANCE (15+ endpoints)
  └── GET  /api/compliance/overview          → ✅ Compliance
  └── GET  /api/compliance/controls          → ✅ Compliance
  └── PUT  /api/compliance/controls/<id>/status → 🟡 Añadir a Compliance
  └── GET  /api/compliance/audit             → 🟡 F3.2 Compliance
  └── GET  /api/compliance/report            → 🟡 F3.2 Compliance
  └── GET  /api/compliance/policies          → 🟡 F3.2 Compliance
  └── GET/POST /api/compliance/typeii/*      → 🟡 F3.2 SOC2
  └── GET  /api/compliance/gdpr/*            → 🟡 F3.2 GDPR
  └── GET  /api/compliance/hipaa/*           → 🟡 F3.2 HIPAA

SYNC CLOUD (8+ endpoints) ✅
  └── GET/PUT /api/sync/config              → ✅ SyncCloud
  └── POST /api/sync/key/generate           → ✅ SyncCloud
  └── POST /api/sync/export, /push          → ✅ SyncCloud
  └── GET  /api/sync/history, /stats        → ✅ SyncCloud

ORBITAL (5 endpoints)
  └── GET  /api/orbital/status               → 🟡 F3.1 OrbitalPage
  └── POST /api/orbital/tick                 → 🟡 F3.1 OrbitalPage
  └── POST /api/orbital/variable             → 🟡 F3.1 OrbitalPage
  └── DELETE /api/orbital/variable/<name>    → 🟡 F3.1 OrbitalPage
  └── POST /api/orbital/cycle                → 🟡 F3.1 OrbitalPage
  └── POST /api/orbital/reset                → 🟡 F3.1 OrbitalPage

PARTNERSHIP (8+ endpoints)
  └── GET  /api/partners/overview            → 🟢 F4.1 PartnersPage
  └── POST /api/partners/register            → 🟢 F4.1 PartnersPage
  └── POST /api/partners/<id>/approve        → 🟢 F4.1 PartnersPage
  └── POST /api/partners/<id>/promote        → 🟢 F4.1 PartnersPage
  └── GET  /api/partners/tiers               → 🟢 F4.1 PartnersPage
  └── GET/POST /api/partners/benefits        → 🟢 F4.1 PartnersPage
  └── GET  /api/partners/activity            → 🟢 F4.1 PartnersPage

AIR-GAP (4 endpoints)
  └── GET  /api/airgap/status                → 🟢 F4.2 AirgapPage
  └── GET  /api/airgap/config                → 🟢 F4.2 AirgapPage
  └── POST /api/airgap/license               → 🟢 F4.2 AirgapPage
  └── POST /api/airgap/license/verify        → 🟢 F4.2 AirgapPage

LICENSE (2 endpoints)
  └── POST /api/license/validate             → 🟢 F4.3 Settings
  └── GET  /api/license/info                 → 🟢 F4.3 Settings

REPORTS (4 endpoints)
  └── GET  /api/reports/workflows/<fmt>      → 🟢 F4.4 ReportsPage
  └── GET  /api/reports/crm/<fmt>            → 🟢 F4.4 ReportsPage
  └── GET  /api/reports/inventory/<fmt>      → 🟢 F4.4 ReportsPage
  └── GET  /api/reports/invoices/<fmt>       → 🟢 F4.4 ReportsPage

SYSTEM (3 endpoints)
  └── POST /api/system/backup                → 🟢 F4.5 Admin
  └── GET  /api/system/logs                  → 🟢 F4.5 Admin
  └── GET  /api/system/status                → 🟢 F4.5 Admin
```

---

## 🎯 TOTAL DE ARCHIVOS A CREAR

| Tipo | Cantidad |
|------|----------|
| **Páginas nuevas** | **12** |
| **Types nuevos** | **9** |
| **Hooks nuevos** | **3** |
| **Contextos nuevos** | **2** |
| **Componentes UI nuevos** | **12** |
| **Componentes de negocio nuevos** | **~45** |
| **Archivos a modificar** | **~10** |
| **Total** | **~93 archivos** |

---

## ⚙️ ROUTER — NUEVAS RUTAS

```typescript
// App.tsx — Nuevo router
<Route path="/app" element={<ProtectedRoute><AppLayout /></ProtectedRoute>}>
  <Route index element={<Navigate to="/app/dashboard" replace />} />
  <Route path="dashboard"    element={<Dashboard />} />         // ✅
  <Route path="editor"       element={<Editor />} />            // ✅
  <Route path="workflows"    element={<Workflows />} />         // ✅
  <Route path="chat"         element={<ChatPage />} />          // 🔴 NUEVO
  <Route path="crm"          element={<CrmPage />} />           // 🟠 NUEVO
  <Route path="inventory"    element={<InventoryPage />} />     // 🟠 NUEVO
  <Route path="invoices"     element={<InvoicePage />} />       // 🟠 NUEVO
  <Route path="admin"        element={<AdminPage />} />         // 🔴 NUEVO
  <Route path="plugins"      element={<Plugins />} />           // ✅
  <Route path="compliance"   element={<Compliance />} />        // ✅ ← Expandir
  <Route path="orbital"      element={<OrbitalPage />} />       // 🟡 NUEVO
  <Route path="partners"     element={<PartnersPage />} />      // 🟢 NUEVO
  <Route path="airgap"       element={<AirgapPage />} />        // 🟢 NUEVO
  <Route path="reports"      element={<ReportsPage />} />       // 🟢 NUEVO
  <Route path="sync"         element={<SyncCloud />} />         // ✅
  <Route path="deploy"       element={<Deployments />} />       // ✅
  <Route path="settings"     element={<Settings />} />          // ✅ ← Expandir
</Route>
<Route path="/login" element={<LoginPage />} />                 // 🔴 NUEVO
<Route path="*" element={<NotFoundPage />} />                   // 🔴 NUEVO
```

---

## 📋 CHECKLIST DE VERIFICACIÓN POR FASE

### Fase 0 — Fundación
- [ ] Login funciona: POST /api/auth/login → session
- [ ] Logout funciona: POST /api/auth/logout → redirect
- [ ] AuthContext persiste sesión
- [ ] ProtectedRoute redirige a /login
- [ ] Sidebar muestra user info + logout
- [ ] Componentes UI nuevos funcionan (select, table, tabs, etc.)

### Fase 1 — Críticos
- [ ] Settings completo: tabs SMTP + WhatsApp + Password + API Key + Sistema
- [ ] Chat NLU: analyze, compile, simulate modes
- [ ] Admin: CRUD usuarios + Dead Letter Queue + Work Queue
- [ ] Todas las pruebas de los 3 módulos pasan

### Fase 2 — Negocio
- [ ] CRM: listar, crear, filtrar leads
- [ ] Inventario: listar, crear, ajustar stock, alertas
- [ ] Facturación: listar, crear, filtrar facturas
- [ ] Todas las pruebas pasan

### Fase 3 — Técnicos
- [ ] ORBITAL: status, tick, variables, ciclos, reset
- [ ] Compliance avanzado: SOC2, GDPR, HIPAA tabs
- [ ] Todas las pruebas pasan

### Fase 4 — Integración
- [ ] Partners: listar, registrar, aprobar, promocionar
- [ ] AirGap: status, config, licencias offline
- [ ] Licencias: validar, info
- [ ] Reportes: export CSV/PDF
- [ ] System: backup, logs, status
- [ ] Todas las pruebas pasan

### Fase 5 — Mejoras
- [ ] ErrorBoundary global
- [ ] NotFoundPage
- [ ] Dark/light mode toggle
- [ ] useApi mejorado con tipos
- [ ] Build sin errores
- [ ] TypeScript typecheck pasa

---

## 🚩 RIESGOS Y MITIGACIONES

| Riesgo | Impacto | Probabilidad | Mitigación |
|--------|---------|--------------|------------|
| Backend no tiene CORS configurado | 🔴 Alto | Media | Configurar Flask-CORS en el backend |
| Session vs Token auth | 🔴 Alto | Baja | Backend usa Flask sessions; adaptar frontend |
| Tipos TypeScript incorrectos | 🟡 Medio | Media | Usar contratos de API, probar con datos reales |
| Paginación no soportada en backend | 🟡 Medio | Alta | Implementar paginación client-side |
| Rutas de API v2 (FastAPI) no documentadas | 🟡 Medio | Media | Revisar src/api_v2/routers/ |
| Componentes muy grandes (>200 líneas) | 🟡 Medio | Media | Dividir en subcomponentes pequeños |

---

## 📌 NOTAS TÉCNICAS

1. **Todos los componentes UI nuevos siguen el patrón shadcn/ui** (Radix primitives + class-variance-authority + cn())
2. **Cada página sigue el patrón:** Container (data fetching) → State (loading/empty/error/success) → Presentational components
3. **SSE (Server-Sent Events):** El hook `useSSE.ts` ya existe y funciona — reutilizarlo para actualizaciones en vivo
4. **Navegación:** Los items del NAV_ITEMS en AppLayout.tsx deben actualizarse para incluir las nuevas rutas
5. **i18n:** El backend tiene español/inglés. El frontend solo español. Considerar añadir i18n en Fase 5.
6. **Testing:** Considerar añadir tests con Vitest + React Testing Library después de la implementación
