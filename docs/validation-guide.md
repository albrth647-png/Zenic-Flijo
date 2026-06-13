# ORBITAL v3.2 — Guía de Validación Independiente

## Objetivo

Verificar que el motor ORBITAL cumple sus garantías de convergencia determinista.
Esta guía está pensada para que un revisor externo —sin conocimiento previo del código—
pueda confirmar que el sistema hace lo que dice: converger a un punto fijo de forma
determinista, 100% offline, sin depender de servicios externos.

## Prerrequisitos

```bash
git clone <repo>
cd zenic-flujo
pip install -r requirements.txt
```

Tiempo estimado total: ~5 minutos.

---

## Validación 1: Determinismo (Mismas entradas → mismo resultado)

**¿Qué prueba?** Que dadas las mismas condiciones iniciales, el motor siempre produce
el mismo estado final. Si el sistema usara aleatoriedad oculta, dos ejecuciones
idénticas darían resultados diferentes.

```python
from src.orbital.engine import OrbitalEngine

# Crear motor con las mismas condiciones dos veces
engine1 = OrbitalEngine()
engine1.create_variable("X", theta=0.0, amplitude=10.0, velocity=0.15)
engine1.create_variable("Y", theta=0.5, amplitude=20.0, velocity=0.08)
engine1.create_cycle("Test", ["X", "Y"], threshold=0.3)

engine2 = OrbitalEngine()
engine2.create_variable("X", theta=0.0, amplitude=10.0, velocity=0.15)
engine2.create_variable("Y", theta=0.5, amplitude=20.0, velocity=0.08)
engine2.create_cycle("Test", ["X", "Y"], threshold=0.3)

# Ejecutar un tick en ambos
r1 = engine1.run_tick()
r2 = engine2.run_tick()

# Comparar resultados
print(f"Engine 1 convergió: {r1.cod_results[0].converged}")
print(f"Engine 2 convergió: {r2.cod_results[0].converged}")
print(f"Fases iguales: {r1.cod_results[0].final_phases == r2.cod_results[0].final_phases}")
```

**Criterio de aceptación:**
- ✅ Ambos engines convergen (`converged == True`)
- ✅ Las fases finales son idénticas (determinismo puro)

---

## Validación 2: Amplitudes Extremas (A = 10,000)

**¿Qué prueba?** Que la normalización de amplitud permite convergencia incluso
cuando las amplitudes son 10,000 veces mayores que lo normal. Sin normalización,
el TOR sería ~100,000,000 y `tanh` se saturaría.

```python
from src.orbital.engine import OrbitalEngine

engine = OrbitalEngine()
engine.create_variable("A", theta=0.0, amplitude=10000, velocity=0.2)
engine.create_variable("B", theta=1.0, amplitude=8000, velocity=0.15)
engine.create_cycle("Extreme", ["A", "B"], threshold=0.3)

result = engine.run_tick()
cod = result.cod_results[0]

print(f"Convergió: {cod.converged}")
print(f"Iteraciones: {cod.iterations}")
print(f"Delta final: {cod.convergence_delta:.8f}")
```

**Criterio de aceptación:**
- ✅ Converge (`converged == True`)
- ✅ En menos de 100 iteraciones
- ✅ Delta final < 1e-4

---

## Validación 3: Benchmarks Automáticos

**¿Qué prueba?** Que todos los componentes del motor (TOR, COD, cache, engine)
ejecutan correctamente sus benchmarks sin errores.

```bash
python -m src.orbital.benchmarks
```

**Criterio de aceptación:**
- ✅ Todos los benchmarks completan sin error
- ✅ TOR matrix: todos los tamaños calculan
- ✅ COD convergence: todas las configuraciones convergen
- ✅ COD amplitudes: incluso A=10,000 converge
- ✅ TOR cache: hit rate > 90%
- ✅ Engine throughput: al menos 5 ticks/s

---

## Validación 4: Suite de Tests

**¿Qué prueba?** Que los tests unitarios y de integración del motor ORBITAL
pasan correctamente.

```bash
python -m pytest src/tests/ --ignore=src/tests/test_ui_playwright.py -q --tb=short
```

**Criterio de aceptación:**
- ✅ Tasa de aprobación > 90%
- ✅ Sin errores de importación
- ✅ Tests de orbital específicamente pasan todos

---

## Validación 5: Seguridad Básica

**¿Qué prueba?** Que no hay vulnerabilidades conocidas en el código fuente.

```bash
pip install semgrep 2>/dev/null || true
semgrep --config auto --severity ERROR src/ 2>&1 | tail -20
```

**Criterio de aceptación:**
- ✅ 0 findings de severidad ERROR
- ✅ Sin `eval()` en código de producción (verificado)
- ✅ Sin secrets hardcodeados (verificado)

---

## Checklist de Validación

| # | Prueba | Resultado |
|---|--------|-----------|
| 1 | Determinismo: mismas entradas → mismo estado | ⬜ |
| 2 | Amplitudes extremas: A=10000 converge < 100 iteraciones | ⬜ |
| 3 | Benchmarks: todos completan sin error | ⬜ |
| 4 | Tests: > 90% pass rate | ⬜ |
| 5 | Seguridad: 0 findings semgrep ERROR | ⬜ |

**Firma del validador:** _______________ **Fecha:** _______________

---

## Documentos Relacionados

- `docs/orbital-technical.md` — Arquitectura y optimizaciones
- `docs/orbital-benchmarks.md` — Benchmarks detallados
- `docs/orbital-whitepaper.md` — White paper en inglés
- `docs/benchmark-report.md` — Comparativa vs n8n/Zapier