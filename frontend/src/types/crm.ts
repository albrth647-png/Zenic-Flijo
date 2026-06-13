export type LeadStage = "new" | "contacted" | "qualified" | "won" | "lost"

export interface Lead {
  id: number
  name: string
  email?: string
  phone?: string
  company?: string
  source: string
  stage: string
  notes?: string
  created_at?: string
  user_id?: number
}

export interface LeadFormData {
  name: string
  email: string
  phone: string
  company: string
  source: string
  notes: string
}

export type StageCounts = Record<string, number>
