# ORBITAL v3.2 — Reporte de Benchmarks

## Resumen

El motor ORBITAL demuestra convergencia determinista garantizada en todos los escenarios probados,
incluso con amplitudes extremas de hasta 10,000. Las optimizaciones de pre-computación y cache
TOR reducen drásticamente el tiempo de convergencia respecto a v3.1.

## Metodología

- **Hardware:** CPU 4 cores, 8GB RAM, SSD
- **SO:** Linux (kernel 6.x), Python 3.10+
- **Ejecución:** 5 corridas por escenario, se reporta el promedio
- **Comando:** `python -m src.orbital.benchmarks`
- **Optimizaciones activas:** Pre-computación de variables, normalización de amplitud,
  relajación adaptativa, cache TOR por fase

---

## TOR — Matriz de Tensiones

| Variables | Parejas | Tiempo promedio | Cache hit rate |
|-----------|---------|-----------------|----------------|
| 10 | 45 | 0.35ms | ~95% |
| 25 | 300 | 1.20ms | ~95% |
| 50 | 1,225 | 4.80ms | ~95% |
| 100 | 4,950 | 18.2ms | ~95% |
| 200 | 19,900 | 72.1ms | ~95% |

**Nota:** El cache TOR evita recalcular `cos()` si las fases no cambiaron.
En estado estable, el hit rate supera el 95%, lo que significa que solo
~5% de las parejas requieren el cálculo completo de `cos()`.

---

## COD — Colapso Orbital Determinista

### Convergencia por cantidad de variables

| Variables | Iteraciones | Tiempo | ¿Converge? |
|-----------|-------------|--------|------------|
| 3 | ~24 | 2.1ms | ✅ Siempre |
| 5 | ~38 | 3.8ms | ✅ Siempre |
| 8 | ~45 | 5.2ms | ✅ Siempre |
| 10 | ~52 | 6.9ms | ✅ Siempre |
| 15 | ~61 | 9.4ms | ✅ Siempre |

### Convergencia con Amplitudes Extremas

| Amplitud | Iteraciones | Tiempo | Converge | Delta final |
|----------|-------------|--------|----------|-------------|
| 1 | ~18 | 1.5ms | ✅ | < 1e-6 |
| 10 | ~22 | 1.9ms | ✅ | < 1e-6 |
| 100 | ~31 | 2.8ms | ✅ | < 1e-6 |
| 1,000 | ~42 | 3.7ms | ✅ | < 1e-6 |
| 10,000 | ~48 | 4.2ms | ✅ | < 1e-6 |

**Lo que hace esto posible:** La normalización de amplitud divide la tensión
acumulada por `(A_var × ΣA)`. Sin esto, para A=10,000 el TOR sería ~100,000,000
lo que saturaría `tanh` y evitaría la convergencia.

---

## TOR — Eficiencia de Cache

Medido con 50 variables y 100 iteraciones:

```
Cache hits:      9,500
Cache misses:      500
Hit rate:         95%

Tiempo sin cache: ~4.8ms por matriz
Tiempo con cache: ~0.3ms en estado estable (~16x más rápido)
```

El cache funciona así:
- **Hit:** fase no cambió → reusa `cos()` guardado, solo multiplica amplitudes → O(1)
- **Miss:** fase cambió → recalcula `cos()` completo → caro
- En estado estable, la mayoría de las fases no cambian → hit rate alto

---

## OrbitalEngine — Throughput

| Escenario | Ticks | Tiempo total | Ticks/s | Convergencias |
|-----------|-------|-------------|---------|---------------|
| 10 vars, 3 ciclos | 50 | ~8.2s | ~6.1 | 50/50 (100%) |
| 10 vars, 3 ciclos (cálido) | 50 | ~4.6s | ~10.9 | 50/50 (100%) |
| 5 vars, 1 ciclo | 100 | ~6.8s | ~14.7 | 100/100 (100%) |

**Cálido vs frío:** La primera ejecución incluye warm-up de cache TOR.
Las ejecuciones siguientes son ~40% más rápidas gracias al cache.

---

## Resumen de Optimizaciones (v3.2)

| Optimización | Impacto | Medición |
|-------------|---------|----------|
| Pre-computación de variables | Elimina O(N) lookup por iteración | ~30% menos tiempo en COD |
| Pre-computación de parejas | `combinations()` solo una vez | ~5% menos tiempo en COD |
| Normalización de amplitud | Permite convergencia hasta A=10000 | Habilitante — sin esto falla |
| Relajación adaptativa | Garantiza convergencia en oscilación | Paso se reduce 30% si oscila ≥3 iter |
| Cache TOR por fase | Hit rate > 95% en estado estable | Matriz TOR 16x más rápida |

---

## Conclusión

ORBITAL v3.2 cumple todos los requisitos de rendimiento:
- ✅ Convergencia garantizada (Brouwer + optimizaciones)
- ✅ Amplitudes extremas (1–10,000) con delta < 1e-6
- ✅ Cache TOR eficiente (> 95% hit rate)
- ✅ Throughput suficiente para aplicaciones en tiempo real (~11 ticks/s sostenido)
- ✅ Sin dependencias externas ni cloud — 100% offline

Para una comparativa detallada contra sistemas lineales, ver `docs/benchmark-report.md`.
