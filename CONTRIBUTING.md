# Contribuyendo a Zenic-Flijo

¡Gracias por tu interés en contribuir a Zenic-Flijo! Este documento establece las guías y mejores prácticas para contribuir al proyecto.

## 📋 Índice

- [Código de Conducta](#código-de-conducta)
- [¿Cómo puedo contribuir?](#cómo-puedo-contribuir)
- [Desarrollo Local](#desarrollo-local)
- [Estándares de Código](#estándares-de-código)
- [Proceso de PR](#proceso-de-pr)
- [Estructura del Proyecto](#estructura-del-proyecto)

## Código de Conducta

Este proyecto se rige por un [Código de Conducta](CODE_OF_CONDUCT.md). Al participar, se espera que mantengas este código. Por favor, reporta comportamientos inaceptables a dev@zenic-flujo.io.

## ¿Cómo puedo contribuir?

### 🐛 Reportar Bugs

1. **Verifica que el bug no haya sido reportado** — revisa los [issues existentes](https://github.com/albrth647-png/Zenic-Flijo/issues)
2. **Usa la plantilla de bug report** — incluye:
   - Versión del software
   - Sistema operativo y versión de Python
   - Pasos para reproducir
   - Comportamiento esperado vs actual
   - Logs relevantes

### 💡 Sugerir Features

1. **Abre un discussion** primero para validar la idea
2. **Describe el problema** que resuelve, no solo la solución propuesta
3. **Incluye ejemplos** de uso si es posible

### 🚀 Enviar Código

1. **Fork** el repositorio
2. **Crea una rama** con nombre descriptivo:
   - `feat/nombre-corto` — nuevas funcionalidades
   - `fix/nombre-corto` — correcciones de bugs
   - `docs/nombre-corto` — documentación
   - `refactor/nombre-corto` — refactorización
3. **Desarrolla** siguiendo los estándares abajo
4. **Abre un Pull Request**

## Desarrollo Local

### Requisitos

```bash
# Python 3.12+
python --version

# Node.js 18+ (solo para frontend)
node --version

# Docker (opcional, para servicios externos)
docker --version
```

### Setup

```bash
# 1. Clonar el repositorio
git clone https://github.com/albrth647-png/Zenic-Flijo.git
cd Zenic-Flijo

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Iniciar servicios (PostgreSQL, Redis)
docker compose up -d postgres redis

# 5. Configurar variables de entorno
cp .env.example .env
# Editar .env con tu configuración local

# 6. Iniciar servidor de desarrollo
python src/main.py
```

### Frontend (React SPA)

```bash
cd frontend
npm install
npm run dev  # Puerto 5173, proxy a Flask en 5000
npm run build  # Build a src/web/static/spa/
```

### Tests

```bash
# Tests Python
python -m pytest src/tests/ -v

# Tests específicos
python -m pytest src/tests/test_engine.py -v
python -m pytest src/tests/test_orbital.py -v

# Lint
ruff check src/ --fix
ruff format src/ --check

# Type check
mypy src/ --ignore-missing-imports
```

## Estándares de Código

### Python

- **Python 3.12+** — usar type hints en todo el código
- **Ruff** — seguir las reglas definidas en `ruff.toml`
- **Formato**: `ruff format src/`
- **Docstrings**: Google style
- **Nombres**:
  - `snake_case` para variables y funciones
  - `PascalCase` para clases
  - `UPPER_CASE` para constantes
  - `_privado` para miembros privados

### TypeScript / React

- **TypeScript strict mode**
- **shadcn/ui** para componentes de UI
- **React Query** para fetching de datos
- **Zustand** para estado global (cuando sea necesario)
- **Tailwind CSS** para estilos (nunca CSS modules)

### Commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add workflow export endpoint
fix: correct rate limiting for login attempts
docs: update deployment guide
refactor: extract sync engine from app.py
test: add unit tests for ComplianceManager
chore: update dependencies
```

## Proceso de PR

### Checklist del PR

- [ ] El código pasa `ruff check` y `ruff format`
- [ ] El código pasa `mypy` (Python) o TypeScript compiler
- [ ] Los tests pasan (`python -m pytest`)
- [ ] Se agregaron tests para nueva funcionalidad
- [ ] La documentación fue actualizada
- [ ] El PR tiene un título descriptivo siguiendo Conventional Commits
- [ ] El PR no excede las 400 líneas de cambios

### Revisión

1. **Auto-revisión**: Revisa tu propio código antes de pedir review
2. **Solicita review**: Asigna al menos un reviewer
3. **Responde**: Atiende los comentarios de manera constructiva
4. **Merge**: Un maintainer aprobará y hará merge

### CI/CD

El pipeline de CI ejecuta:

1. `ruff check` — lint
2. `ruff format --check` — formato
3. `mypy src/` — type checking
4. `python -m pytest` — tests
5. `npm run build` — build frontend

Todos deben pasar antes del merge.

## Estructura del Proyecto

```
src/
├── cli/           # CLI interactiva
├── compliance/    # SOC 2, GDPR, HIPAA
├── connectors/    # 35 conectores pre-construidos
├── data/          # Database manager, backup
├── events/        # Event bus, work queue, workers
├── license/       # Validación de licencias
├── marketplace/   # Marketplace de conectores
├── mobile/        # API mobile + sync offline
├── nlu/           # NLP pipeline (intents, entidades, slots)
├── observability/ # Métricas, tracing, telemetría
├── orbital/       # Motor orbital determinista
├── sdk/           # SDK para conectores
├── security/      # RBAC, MFA, SSO, encryption
├── sync/          # Sync Cloud E2E
├── tenant/        # Multi-tenant
├── tools/         # CRM, inventario, facturas
├── web/           # Flask app, API REST
├── workflow/      # Engine, steps, dead letter
└── main.py        # Entry point
```

## ¿Dudas?

Abre un [discussion](https://github.com/albrth647-png/Zenic-Flijo/discussions) o envía un email a dev@zenic-flujo.io.

---

¡Gracias por contribuir a Zenic-Flijo! 🎉
