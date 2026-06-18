import { useEffect, useRef, useState } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { StatusBadge } from "@/components/StatusBadge"
import { apiFetch } from "@/hooks/useApi"
import {
  Plus, RefreshCw
} from "lucide-react"
import { Link } from "react-router-dom"

interface Workflow {
  id: number
  name: string
  status: string
  trigger_type: string
  updated_at: string
  last_execution_at: string | null
}

export default function Workflows() {
  const [workflows, setWorkflows] = useState<Workflow[]>([])
  const [loading, setLoading] = useState(true)
  const cancelledRef = useRef(false)

  const load = async () => {
    setLoading(true)
    const data = await apiFetch<Workflow[]>("/api/workflows")
    if (cancelledRef.current) return
    if (data) setWorkflows(data)
    if (!cancelledRef.current) setLoading(false)
  }

  useEffect(() => {
    cancelledRef.current = false
    // eslint-disable-next-line react-hooks/set-state-in-effect
    load()
    return () => { cancelledRef.current = true }
  }, [])

  const toggleStatus = async (id: number, status: string) => {
    const action = status === "active" ? "pause" : "activate"
    const res = await apiFetch(`/api/workflows/${id}/${action}`, { method: "POST" })
    if (res) load()
  }

  const deleteWorkflow = async (id: number) => {
    if (!confirm("¿Eliminar este workflow?")) return
    const res = await apiFetch(`/api/workflows/${id}`, { method: "DELETE" })
    if (res) load()
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight">Workflows</h1>
          <p className="text-muted-foreground text-sm">
            Gestiona tus automatizaciones
          </p>
        </div>
        <div className="flex gap-2">
          <Button variant="outline" size="sm" onClick={load}>
            <RefreshCw className="size-3 mr-1" /> Recargar
          </Button>
          <Link to="/app/editor">
            <Button size="sm">
              <Plus className="size-3 mr-1" /> Nuevo
            </Button>
          </Link>
        </div>
      </div>

      <Card>
        <CardHeader>
          <CardTitle className="text-lg">Todos los workflows</CardTitle>
        </CardHeader>
        <CardContent>
          {loading ? (
            <p className="text-sm text-muted-foreground py-8 text-center">
              Cargando...
            </p>
          ) : workflows.length === 0 ? (
            <p className="text-sm text-muted-foreground py-8 text-center">
              No hay workflows aún.{" "}
              <Link to="/app/editor" className="text-primary hover:underline">
                Crea el primero
              </Link>
            </p>
          ) : (
            <div className="space-y-2">
              {workflows.map((wf) => (
                <div
                  key={wf.id}
                  className="flex items-center justify-between rounded-lg border p-3 hover:bg-accent/50 transition-colors"
                >
                  <div className="flex items-center gap-3">
                    <div>
                      <Link
                        to={`/app/editor?wf=${wf.id}`}
                        className="font-medium text-sm hover:text-primary transition-colors"
                      >
                        {wf.name || "Sin nombre"}
                      </Link>
                      <div className="flex items-center gap-2 mt-1">
                        <Badge variant="outline" className="text-[10px] px-1.5 py-0">
                          {wf.trigger_type}
                        </Badge>
                        <span className="text-xs text-muted-foreground">
                          #{wf.id}
                        </span>
                      </div>
                    </div>
                  </div>
                  <div className="flex items-center gap-2">
                    <StatusBadge status={wf.status} />
                    <Button
                      variant="ghost"
                      size="sm"
                      onClick={() => toggleStatus(wf.id, wf.status)}
                    >
                      {wf.status === "active" ? "⏸" : "▶️"}
                    </Button>
                    <Button
                      variant="ghost"
                      size="sm"
                      className="text-destructive hover:text-destructive"
                      onClick={() => deleteWorkflow(wf.id)}
                    >
                      🗑
                    </Button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  )
}


