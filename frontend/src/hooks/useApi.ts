import { useCallback, useState } from "react"

interface ApiOptions extends RequestInit {
  skipAuth?: boolean
  signal?: AbortSignal
}

export function useApi() {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const api = useCallback(async <T = unknown>(path: string, options: ApiOptions = {}): Promise<T | null> => {
    setLoading(true)
    setError(null)
    try {
      const res = await fetch(path, {
        headers: {
          "Content-Type": "application/json",
          ...options.headers,
        },
        credentials: "include",
        ...options,
      })
      if (res.status === 401 && !options.skipAuth) {
        // Si la sesión expiró, redirige al login
        window.location.href = "/login?expired=1"
        return null
      }
      if (!res.ok) {
        const data = await res.json().catch(() => ({}))
        // Soporta formato ErrorResponse: { error: "code", message: "text", details: {} }
        // y formato legacy: { error: "text" }
        const errMsg = data.message || data.error || `Error ${res.status}`
        setError(errMsg)
        return null
      }
      const data = await res.json()
      return data as T
    } catch (e) {
      if (e instanceof DOMException && e.name === "AbortError") {
        return null  // Petición cancelada intencionalmente
      }
      const errMsg = e instanceof Error ? e.message : "Error de conexión"
      setError(errMsg)
      return null
    } finally {
      setLoading(false)
    }
  }, [])

  return { api, loading, error }
}

export async function apiFetch<T = unknown>(path: string, options: ApiOptions = {}): Promise<T | null> {
  try {
    const res = await fetch(path, {
      headers: {
        "Content-Type": "application/json",
        ...options.headers,
      },
      credentials: "include",
      ...options,
    })
    if (res.status === 401 && !options.skipAuth) {
      window.location.href = "/login?expired=1"
      return null
    }
    if (!res.ok) return null
    return await res.json() as T
  } catch {
    return null
  }
}
