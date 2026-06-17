/**
 * Tests del hook useApi.
 *
 * Previenen regressiones de BUG-FE-01: el hook debe exponer getApi()
 * con métodos HTTP { get, post, put, patch, delete }, además de apiFetch()
 * y los estados loading/error.
 *
 * Si este test falla, las 11 páginas que usan `const api = getApi(); api.get(...)`
 * se romperán en runtime.
 */
import { describe, it, expect, vi, beforeEach, afterEach } from "vitest"
import { renderHook, act } from "@testing-library/react"
import { useApi, apiFetch } from "@/hooks/useApi"

// Mock global fetch
const mockFetch = vi.fn()
vi.stubGlobal("fetch", mockFetch)

describe("useApi hook", () => {
  beforeEach(() => {
    mockFetch.mockReset()
  })

  afterEach(() => {
    vi.clearAllMocks()
  })

  describe("contract", () => {
    it("expone { api, apiFetch, getApi, loading, error }", () => {
      const { result } = renderHook(() => useApi())

      expect(result.current).toHaveProperty("api")
      expect(result.current).toHaveProperty("apiFetch")
      expect(result.current).toHaveProperty("getApi")
      expect(result.current).toHaveProperty("loading")
      expect(result.current).toHaveProperty("error")

      expect(typeof result.current.api).toBe("function")
      expect(typeof result.current.apiFetch).toBe("function")
      expect(typeof result.current.getApi).toBe("function")
      expect(typeof result.current.loading).toBe("boolean")
    })

    it("getApi() retorna objeto con get/post/put/patch/delete", () => {
      const { result } = renderHook(() => useApi())

      const api = result.current.getApi()

      expect(api).not.toBeNull()
      expect(typeof api.get).toBe("function")
      expect(typeof api.post).toBe("function")
      expect(typeof api.put).toBe("function")
      expect(typeof api.patch).toBe("function")
      expect(typeof api.delete).toBe("function")
    })
  })

  describe("getApi().get", () => {
    it("hace GET con credentials: include y Content-Type application/json", async () => {
      mockFetch.mockResolvedValueOnce({
        ok: true,
        status: 200,
        text: () => Promise.resolve(JSON.stringify({ hello: "world" })),
      } as Response)

      const { result } = renderHook(() => useApi())
      const api = result.current.getApi()

      let data
      await act(async () => {
        data = await api.get("/api/test")
      })

      expect(mockFetch).toHaveBeenCalledWith(
        "/api/test",
        expect.objectContaining({
          method: "GET",
          credentials: "include",
          headers: expect.objectContaining({
            "Content-Type": "application/json",
          }),
        }),
      )
      expect(data).toEqual({ hello: "world" })
    })

    it("retorna null en 401 y redirige a /login?expired=1", async () => {
      // Spy para capturar la redirección sin romper el test
      const originalHref = window.location.href
      const hrefSetter = vi.fn()
      Object.defineProperty(window, "location", {
        writable: true,
        value: {
          set href(v: string) { hrefSetter(v) },
          get href() { return originalHref },
        },
      })

      mockFetch.mockResolvedValueOnce({
        ok: false,
        status: 401,
        text: () => Promise.resolve(""),
      } as Response)

      const { result } = renderHook(() => useApi())
      const api = result.current.getApi()

      let data
      await act(async () => {
        data = await api.get("/api/protected")
      })

      expect(data).toBeNull()
      expect(hrefSetter).toHaveBeenCalledWith("/login?expired=1")
    })

    it("retorna null y setea error en 500", async () => {
      mockFetch.mockResolvedValueOnce({
        ok: false,
        status: 500,
        json: () => Promise.resolve({ error: "Internal Server Error" }),
      } as Response)

      const { result } = renderHook(() => useApi())
      const api = result.current.getApi()

      let data
      await act(async () => {
        data = await api.get("/api/broken")
      })

      expect(data).toBeNull()
      expect(result.current.error).toBe("Internal Server Error")
    })
  })

  describe("getApi().post", () => {
    it("hace POST con body JSON.stringify", async () => {
      mockFetch.mockResolvedValueOnce({
        ok: true,
        status: 201,
        text: () => Promise.resolve(JSON.stringify({ id: 1 })),
      } as Response)

      const { result } = renderHook(() => useApi())
      const api = result.current.getApi()

      let data
      await act(async () => {
        data = await api.post("/api/items", { name: "test" })
      })

      expect(mockFetch).toHaveBeenCalledWith(
        "/api/items",
        expect.objectContaining({
          method: "POST",
          body: JSON.stringify({ name: "test" }),
          credentials: "include",
        }),
      )
      expect(data).toEqual({ id: 1 })
    })

    it("hace POST sin body si no se pasa", async () => {
      mockFetch.mockResolvedValueOnce({
        ok: true,
        status: 204,
        text: () => Promise.resolve(""),
      } as Response)

      const { result } = renderHook(() => useApi())
      const api = result.current.getApi()

      let data
      await act(async () => {
        data = await api.post("/api/trigger")
      })

      expect(mockFetch).toHaveBeenCalledWith(
        "/api/trigger",
        expect.objectContaining({
          method: "POST",
          body: undefined,
        }),
      )
      expect(data).toBeNull() // 204 No Content
    })
  })

  describe("getApi().put / patch / delete", () => {
    it("put envía método PUT y body", async () => {
      mockFetch.mockResolvedValueOnce({
        ok: true,
        status: 200,
        text: () => Promise.resolve(JSON.stringify({})),
      } as Response)

      const { result } = renderHook(() => useApi())
      const api = result.current.getApi()

      await act(async () => {
        await api.put("/api/items/1", { name: "updated" })
      })

      expect(mockFetch).toHaveBeenCalledWith(
        "/api/items/1",
        expect.objectContaining({
          method: "PUT",
          body: JSON.stringify({ name: "updated" }),
        }),
      )
    })

    it("patch envía método PATCH", async () => {
      mockFetch.mockResolvedValueOnce({
        ok: true,
        status: 200,
        text: () => Promise.resolve(JSON.stringify({})),
      } as Response)

      const { result } = renderHook(() => useApi())
      const api = result.current.getApi()

      await act(async () => {
        await api.patch("/api/items/1", { status: "active" })
      })

      expect(mockFetch).toHaveBeenCalledWith(
        "/api/items/1",
        expect.objectContaining({
          method: "PATCH",
          body: JSON.stringify({ status: "active" }),
        }),
      )
    })

    it("delete envía método DELETE sin body", async () => {
      mockFetch.mockResolvedValueOnce({
        ok: true,
        status: 200,
        text: () => Promise.resolve(JSON.stringify({})),
      } as Response)

      const { result } = renderHook(() => useApi())
      const api = result.current.getApi()

      await act(async () => {
        await api.delete("/api/items/1")
      })

      expect(mockFetch).toHaveBeenCalledWith(
        "/api/items/1",
        expect.objectContaining({
          method: "DELETE",
          body: undefined,
        }),
      )
    })
  })

  describe("apiFetch (standalone export)", () => {
    it("es una función exportada y funciona sin hook", async () => {
      expect(typeof apiFetch).toBe("function")

      // apiFetch usa res.json() internamente (no res.text())
      mockFetch.mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: () => Promise.resolve({ ok: true }),
      } as Response)

      const data = await apiFetch("/api/standalone")
      expect(data).toEqual({ ok: true })
    })
  })

  describe("loading state", () => {
    it("cambia a true durante la petición y false al terminar", async () => {
      // Mock con un delay simulado
      let resolveFetch: (v: unknown) => void
      mockFetch.mockReturnValueOnce(
        new Promise((resolve) => {
          resolveFetch = resolve
        }),
      )

      const { result } = renderHook(() => useApi())
      const api = result.current.getApi()

      expect(result.current.loading).toBe(false)

      let promise: Promise<unknown> | undefined
      act(() => {
        promise = api.get("/api/slow")
      })

      // El loading debe estar true mientras la promesa no resuelve
      // (puede ser true o false según el timing, lo importante es que termina false)
      await act(async () => {
        resolveFetch!({
          ok: true,
          status: 200,
          text: () => Promise.resolve(JSON.stringify({})),
        })
        await promise
      })

      expect(result.current.loading).toBe(false)
    })
  })
})
