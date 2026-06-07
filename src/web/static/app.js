// Workflow Determinista — App JS

// ============================================
// Core API helper
// ============================================
async function api(path, options = {}) {
    try {
        const res = await fetch(path, {
            headers: {'Content-Type': 'application/json', ...options.headers},
            ...options
        });
        if (res.status === 401) { window.location.href = '/login'; return null; }
        if (!res.ok) {
            const data = await res.json().catch(() => ({}));
            showToast(data.error || `Error ${res.status}`, 'error');
            return null;
        }
        return res.json();
    } catch (e) {
        showToast('Error de conexión', 'error');
        return null;
    }
}

// ============================================
// Toast notification system
// ============================================
function showToast(message, type = 'info') {
    let container = document.getElementById('toastContainer');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toastContainer';
        container.className = 'toast-container';
        document.body.appendChild(container);
    }
    const icons = { success: '✅', error: '❌', warning: '⚠️', info: 'ℹ️' };
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerHTML = `<span>${icons[type] || ''}</span><span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
        toast.classList.add('hide');
        setTimeout(() => toast.remove(), 300);
    }, 3500);
}

// ============================================
// Date formatting (Spanish relative time)
// ============================================
function formatDate(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    const now = new Date();
    const diffMs = now - date;
    const diffSec = Math.floor(diffMs / 1000);
    const diffMin = Math.floor(diffSec / 60);
    const diffHour = Math.floor(diffMin / 60);
    const diffDay = Math.floor(diffHour / 24);

    if (diffSec < 60) return 'hace un momento';
    if (diffMin < 60) return `hace ${diffMin} min`;
    if (diffHour < 24) return `hace ${diffHour}h`;
    if (diffDay === 1) return 'ayer';
    if (diffDay < 7) return `hace ${diffDay} días`;
    if (diffDay < 30) return `hace ${Math.floor(diffDay / 7)} semanas`;
    return date.toLocaleDateString('es-ES', { day: 'numeric', month: 'short', year: 'numeric' });
}

// ============================================
// Status formatting with icon
// ============================================
function formatStatus(status) {
    const icons = {
        active: '🟢', paused: '🟡', failed: '🔴', error: '🔴',
        completed: '✅', running: '🔵', archived: '⚫'
    };
    const labels = {
        active: 'Activo', paused: 'Pausado', failed: 'Fallido', error: 'Error',
        completed: 'Completado', running: 'Ejecutando', archived: 'Archivado'
    };
    const icon = icons[status] || '⚪';
    const label = labels[status] || status;
    return `<span class="status-badge ${status}">${icon} ${label}</span>`;
}

// ============================================
// License info loader
// ============================================
async function loadLicenseInfo() {
    try {
        const data = await (await fetch('/api/license/info')).json();
        return data;
    } catch (e) {
        return null;
    }
}

// ============================================
// Trial progress bar renderer
// ============================================
function renderTrialProgress(daysLeft, totalDays = 30) {
    const pct = Math.max(0, Math.min(100, ((totalDays - daysLeft) / totalDays) * 100));
    const remaining = Math.max(0, daysLeft);
    let cls = 'active';
    if (remaining <= 5) cls = 'warning';
    if (remaining <= 0) cls = 'expired';
    return `
        <div class="trial-progress">
            <div class="trial-progress-label">
                <span>${remaining > 0 ? `${remaining} días restantes` : 'Período expirado'}</span>
                <span>${totalDays} días totales</span>
            </div>
            <div class="trial-progress-bar">
                <div class="trial-progress-fill ${cls}" style="width:${pct}%"></div>
            </div>
        </div>
    `;
}

// ============================================
// Dashboard charts (Chart.js)
// ============================================
let chartInstances = {};

function destroyCharts() {
    Object.values(chartInstances).forEach(c => { try { c.destroy(); } catch {} });
    chartInstances = {};
}

async function loadDashboardCharts() {
    if (typeof Chart === 'undefined') {
        console.warn('Chart.js no disponible — recarga la página');
        return;
    }
    destroyCharts();

    const data = await api('/api/dashboard/timeline?days=14');
    if (!data) return;

    // ── Chart colors (dark theme) ───────────────────────────
    const colors = {
        success: '#22c55e',
        failed: '#ef4444',
        primary: '#6366f1',
        warning: '#f59e0b',
        grid: 'rgba(255,255,255,0.06)',
        text: '#888',
    };
    const chartDefaults = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                labels: { color: colors.text, font: { size: 11 } },
            }
        },
        scales: {
            x: {
                ticks: { color: colors.text, font: { size: 10 } },
                grid: { color: colors.grid },
            },
            y: {
                beginAtZero: true,
                ticks: { color: colors.text, font: { size: 10 } },
                grid: { color: colors.grid },
            }
        }
    };

    // ── 1. Ejecuciones por día (bar chart) ──────────────────
    const execCtx = document.getElementById('executionsChart');
    if (execCtx && data.daily?.length) {
        const days = data.daily.map(d => {
            const parts = d.day.split('-');
            return `${parts[2]}/${parts[1]}`;
        });
        chartInstances.executions = new Chart(execCtx, {
            type: 'bar',
            data: {
                labels: days,
                datasets: [
                    {
                        label: '✅ Completadas',
                        data: data.daily.map(d => d.completed),
                        backgroundColor: colors.success,
                        borderRadius: 4,
                    },
                    {
                        label: '❌ Fallidas',
                        data: data.daily.map(d => d.failed),
                        backgroundColor: colors.failed,
                        borderRadius: 4,
                    },
                ]
            },
            options: {
                ...chartDefaults,
                plugins: {
                    ...chartDefaults.plugins,
                    legend: {
                        ...chartDefaults.plugins.legend,
                        position: 'top',
                    }
                },
                scales: {
                    ...chartDefaults.scales,
                    x: {
                        ...chartDefaults.scales.x,
                        stacked: true,
                    },
                    y: {
                        ...chartDefaults.scales.y,
                        stacked: true,
                    }
                }
            }
        });
    }

    // ── 2. Tasa de éxito (doughnut) ─────────────────────────
    const successCtx = document.getElementById('successChart');
    if (successCtx && data.daily?.length) {
        const totalCompleted = data.daily.reduce((s, d) => s + d.completed, 0);
        const totalFailed = data.daily.reduce((s, d) => s + d.failed, 0);
        chartInstances.success = new Chart(successCtx, {
            type: 'doughnut',
            data: {
                labels: ['Completadas', 'Fallidas'],
                datasets: [{
                    data: [totalCompleted, totalFailed || 0],
                    backgroundColor: [colors.success, colors.failed],
                    borderWidth: 0,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: '65%',
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            color: colors.text,
                            font: { size: 11 },
                            padding: 12,
                        }
                    }
                }
            }
        });
    }

    // ── 3. Tools más usadas (horizontal bar) ────────────────
    const toolsCtx = document.getElementById('toolsChart');
    if (toolsCtx && data.tools?.length) {
        const toolLabels = {
            crm: 'CRM', invoice: 'Facturas', inventory: 'Inventario',
            notification: 'Notificaciones', system: 'Sistema',
            api_connector: 'API Connector', data_keeper: 'Data Keeper',
            autopilot: 'Autopilot', logic_gate: 'Logic Gate',
        };
        const labels = data.tools.map(t => toolLabels[t.tool] || t.tool);
        const values = data.tools.map(t => t.count);
        const barColors = ['#6366f1','#22c55e','#f59e0b','#ef4444','#8b5cf6','#06b6d4','#f97316','#84cc16','#a855f7','#ec4899'];
        chartInstances.tools = new Chart(toolsCtx, {
            type: 'bar',
            data: {
                labels,
                datasets: [{
                    label: 'Ejecuciones',
                    data: values,
                    backgroundColor: barColors.slice(0, labels.length),
                    borderRadius: 4,
                }]
            },
            options: {
                ...chartDefaults,
                indexAxis: 'y',
                plugins: {
                    ...chartDefaults.plugins,
                    legend: { display: false },
                }
            }
        });
    }
}

// ============================================
// Dashboard loader
// ============================================
async function loadDashboard() {
    const data = await api('/api/dashboard/stats');
    if (!data) return;
    const { stats, trial } = data;

    // Stats
    document.getElementById('statTotal').textContent = stats.total || 0;
    document.getElementById('statActive').textContent = stats.by_status?.active || 0;
    document.getElementById('statError').textContent = (stats.by_status?.failed || 0) + (stats.by_status?.error || 0);
    document.getElementById('statPaused').textContent = stats.by_status?.paused || 0;

    // Trial/license badge in header
    const headerBadge = document.getElementById('headerBadge');
    if (headerBadge && trial) {
        if (trial.is_trial) {
            headerBadge.innerHTML = `<span class="trial-badge-sm">⏳ Prueba: ${trial.days_left || 0}d</span>`;
        } else {
            headerBadge.innerHTML = `<span class="license-badge-sm">🔑 Licencia activa</span>`;
        }
    }

    // Recent executions with proper icons and time
    const list = document.getElementById('executionsList');
    if (stats.recent_executions?.length) {
        list.innerHTML = stats.recent_executions.map(e => `
            <div class="execution-item fade-in">
                <span class="execution-name">${e.name || 'Workflow'}</span>
                ${formatStatus(e.status)}
                <span class="execution-time">${formatDate(e.started_at || e.created_at)}</span>
            </div>
        `).join('');
    } else {
        list.innerHTML = '<p class="loading">Sin ejecuciones aún</p>';
    }

    // Suggestions from chat API (real templates)
    loadDashboardSuggestions();
}

async function loadDashboardSuggestions() {
    const grid = document.getElementById('suggestionsGrid');
    try {
        const res = await fetch('/api/workflows/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({text: 'sugerencias rápidas de automatización'})
        });
        const data = await res.json();
        if (data.suggestions?.length) {
            grid.innerHTML = data.suggestions.map(s => `
                <div class="suggestion-card" onclick="window.location.href='/chat?prefill=${encodeURIComponent(s.template_name.replace(/_/g,' '))}'">
                    <h3>📌 ${s.template_name.replace(/_/g,' ')}</h3>
                    <p>${s.description || 'Workflow automatizado'}</p>
                    <small>🔁 ${s.trigger.type} · ${s.steps.length} pasos</small>
                </div>
            `).join('');
            return;
        }
    } catch (e) { /* fallback */ }
    // Fallback suggestions
    const defaults = [
        { name: 'Backup automático de base de datos', desc: 'Respaldo diario de tu información' },
        { name: 'Alerta de stock bajo', desc: 'Notificación cuando el inventario baja' },
        { name: 'Email de cumpleaños', desc: 'Saludo automático a clientes' },
        { name: 'Facturación semanal', desc: 'Genera facturas cada semana' }
    ];
    grid.innerHTML = defaults.map(s => `
        <div class="suggestion-card" onclick="window.location.href='/chat?prefill=${encodeURIComponent(s.name)}'">
            <h3>📌 ${s.name}</h3>
            <p>${s.desc}</p>
            <small style="color:var(--text-muted)">Click para crear</small>
        </div>
    `).join('');
}

// ============================================
// Workflow list
// ============================================
async function loadWorkflowList() {
    const workflows = await api('/api/workflows');
    if (!workflows) return;
    const container = document.getElementById('workflowList');
    if (!workflows.length) {
        container.innerHTML = '<p class="loading">No hay workflows aún. <a href="/chat">Crea uno</a></p>';
        return;
    }
    container.innerHTML = `
        <div style="overflow-x:auto">
        <table class="table">
            <thead><tr><th>ID</th><th>Nombre</th><th>Estado</th><th>Trigger</th><th>Última ejecución</th><th>Acciones</th></tr></thead>
            <tbody>
            ${workflows.map(w => `
                <tr>
                    <td>${w.id}</td>
                    <td><a href="/workflows/${w.id}">${w.name || 'Sin nombre'}</a></td>
                    <td>${formatStatus(w.status)}</td>
                    <td style="color:var(--text-muted);font-size:.85rem">${w.trigger_type}</td>
                    <td style="color:var(--text-muted);font-size:.85rem">${formatDate(w.last_execution_at || w.updated_at)}</td>
                    <td>
                        <button onclick="toggleWorkflow(${w.id}, '${w.status}')" class="btn btn-sm">
                            ${w.status === 'active' ? '⏸ Pausar' : w.status === 'paused' ? '▶️ Reanudar' : '▶️ Activar'}
                        </button>
                        <button onclick="deleteWorkflow(${w.id})" class="btn btn-sm btn-danger">🗑</button>
                    </td>
                </tr>
            `).join('')}
            </tbody>
        </table></div>
    `;
}

async function toggleWorkflow(id, currentStatus) {
    const action = currentStatus === 'active' ? 'pause' : 'activate';
    const res = await api(`/api/workflows/${id}/${action}`, {method: 'POST'});
    if (res) showToast('Workflow actualizado', 'success');
    loadWorkflowList();
}

async function deleteWorkflow(id) {
    if (!confirm('¿Eliminar este workflow?')) return;
    const res = await api(`/api/workflows/${id}`, {method: 'DELETE'});
    if (res) showToast('Workflow eliminado', 'success');
    loadWorkflowList();
}

// ============================================
// Workflow detail
// ============================================
async function loadWorkflowDetail(workflowId) {
    const wf = await api(`/api/workflows/${workflowId}`);
    if (!wf) return;
    document.getElementById('wfName').textContent = wf.name || 'Sin nombre';
    document.getElementById('wfStatus').textContent = wf.status;
    document.getElementById('wfTrigger').textContent = `${wf.trigger_type}: ${JSON.stringify(wf.trigger_config)}`;
    document.getElementById('wfSteps').textContent = JSON.stringify(wf.steps, null, 2);
    const history = await api(`/api/workflows/${workflowId}/history`);
    if (history?.length) {
        document.getElementById('wfHistory').innerHTML = history.map(e => `
            <div class="execution-item">
                <span>#${e.id}</span>
                ${formatStatus(e.status)}
                <span style="color:var(--text-muted);font-size:.85rem">
                    ${e.duration_ms ? `${e.duration_ms}ms` : ''}
                    ${e.started_at ? `· ${formatDate(e.started_at)}` : ''}
                </span>
            </div>
        `).join('');
    }
}

// ============================================
// Settings (global, used by settings page)
// ============================================
async function loadSettingsGlobal() {
    const settings = await api('/api/settings');
    if (!settings) return;
    Object.entries(settings).forEach(([k, v]) => {
        const el = document.getElementById(`setting_${k}`);
        if (el) el.value = v || '';
    });
}

async function saveSettingsGlobal() {
    const data = {};
    document.querySelectorAll('[data-setting]').forEach(el => { data[el.dataset.setting] = el.value; });
    const res = await api('/api/settings', {method: 'PUT', body: JSON.stringify(data)});
    if (res !== null) showToast('Configuración guardada', 'success');
}

// ============================================
// Mobile nav toggle
// ============================================
document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.getElementById('navHamburger');
    const navLinks = document.getElementById('navLinks');
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('open');
        });
    }
});
