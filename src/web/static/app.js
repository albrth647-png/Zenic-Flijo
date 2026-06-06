// Workflow Determinista — App JS
async function api(path, options = {}) {
    const res = await fetch(path, {
        headers: {'Content-Type': 'application/json', ...options.headers},
        ...options
    });
    if (res.status === 401) { window.location.href = '/login'; return null; }
    return res.json();
}

async function loadDashboard() {
    const data = await api('/api/dashboard/stats');
    if (!data) return;
    const { stats, trial } = data;
    document.getElementById('statTotal').textContent = stats.total || 0;
    document.getElementById('statActive').textContent = stats.by_status?.active || 0;
    document.getElementById('statError').textContent = (stats.by_status?.failed || 0) + (stats.by_status?.error || 0);
    document.getElementById('statPaused').textContent = stats.by_status?.paused || 0;
    const list = document.getElementById('executionsList');
    if (stats.recent_executions?.length) {
        list.innerHTML = stats.recent_executions.map(e => `
            <div class="execution-item">
                <span>${e.name}</span>
                <span class="execution-status ${e.status}">${e.status === 'completed' ? '✅' : '❌'} ${e.status}</span>
                <span style="color:var(--text-muted);font-size:.85rem">${e.started_at ? new Date(e.started_at).toLocaleDateString() : ''}</span>
            </div>
        `).join('');
    } else {
        list.innerHTML = '<p class="loading">Sin ejecuciones aún</p>';
    }
    const suggestions = ['Backup automático de base de datos', 'Alerta de stock bajo', 'Email de cumpleaños', 'Facturación semanal'];
    document.getElementById('suggestionsGrid').innerHTML = suggestions.map(s => `
        <div class="suggestion-card" onclick="window.location.href='/chat'">
            <h3>${s}</h3>
            <small style="color:var(--text-muted)">Click para crear</small>
        </div>
    `).join('');
}

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
            <thead><tr><th>ID</th><th>Nombre</th><th>Estado</th><th>Trigger</th><th>Acciones</th></tr></thead>
            <tbody>
            ${workflows.map(w => `
                <tr>
                    <td>${w.id}</td>
                    <td><a href="/workflows/${w.id}">${w.name || 'Sin nombre'}</a></td>
                    <td><span class="execution-status ${w.status}">${w.status}</span></td>
                    <td style="color:var(--text-muted);font-size:.85rem">${w.trigger_type}</td>
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
    await api(`/api/workflows/${id}/${action}`, {method: 'POST'});
    loadWorkflowList();
}

async function deleteWorkflow(id) {
    if (!confirm('¿Eliminar este workflow?')) return;
    await api(`/api/workflows/${id}`, {method: 'DELETE'});
    loadWorkflowList();
}

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
                <span class="execution-status ${e.status}">${e.status}</span>
                <span style="color:var(--text-muted);font-size:.85rem">
                    ${e.duration_ms ? `${e.duration_ms}ms` : ''}
                    ${e.started_at ? `· ${new Date(e.started_at).toLocaleString()}` : ''}
                </span>
            </div>
        `).join('');
    }
}

async function loadSettings() {
    const settings = await api('/api/settings');
    if (!settings) return;
    Object.entries(settings).forEach(([k, v]) => {
        const el = document.getElementById(`setting_${k}`);
        if (el) el.value = v || '';
    });
}

async function saveSettings() {
    const data = {};
    document.querySelectorAll('[data-setting]').forEach(el => { data[el.dataset.setting] = el.value; });
    await api('/api/settings', {method: 'PUT', body: JSON.stringify(data)});
    alert('Configuración guardada');
}
