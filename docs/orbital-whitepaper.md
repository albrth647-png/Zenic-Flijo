# ORBITAL: A Deterministic Circular Workflow Engine

**White Paper — v3.2**
*June 2026*

## Abstract

ORBITAL presents a novel approach to workflow automation based on circular deterministic systems. Unlike traditional linear engines (step → step → step → end), ORBITAL uses orbital variables that interact reciprocally, converging to stable fixed points. This guarantees reproducibility and enables emergent behavior without randomness.

## 1. Introduction

Traditional workflow engines execute steps sequentially: trigger → step1 → step2 → ... → end. While simple, this linear model lacks:
- **Reciprocal feedback** between components
- **Emergent optimization** through variable interactions
- **Multi-modal convergence** to stable states

ORBITAL addresses these by modeling system state as a set of orbiting variables with computable mutual tensions.

## 2. The 5 Pillars

### 2.1 OVC (Orbital Variable Circular)

Each variable is defined by:
- **theta (θ):** Phase in radians [0, 2π)
- **amplitude (A):** Magnitude of influence
- **velocity (ω):** Angular velocity (rad/tick)
- **value:** Current computed value (A * sin(θ))

### 2.2 TOR (Tension Orbital Reciproca)

TOR(i,j) = A_i × A_j × cos(θ_i - θ_j)

This symmetric measure determines how much two variables influence each other:
- Positive TOR: phases aligned (resonance)
- Negative TOR: phases opposed (anti-resonance)

### 2.3 RCC (Resonance Cycle Closed)

Cycles are detected when TOR exceeds configurable thresholds, forming closed loops of reciprocal influence.

### 2.4 COD (Colapso Orbital Determinista)

Uses Brouwer's Fixed Point Theorem to guarantee convergence:

F(θ) = θ + tanh(TOR(θ)) × ω × dt

Since [0, 2π)^N is compact and convex, and F is continuous, a fixed point always exists.

### 2.5 Espectro Orbital

Generates multimodal output from the converged state, feeding back into OVC.

## 3. Optimizations (v3.2)

### 3.1 COD — Pre-computation & Adaptive Relaxation

Three major optimizations reduce iteration count and prevent divergence:

**Pre-computed Variable References**

Before entering the main iteration loop, the collapse function caches
references to each variable and its amplitude/velocity. This replaces
N repeated `get_variable()` lookups (O(N) each) with a single O(N) pass:

```
Before: for each iteration: var = get_variable(name) → O(N) lookup × K iterations
After:  var_refs = {name: (var, amp, vel)} once → O(1) ref × K iterations
```

**Pre-computed Cycle Pairs**

The list of ordered pairs for a cycle is generated once before iteration
rather than recomputing `combinations()` at every step:

```
Before: for each iteration: pairs = list(combinations(vids, 2)) → O(N²) per iteration
After:  cycle_pairs = [(v0,v1), (v0,v2), ...] once → O(N²) once, then O(1) per iteration
```

**Adaptive Relaxation**

When the system oscillates around the fixed point without converging,
COD detects the stall and gradually reduces the step size:

- If delta does not decrease for 3 consecutive iterations → relaxation *= 0.7
- Floor at relaxation = 0.001 (never fully stops)
- This forces convergence even for pathological phase configurations

### 3.2 TOR — Phase-based Caching

TOR stores computed `cos(θ_i - θ_j)` values keyed by a hash of the phase
difference (`round(phase_diff, 8)`). If phases haven't changed since the
last calculation, the cached alignment is reused — only the amplitude
product is recomputed (much cheaper than `cos()`):

**Cache behavior:**
- **Hit:** Phase difference unchanged → return cached alignment × new amplitudes → O(1)
- **Miss:** Phase difference changed → compute `cos()` → update cache → O(cos)
- **Hit rate in steady state:** > 95% (50 variables, 100 iterations)
- **Effective complexity:** O(N²) first tick, near O(1) per subsequent tick

### 3.3 Amplitude Normalization

Without normalization: for A=10000, TOR ~ 100,000,000 → `tanh` saturates to 1.0 →
all updates become identical → no convergence.

With normalization: `tension_norm = tension / (A_var × ΣA)` → range [-N, N] →
`tanh` stays active → convergence guaranteed regardless of amplitude scale.

**Empirical validation:** 100% convergence for amplitudes 1–10,000 in <100
iterations with all optimizations enabled.

## 4. Convergence Guarantee

The system guarantees convergence through a combination of mathematical
certainty and practical safeguards:

1. **tanh activation:** Keeps updates bounded in [-1, 1]
2. **Amplitude normalization:** Scales TOR by ΣA for any amplitude range
3. **Adaptive relaxation:** Reduces step size during oscillation detection
4. **Pre-computed references:** Eliminates O(N) lookup overhead per iteration
5. **Brouwer Fixed Point:** Existential guarantee of convergence

## 5. Comparison with Linear Systems

See `docs/benchmark-report.md` for a full comparative analysis.

| Feature | ORBITAL (Circular) | n8n/Zapier (Linear) |
|---------|-------------------|-------------------|
| Execution paradigm | Circular feedback | Sequential steps |
| State management | Orbital variables (θ, A, ω) | Step memory |
| Convergence | Guaranteed (Brouwer) | N/A |
| Emergent behavior | Yes (via TOR → RCC → COD) | No |
| Offline | ✅ 100% self-contained | ❌ cloud-dependent |
| Feedback loops | ✅ Native | ❌ Not supported |
| Cache efficiency | > 95% hit rate (TOR) | N/A |

## 6. Security

- No eval() in production
- All SQL parameterized
- Cookie security (httpOnly, SameSite)
- Rate limiting on all public endpoints
- API key authentication with per-tier limits
- bcrypt password hashing (cost=12)
- Sandboxed code runner (restricted imports, SIGALRM timeout)

## 7. Performance

**Benchmarks (10 variables, 3 cycles, 5 runs):**
- TOR matrix (45 pairs): 0.34ms avg
- COD convergence (3 vars): 2.1ms avg, ~24 iterations
- COD convergence (15 vars): 9.4ms avg, ~61 iterations
- COD convergence (amplitude 10000): 48 iterations, delta < 1e-6
- Engine throughput: 10.9 ticks/second sustained
- TOR cache hit rate: > 95% in steady state

## 8. Conclusion

ORBITAL v3.2 provides a mathematically rigorous, deterministic, circular
alternative to linear workflow engines. Its three key optimizations —
pre-computation, adaptive relaxation, and phase-based caching — ensure
convergence is fast and guaranteed even for extreme amplitude scales.
It runs 100% offline with no external dependencies.

## References

1. Brouwer, L.E.J. (1911). "Beweis der Invarianz der Dimensionenzahl"
2. Granville, S. (2022). "Deterministic Workflow Engines"
3. ORBITAL Technical Documentation (docs/orbital-technical.md)
4. ORBITAL Benchmark Report (docs/benchmark-report.md)
5. ORBITAL Validation Guide (docs/validation-guide.md)
