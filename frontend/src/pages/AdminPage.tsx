import { useState, useEffect, useCallback } from "react"
import { useApi } from "@/hooks/useApi"
import { toast } from "@/components/ui/toast"
import { Card, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription, DialogFooter } from "@/components/ui/dialog"
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Skeleton } from "@/components/ui/skeleton"
import { EmptyState } from "@/components/ui/empty-state"
import { MetricsTab } from "@/components/admin/MetricsTab"
import { AlertsTab } from "@/components/admin/AlertsTab"
import {
  Users as UsersIcon,
  Trash2,
  Edit,
  Shield,
  Activity,
  RefreshCw,
  AlertCircle,
  Play,
  XCircle,
  RotateCcw,
  UserPlus,
  Inbox,
  CheckCircle2,
  Loader2,
} from "lucide-react"

import type {
  AdminUser as User,
  DeadLetterEntry,
  DeadLetterStats,
  QueueMetrics,
  WorkerInfo,
  QueueItem,
} from "@/types/admin"

// ── Componentes ──────────────────────────────────────

function UsersTab() {
  const { getApi } = useApi()
  const [users, setUsers] = useState<User[]>([])
  const [loading, setLoading] = useState(true)
  const [showDialog, setShowDialog] = useState(false)
  const [editingUser, setEditingUser] = useState<User | null>(null)
  const [form, setForm] = useState({ username: "", password: "", display_name: "", email: "", role: "editor" as string })
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState("")

  const loadUsers = useCallback(async () => {
    try {
      const api = getApi()
      const data = await api.get("/api/users")
      setUsers(data as User[])
    } catch {
      toast({ title: "Error al cargar usuarios", variant: "error" })
    } finally {
      setLoading(false)
    }
  }, [getApi])

  useEffect(() => {
    const ac = new AbortController()
    // eslint-disable-next-line react-hooks/set-state-in-effect
    loadUsers()
    return () => ac.abort()
  }, [loadUsers])

  async function handleSave() {
    setSaving(true)
    setError("")
    try {
      const api = getApi()
      if (editingUser) {
        await api.put(`/api/users/${editingUser.id}`, {
          display_name: form.display_name,
          email: form.email,
          role: form.role,
        })
      } else {
        await api.post("/api/users", form)
      }
      setShowDialog(false)
      setEditingUser(null)
      setForm({ username: "", password: "", display_name: "", email: "", role: "editor" })
      loadUsers()
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : "Error al guardar el usuario")
    } finally {
      setSaving(false)
    }
  }

  async function handleDelete(userId: number, username: string) {
    if (!confirm(`¿Estás seguro de eliminar a "${username}"? Esta acción no se puede deshacer.`)) return
    try {
      const api = getApi()
      await api.delete(`/api/users/${userId}`)
      loadUsers()
    } catch {
      toast({ title: "Error al eliminar usuario", variant: "error" })
    }
  }

  function openEdit(user: User) {
    setEditingUser(user)
    setForm({
      username: user.username,
      password: "",
      display_name: user.display_name || "",
      email: user.email || "",
      role: user.role,
    })
    setShowDialog(true)
  }

  const roleBadge = (role: string) => {
    const styles: Record<string, string> = {
      admin: "bg-red-500/10 text-red-400 border-red-500/20",
      editor: "bg-blue-500/10 text-blue-400 border-blue-500/20",
      viewer: "bg-zinc-500/10 text-zinc-400 border-zinc-500/20",
    }
    const labels: Record<string, string> = {
      admin: "Administrador",
      editor: "Editor",
      viewer: "Solo lectura",
    }
    return (
      <Badge variant="outline" className={`border ${styles[role] || styles.viewer}`}>
        <Shield className="mr-1 h-3 w-3" />
        {labels[role] || role}
      </Badge>
    )
  }

  if (loading) {
    return (
      <div className="space-y-3">
        {[1, 2, 3].map((i) => (
          <Skeleton key={i} className="h-16 w-full rounded-lg bg-zinc-800" />
        ))}
      </div>
    )
  }

  return (
    <div>
      <div className="mb-4 flex items-center justify-between">
        <p className="text-sm text-zinc-400">
          {users.length} usuario{users.length !== 1 ? "s" : ""} registrado{users.length !== 1 ? "s" : ""}
        </p>
        <Button
          onClick={() => {
            setEditingUser(null)
            setForm({ username: "", password: "", display_name: "", email: "", role: "editor" })
            setShowDialog(true)
          }}
          className="bg-indigo-600 text-white hover:bg-indigo-500"
        >
          <UserPlus className="mr-1.5 h-4 w-4" />
          Nuevo usuario
        </Button>
      </div>

      {users.length === 0 ? (
        <EmptyState
          icon={<UsersIcon className="h-12 w-12" />}
          title="No hay usuarios aún"
          description="Crea el primer usuario para empezar a trabajar en equipo."
        />
      ) : (
        <div className="space-y-2">
          {users.map((user) => (
            <div
              key={user.id}
              className="flex items-center justify-between rounded-lg border border-zinc-800 bg-zinc-900/50 p-4 transition-colors hover:border-zinc-700"
            >
              <div className="flex items-center gap-3">
                <div className="flex h-10 w-10 items-center justify-center rounded-full bg-zinc-800 text-sm font-medium text-zinc-300">
                  {(user.display_name || user.username).charAt(0).toUpperCase()}
                </div>
                <div>
                  <div className="flex items-center gap-2">
                    <span className="font-medium text-zinc-200">
                      {user.display_name || user.username}
                    </span>
                    {!user.is_active && (
                      <Badge variant="outline" className="border-red-500/20 bg-red-500/10 text-xs text-red-400">
                        Inactivo
                      </Badge>
                    )}
                  </div>
                  <div className="mt-0.5 flex items-center gap-3 text-xs text-zinc-500">
                    <span>@{user.username}</span>
                    {user.email && <span>· {user.email}</span>}
                  </div>
                </div>
              </div>
              <div className="flex items-center gap-3">
                {roleBadge(user.role)}
                <Button
                  variant="ghost"
                  size="sm"
                  onClick={() => openEdit(user)}
                  className="text-zinc-400 hover:text-zinc-200"
                >
                  <Edit className="h-4 w-4" />
                </Button>
                <Button
                  variant="ghost"
                  size="sm"
                  onClick={() => handleDelete(user.id, user.username)}
                  className="text-zinc-400 hover:text-red-400"
                >
                  <Trash2 className="h-4 w-4" />
                </Button>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Diálogo de crear/editar usuario */}
      <Dialog open={showDialog} onOpenChange={setShowDialog}>
        <DialogContent className="border-zinc-800 bg-zinc-900 text-zinc-200">
          <DialogHeader>
            <DialogTitle>{editingUser ? "Editar usuario" : "Nuevo usuario"}</DialogTitle>
            <DialogDescription className="text-zinc-400">
              {editingUser
                ? "Actualiza los datos del usuario"
                : "Crea una cuenta para que alguien más pueda usar la plataforma"}
            </DialogDescription>
          </DialogHeader>

          <div className="space-y-4">
            <div>
              <label className="mb-1 block text-sm text-zinc-300">Nombre de usuario</label>
              <Input
                value={form.username}
                onChange={(e) => setForm({ ...form, username: e.target.value })}
                disabled={!!editingUser}
                placeholder="Ej: maria.rodriguez"
                className="border-zinc-700 bg-zinc-800 text-zinc-200 placeholder:text-zinc-500"
              />
            </div>

            {!editingUser && (
              <div>
                <label className="mb-1 block text-sm text-zinc-300">Contraseña</label>
                <Input
                  type="password"
                  value={form.password}
                  onChange={(e) => setForm({ ...form, password: e.target.value })}
                  placeholder="Mínimo 6 caracteres"
                  className="border-zinc-700 bg-zinc-800 text-zinc-200 placeholder:text-zinc-500"
                />
              </div>
            )}

            <div>
              <label className="mb-1 block text-sm text-zinc-300">Nombre visible</label>
              <Input
                value={form.display_name}
                onChange={(e) => setForm({ ...form, display_name: e.target.value })}
                placeholder="Ej: María Rodríguez"
                className="border-zinc-700 bg-zinc-800 text-zinc-200 placeholder:text-zinc-500"
              />
            </div>

            <div>
              <label className="mb-1 block text-sm text-zinc-300">Correo electrónico</label>
              <Input
                type="email"
                value={form.email}
                onChange={(e) => setForm({ ...form, email: e.target.value })}
                placeholder="ejemplo@correo.com"
                className="border-zinc-700 bg-zinc-800 text-zinc-200 placeholder:text-zinc-500"
              />
            </div>

            <div>
              <label className="mb-1 block text-sm text-zinc-300">Rol</label>
              <Select value={form.role} onValueChange={(v) => setForm({ ...form, role: v })}>
                <SelectTrigger className="border-zinc-700 bg-zinc-800 text-zinc-200">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent className="border-zinc-700 bg-zinc-800 text-zinc-200">
                  <SelectItem value="admin">Administrador — acceso completo</SelectItem>
                  <SelectItem value="editor">Editor — puede crear y modificar</SelectItem>
                  <SelectItem value="viewer">Solo lectura — solo ver</SelectItem>
                </SelectContent>
              </Select>
            </div>

            {error && (
              <div className="rounded-lg bg-red-500/10 p-3 text-sm text-red-400">{error}</div>
            )}
          </div>

          <DialogFooter>
            <Button
              variant="outline"
              onClick={() => setShowDialog(false)}
              className="border-zinc-700 text-zinc-300 hover:bg-zinc-800"
            >
              Cancelar
            </Button>
            <Button
              onClick={handleSave}
              disabled={saving || (!editingUser && (!form.username || !form.password))}
              className="bg-indigo-600 text-white hover:bg-indigo-500"
            >
              {saving ? (
                <>
                  <Loader2 className="mr-1.5 h-4 w-4 animate-spin" />
                  Guardando…
                </>
              ) : editingUser ? (
                "Guardar cambios"
              ) : (
                "Crear usuario"
              )}
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  )
}

function DeadLetterTab() {
  const { getApi } = useApi()
  const [entries, setEntries] = useState<DeadLetterEntry[]>([])
  const [stats, setStats] = useState<DeadLetterStats | null>(null)
  const [loading, setLoading] = useState(true)
  const [filter, setFilter] = useState<string>("all")

  const loadData = useCallback(async () => {
    try {
      const api = getApi()
      const [data, statsData] = await Promise.all([
        api.get(`/api/dead-letter${filter !== "all" ? `?status=${filter}` : ""}`),
        api.get("/api/dead-letter/stats"),
      ])
      const r = data as { entries: DeadLetterEntry[]; stats: DeadLetterStats }
      setEntries(r.entries || [])
      setStats(statsData as DeadLetterStats)
    } catch {
      toast({ title: "Error al cargar buzón", variant: "error" })
    } finally {
      setLoading(false)
    }
  }, [getApi, filter])

  useEffect(() => {
    const ac = new AbortController()
    // eslint-disable-next-line react-hooks/set-state-in-effect
    loadData()
    return () => ac.abort()
  }, [loadData])

  async function handleRetry(entryId: number) {
    try {
      const api = getApi()
      await api.post(`/api/dead-letter/${entryId}/retry`)
      loadData()
    } catch {
      toast({ title: "Error al reintentar", variant: "error" })
    }
  }

  async function handleDiscard(entryId: number) {
    try {
      const api = getApi()
      await api.post(`/api/dead-letter/${entryId}/discard`)
      loadData()
    } catch {
      toast({ title: "Error al descartar", variant: "error" })
    }
  }

  async function handleRetryAll() {
    try {
      const api = getApi()
      await api.post("/api/dead-letter/retry-all")
      loadData()
    } catch {
      toast({ title: "Error al reintentar todos", variant: "error" })
    }
  }

  async function handleDiscardAll() {
    if (!confirm("¿Estás seguro de descartar todos los errores? Esta acción no se puede deshacer.")) return
    try {
      const api = getApi()
      await api.post("/api/dead-letter/discard-all")
      loadData()
    } catch {
      toast({ title: "Error al descartar todos", variant: "error" })
    }
  }

  function getStatusBadge(status: string) {
    const styles: Record<string, string> = {
      pending: "bg-amber-500/10 text-amber-400 border-amber-500/20",
      retrying: "bg-blue-500/10 text-blue-400 border-blue-500/20",
      resolved: "bg-emerald-500/10 text-emerald-400 border-emerald-500/20",
      discarded: "bg-zinc-500/10 text-zinc-400 border-zinc-500/20",
    }
    const labels: Record<string, string> = {
      pending: "Pendiente",
      retrying: "Reintentando",
      resolved: "Resuelto",
      discarded: "Descartado",
    }
    return (
      <Badge variant="outline" className={`border ${styles[status] || styles.pending}`}>
        {labels[status] || status}
      </Badge>
    )
  }

  if (loading) {
    return (
      <div className="space-y-3">
        {[1, 2, 3].map((i) => (
          <Skeleton key={i} className="h-20 w-full rounded-lg bg-zinc-800" />
        ))}
      </div>
    )
  }

  return (
    <div>
      {/* Resumen */}
      {stats && (
        <div className="mb-4 grid grid-cols-2 gap-3 sm:grid-cols-5">
          {[
            { label: "Total", value: stats.total, color: "text-zinc-300" },
            { label: "Pendientes", value: stats.pending, color: "text-amber-400" },
            { label: "Reintentando", value: stats.retrying, color: "text-blue-400" },
            { label: "Resueltos", value: stats.resolved, color: "text-emerald-400" },
            { label: "Descartados", value: stats.discarded, color: "text-zinc-500" },
          ].map((item) => (
            <div
              key={item.label}
              className="rounded-lg border border-zinc-800 bg-zinc-900/50 p-3 text-center"
            >
              <p className={`text-2xl font-bold ${item.color}`}>{item.value}</p>
              <p className="mt-1 text-xs text-zinc-500">{item.label}</p>
            </div>
          ))}
        </div>
      )}

      {/* Filtros y acciones */}
      <div className="mb-4 flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-2">
          <Select value={filter} onValueChange={setFilter}>
            <SelectTrigger className="w-[150px] border-zinc-700 bg-zinc-800 text-zinc-200">
              <SelectValue />
            </SelectTrigger>
            <SelectContent className="border-zinc-700 bg-zinc-800 text-zinc-200">
              <SelectItem value="all">Todos</SelectItem>
              <SelectItem value="pending">Pendientes</SelectItem>
              <SelectItem value="retrying">Reintentando</SelectItem>
              <SelectItem value="resolved">Resueltos</SelectItem>
              <SelectItem value="discarded">Descartados</SelectItem>
            </SelectContent>
          </Select>
        </div>
        <div className="flex gap-2">
          <Button
            variant="outline"
            size="sm"
            onClick={handleRetryAll}
            className="border-zinc-700 text-zinc-300 hover:bg-zinc-800"
          >
            <RotateCcw className="mr-1.5 h-3.5 w-3.5" />
            Reintentar todos
          </Button>
          <Button
            variant="outline"
            size="sm"
            onClick={handleDiscardAll}
            className="border-zinc-700 text-zinc-300 hover:bg-zinc-800"
          >
            <Trash2 className="mr-1.5 h-3.5 w-3.5" />
            Descartar todos
          </Button>
          <Button
            variant="ghost"
            size="sm"
            onClick={loadData}
            className="text-zinc-400 hover:text-zinc-200"
          >
            <RefreshCw className="h-4 w-4" />
          </Button>
        </div>
      </div>

      {entries.length === 0 ? (
        <EmptyState
          icon={<CheckCircle2 className="h-12 w-12 text-emerald-400" />}
          title="Todo en orden"
          description="No hay errores pendientes. Todos los workflows están funcionando correctamente."
        />
      ) : (
        <div className="space-y-2">
          {entries.map((entry) => (
            <div
              key={entry.id}
              className="rounded-lg border border-zinc-800 bg-zinc-900/50 p-4 transition-colors hover:border-zinc-700"
            >
              <div className="flex items-start justify-between gap-3">
                <div className="flex-1">
                  <div className="mb-1 flex items-center gap-2">
                    {getStatusBadge(entry.status)}
                    <span className="text-sm font-medium text-zinc-200">
                      {entry.workflow_name || `Workflow #${entry.workflow_id}`}
                    </span>
                    {entry.retry_count > 0 && (
                      <span className="text-xs text-zinc-500">
                        ({entry.retry_count} reintento{entry.retry_count !== 1 ? "s" : ""})
                      </span>
                    )}
                  </div>
                  <p className="text-sm text-zinc-400">{entry.error_message}</p>
                  <div className="mt-1 flex items-center gap-3 text-xs text-zinc-600">
                    <span>{new Date(entry.failed_at).toLocaleString("es-MX")}</span>
                    {entry.step_id && <span>· Paso: {entry.step_id}</span>}
                  </div>
                </div>
                <div className="flex gap-1">
                  {(entry.status === "pending" || entry.status === "retrying") && (
                    <>
                      <Button
                        variant="ghost"
                        size="sm"
                        onClick={() => handleRetry(entry.id)}
                        className="text-zinc-400 hover:text-emerald-400"
                        title="Reintentar"
                      >
                        <Play className="h-4 w-4" />
                      </Button>
                      <Button
                        variant="ghost"
                        size="sm"
                        onClick={() => handleDiscard(entry.id)}
                        className="text-zinc-400 hover:text-red-400"
                        title="Descartar"
                      >
                        <XCircle className="h-4 w-4" />
                      </Button>
                    </>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

function QueueTab() {
  const { getApi } = useApi()
  const [metrics, setMetrics] = useState<QueueMetrics | null>(null)
  const [workers, setWorkers] = useState<WorkerInfo[]>([])
  const [items, setItems] = useState<QueueItem[]>([])
  const [loading, setLoading] = useState(true)

  const loadData = useCallback(async () => {
    try {
      const api = getApi()
      const [statusData, workersData] = await Promise.all([
        api.get("/api/queue/status"),
        api.get("/api/queue/workers"),
      ])
      const s = statusData as { metrics: QueueMetrics; next_items: QueueItem[] }
      setMetrics(s.metrics)
      setItems(s.next_items || [])
      setWorkers(workersData as WorkerInfo[])
    } catch {
      toast({ title: "Error al cargar cola", variant: "error" })
    } finally {
      setLoading(false)
    }
  }, [getApi])

  useEffect(() => {
    const ac = new AbortController()
    // eslint-disable-next-line react-hooks/set-state-in-effect
    loadData()
    return () => ac.abort()
  }, [loadData])

  const formatTime = (seconds: number) => {
    if (seconds < 60) return `${Math.round(seconds)}s`
    if (seconds < 3600) return `${Math.round(seconds / 60)}min`
    return `${(seconds / 3600).toFixed(1)}h`
  }

  if (loading) {
    return (
      <div className="space-y-3">
        {[1, 2, 3].map((i) => (
          <Skeleton key={i} className="h-16 w-full rounded-lg bg-zinc-800" />
        ))}
      </div>
    )
  }

  return (
    <div>
      {/* Métricas */}
      {metrics && (
        <div className="mb-4 grid grid-cols-2 gap-3 sm:grid-cols-5">
          {[
            { label: "En cola", value: metrics.queue_size, icon: <Inbox className="h-4 w-4" />, color: "text-blue-400" },
            { label: "Procesando", value: metrics.processing, icon: <Activity className="h-4 w-4" />, color: "text-amber-400" },
            { label: "Completados", value: metrics.completed, icon: <CheckCircle2 className="h-4 w-4" />, color: "text-emerald-400" },
            { label: "Fallidos", value: metrics.failed, icon: <AlertCircle className="h-4 w-4" />, color: "text-red-400" },
            { label: "Ritmo", value: `${metrics.throughput_per_minute}/min`, icon: <Activity className="h-4 w-4" />, color: "text-zinc-300" },
          ].map((item) => (
            <div
              key={item.label}
              className="rounded-lg border border-zinc-800 bg-zinc-900/50 p-3"
            >
              <div className="flex items-center justify-between">
                <p className={`text-lg font-bold ${item.color}`}>{item.value}</p>
                <span className="text-zinc-600">{item.icon}</span>
              </div>
              <p className="mt-1 text-xs text-zinc-500">{item.label}</p>
            </div>
          ))}
        </div>
      )}

      {/* Trabajadores activos */}
      <div className="mb-4">
        <h3 className="mb-2 text-sm font-medium text-zinc-300">Trabajadores activos</h3>
        {workers.length === 0 ? (
          <p className="text-sm text-zinc-500">No hay trabajadores activos en este momento</p>
        ) : (
          <div className="space-y-2">
            {workers.map((worker) => (
              <div
                key={worker.id}
                className="flex items-center justify-between rounded-lg border border-zinc-800 bg-zinc-900/50 p-3"
              >
                <div className="flex items-center gap-3">
                  <div
                    className={`h-2 w-2 rounded-full ${
                      worker.status === "active" ? "bg-emerald-400" : "bg-zinc-600"
                    }`}
                  />
                  <div>
                    <p className="text-sm font-medium text-zinc-200">{worker.name}</p>
                    <p className="text-xs text-zinc-500">
                      {worker.tasks_completed} tarea{worker.tasks_completed !== 1 ? "s" : ""} completada{worker.tasks_completed !== 1 ? "s" : ""}
                      {worker.uptime_seconds > 0 && ` · ${formatTime(worker.uptime_seconds)} activo`}
                    </p>
                  </div>
                </div>
                {worker.current_task && (
                  <Badge variant="outline" className="border-blue-500/20 bg-blue-500/10 text-xs text-blue-400">
                    <Activity className="mr-1 h-3 w-3" />
                    {worker.current_task}
                  </Badge>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Próximos trabajos */}
      <div>
        <h3 className="mb-2 text-sm font-medium text-zinc-300">Próximos trabajos</h3>
        {items.length === 0 ? (
          <EmptyState
            icon={<Inbox className="h-10 w-10" />}
            title="Cola vacía"
            description="No hay trabajos pendientes. Todo está al día."
          />
        ) : (
          <div className="space-y-2">
            {items.map((item) => (
              <div
                key={item.id}
                className="flex items-center justify-between rounded-lg border border-zinc-800 bg-zinc-900/50 p-3"
              >
                <div>
                  <p className="text-sm font-medium text-zinc-200">
                    {item.workflow_name || `Workflow #${item.workflow_id}`}
                  </p>
                  <p className="text-xs text-zinc-500">
                    Prioridad: {item.priority} · {new Date(item.created_at).toLocaleString("es-MX")}
                  </p>
                </div>
                <Badge
                  variant="outline"
                  className={`border ${
                    item.status === "processing"
                      ? "border-amber-500/20 bg-amber-500/10 text-amber-400"
                      : item.status === "failed"
                        ? "border-red-500/20 bg-red-500/10 text-red-400"
                        : "border-zinc-700 bg-zinc-800 text-zinc-400"
                  }`}
                >
                  {item.status === "processing"
                    ? "Procesando"
                    : item.status === "failed"
                      ? "Fallido"
                      : "En espera"}
                </Badge>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

// ── Página principal ─────────────────────────────────

export default function AdminPage() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-semibold text-zinc-100">Panel de Administración</h1>
        <p className="mt-1 text-sm text-zinc-400">
          Gestiona usuarios, revisa errores y supervisa el motor de workflows
        </p>
      </div>

      <Tabs defaultValue="users" className="w-full">
        <TabsList className="border-zinc-800 bg-zinc-900">
          <TabsTrigger
            value="users"
            className="data-[state=active]:bg-zinc-800 data-[state=active]:text-zinc-100"
          >
            <UsersIcon className="mr-1.5 h-4 w-4" />
            Usuarios
          </TabsTrigger>
          <TabsTrigger
            value="dead-letter"
            className="data-[state=active]:bg-zinc-800 data-[state=active]:text-zinc-100"
          >
            <AlertCircle className="mr-1.5 h-4 w-4" />
            Buzón de errores
          </TabsTrigger>
          <TabsTrigger
            value="queue"
            className="data-[state=active]:bg-zinc-800 data-[state=active]:text-zinc-100"
          >
            <Activity className="mr-1.5 h-4 w-4" />
            Cola de trabajos
          </TabsTrigger>
          <TabsTrigger
            value="metrics"
            className="data-[state=active]:bg-zinc-800 data-[state=active]:text-zinc-100"
          >
            <Activity className="mr-1.5 h-4 w-4" />
            Métricas
          </TabsTrigger>
          <TabsTrigger
            value="alerts"
            className="data-[state=active]:bg-zinc-800 data-[state=active]:text-zinc-100"
          >
            <AlertCircle className="mr-1.5 h-4 w-4" />
            Alertas
          </TabsTrigger>
        </TabsList>

        <div className="mt-4">
          <TabsContent value="users">
            <Card className="border-zinc-800 bg-zinc-900/50">
              <CardContent className="p-4">
                <UsersTab />
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="dead-letter">
            <Card className="border-zinc-800 bg-zinc-900/50">
              <CardContent className="p-4">
                <DeadLetterTab />
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="queue">
            <Card className="border-zinc-800 bg-zinc-900/50">
              <CardContent className="p-4">
                <QueueTab />
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="metrics">
            <Card className="border-zinc-800 bg-zinc-900/50">
              <CardContent className="p-4">
                <MetricsTab />
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="alerts">
            <Card className="border-zinc-800 bg-zinc-900/50">
              <CardContent className="p-4">
                <AlertsTab />
              </CardContent>
            </Card>
          </TabsContent>
        </div>
      </Tabs>
    </div>
  )
}
