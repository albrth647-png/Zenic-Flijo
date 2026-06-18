import { useEffect, useState } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { apiFetch } from "@/hooks/useApi"
import { toast } from "@/components/ui/toast"
import { Server, Loader2, Database, Activity, HardDrive, Download } from "lucide-react"

interface SystemStatus {
  version: string
  status: string
  db_path: string
}

export function SettingsSystemTab() {
  const [status, setStatus] = useState<SystemStatus | null>(null)
  const [loading, setLoading] = useState(true)
  const [backingUp, setBackingUp] = useState(false)
  const [logs, setLogs] = useState<Array<{ id: number; action: string; created_at: string }>>([])

  useEffect(() => {
    Promise.all([
      apiFetch<SystemStatus>("/api/system/status"),
      apiFetch<Array<{ id: number; action: string; created_at: string }>>("/api/system/logs?limit=20"),
    ]).then(([statusRes, logsRes]) => {
      if (statusRes) setStatus(statusRes)
      if (logsRes) setLogs(logsRes)
      setLoading(false)
    })
  }, [])

  const handleBackup = async () => {
    setBackingUp(true)
    const res = await apiFetch<{ path: string; status: string }>("/api/system/backup", {
      method: "POST",
    })
    setBackingUp(false)
    if (res?.status === "completed") {
      toast({
        title: "Backup completado",
        description: "La copia de seguridad se creó correctamente",
        variant: "success",
      })
    } else {
      toast({
        title: "Error al hacer backup",
        description: "No se pudo completar la copia de seguridad",
        variant: "error",
      })
    }
  }

  if (loading) {
    return (
      <Card>
        <CardContent className="p-6">
          <div className="skeleton h-4 w-32 mb-4" />
          <div className="skeleton h-20 w-full mb-3" />
          <div className="skeleton h-40 w-full" />
        </CardContent>
      </Card>
    )
  }

  return (
    <div className="space-y-4">
      <Card>
        <CardHeader>
          <CardTitle className="text-lg flex items-center gap-2">
            <Server className="size-4" />
            Información del sistema
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div className="space-y-3">
              <div className="flex items-center justify-between rounded-lg border p-3">
                <div className="flex items-center gap-2">
                  <Activity className="size-4 text-muted-foreground" />
                  <span className="text-muted-foreground">Versión</span>
                </div>
                <span className="font-medium">{status?.version || "—"}</span>
              </div>
              <div className="flex items-center justify-between rounded-lg border p-3">
                <div className="flex items-center gap-2">
                  <Activity className="size-4 text-muted-foreground" />
                  <span className="text-muted-foreground">Estado</span>
                </div>
                <Badge variant="success">Funcionando</Badge>
              </div>
            </div>
            <div className="space-y-3">
              <div className="flex items-center justify-between rounded-lg border p-3">
                <div className="flex items-center gap-2">
                  <Database className="size-4 text-muted-foreground" />
                  <span className="text-muted-foreground">Base de datos</span>
                </div>
                <span className="text-xs font-mono text-muted-foreground truncate max-w-[140px]">
                  {status?.db_path || "—"}
                </span>
              </div>
              <div className="flex items-center justify-between rounded-lg border p-3">
                <div className="flex items-center gap-2">
                  <HardDrive className="size-4 text-muted-foreground" />
                  <span className="text-muted-foreground">Backup</span>
                </div>
                <Button variant="outline" size="sm" className="h-7 text-xs" onClick={handleBackup} disabled={backingUp}>
                  {backingUp ? (
                    <Loader2 className="size-3 animate-spin mr-1" />
                  ) : (
                    <Download className="size-3 mr-1" />
                  )}
                  {backingUp ? "Respaldando..." : "Hacer backup"}
                </Button>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle className="text-lg">Registro de actividades</CardTitle>
          <p className="text-sm text-muted-foreground">
            Últimas acciones registradas en el sistema
          </p>
        </CardHeader>
        <CardContent>
          {logs.length === 0 ? (
            <p className="text-sm text-muted-foreground py-6 text-center">
              No hay registros de actividad aún
            </p>
          ) : (
            <div className="space-y-1 max-h-64 overflow-y-auto">
              {logs.map((log) => (
                <div
                  key={log.id}
                  className="flex items-center justify-between rounded-lg border px-3 py-2 text-sm hover:bg-accent/50 transition-colors"
                >
                  <span className="text-muted-foreground text-xs font-mono truncate flex-1">
                    {log.action}
                  </span>
                  <span className="text-[10px] text-muted-foreground shrink-0 ml-2">
                    {log.created_at
                      ? new Date(log.created_at).toLocaleString("es-ES", {
                          day: "numeric",
                          month: "short",
                          hour: "2-digit",
                          minute: "2-digit",
                        })
                      : ""}
                  </span>
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  )
}
