// Workflow Determinista — Editor JS
let stepCounter = 0;

function addStep(stepData) {
    stepCounter++;
    const template = document.getElementById('stepTemplate');
    const clone = template.content.cloneNode(true);
    const card = clone.querySelector('.step-card');
    card.dataset.stepId = stepCounter;
    card.querySelector('.step-num').textContent = stepCounter;
    if (stepData) {
        card.querySelector('.step-tool').value = stepData.tool || 'crm';
        card.querySelector('.step-action').value = stepData.action || '';
        card.querySelector('.step-params').value = JSON.stringify(stepData.params || {}, null, 2);
        card.querySelector('.step-condition').value = stepData.condition || '';
    }
    document.getElementById('stepsContainer').appendChild(card);
}

async function saveWorkflow() {
    const wfId = new URLSearchParams(window.location.search).get('wf');
    const steps = [];
    document.querySelectorAll('.step-card').forEach(card => {
        const paramsText = card.querySelector('.step-params').value.trim();
        let params = {};
        try { params = paramsText ? JSON.parse(paramsText) : {}; } catch(e) { params = {_error: 'JSON inválido'}; }
        steps.push({
            id: parseInt(card.dataset.stepId),
            tool: card.querySelector('.step-tool').value,
            action: card.querySelector('.step-action').value,
            params: params,
            condition: card.querySelector('.step-condition').value || undefined,
        });
    });
    const data = {
        trigger_type: document.getElementById('triggerType').value,
        trigger_config: JSON.parse(document.getElementById('triggerConfig').value || '{}'),
        steps: steps,
        name: document.getElementById('wfNameInput')?.value || 'Workflow sin nombre',
    };
    if (wfId) {
        await api(`/api/workflows/${wfId}`, {method: 'PUT', body: JSON.stringify(data)});
        alert('Workflow actualizado');
    } else {
        const result = await api('/api/workflows', {method: 'POST', body: JSON.stringify(data)});
        if (result?.id) window.location.href = `/editor?wf=${result.id}`;
        else alert('Error: ' + (result?.error || 'desconocido'));
    }
}

async function testWorkflow() {
    const wfId = new URLSearchParams(window.location.search).get('wf');
    if (!wfId) { alert('Guarda el workflow primero'); return; }
    const result = await api(`/api/workflows/${wfId}/retry`, {method: 'POST'});
    alert(`Resultado: ${result?.status || 'error'}`);
}

// Cargar workflow existente
document.addEventListener('DOMContentLoaded', async () => {
    const wfId = new URLSearchParams(window.location.search).get('wf');
    if (!wfId) { addStep(); return; }
    const wf = await api(`/api/workflows/${wfId}`);
    if (!wf) { addStep(); return; }
    document.getElementById('triggerType').value = wf.trigger_type || 'event';
    document.getElementById('triggerConfig').value = JSON.stringify(wf.trigger_config || {});
    const header = document.querySelector('.page-header h1');
    if (header) header.textContent = `✏️ Editando: ${wf.name || 'Sin nombre'}`;
    (wf.steps || []).forEach(s => addStep(s));
    if (!wf.steps?.length) addStep();
});
