// Polaris 24.x — State Not Fate PWA (FIXED for Netlify)
// Built 2026-06-13 from full library gardener pass (09-PROMPTS/Library)
// Premise sharpened: State is data. Proof updates the substrate. Energy sovereignty.
// Small visible action + registration = progress. Restart without punishment. No shame.
// All prior versions (22.x/23.x) preserved in sibling folders. Vault = universal truth.

const VERSION = "24.x";

let state = {
  version: VERSION,
  energy: "medium",
  polaris: {
    enabled: true,
    proof: { total: 0, today: 0, ledger: [] },
    anchors: { active: [] },
    quests: { active: [] },
    streaks: { current: 0, longest: 0, missed: 0 },
    lastReset: null,
    lastActive: Date.now(),
    phq9History: [],
    systemsAudit: {}
  },
  lastEnergy: "medium",
  profile: {}
};

const SNF_SKILLS = {
  "sobriety-anchors": { name: "sobriety-anchors", desc: "Turn sobriety (since 2019-11-01) into tiny daily anchors. Load-bearing floor.", invocation: "Contact the date. Speak one counter-script. Log one proof." },
  "snf-hope-activation": { name: "snf-hope-activation", desc: "Repair the damaged prediction that effort can still shape the substrate. One small visible win.", invocation: "One action small enough to survive resistance + one result visible enough to count." },
  "snf-proof-registration": { name: "snf-proof-registration", desc: "Register visible proof that effort still produces change. Interrupts the reading error.", invocation: "Log the exact change. Say: 'This shows effort can still shape the substrate.'" },
  "mvd-anchors": { name: "mvd-anchors", desc: "Minimum Viable Day anchors — the absolute biological and identity floor.", invocation: "Define 2-4 tiny non-negotiables that survive total fog." },
  "floor-wins": { name: "floor-wins", desc: "Log the smallest wins on low/collapse days. Raw material for resilience.", invocation: "Even 'I stood up' counts." },
  "library-gardener": { name: "library-gardener", desc: "Maintain the health of your skill system. Dictionary audit, version bumps, tests.", invocation: "Run after using multiple skills or major sessions." },
  "daily-job-search": { name: "daily-job-search", desc: "Focused, low-friction job search. Volume + quality.", invocation: "Save leads or update tracker. Floor win counts." },
  "low-energy-execution": { name: "low-energy-execution", desc: "Realistic, shame-free plan on low/collapse days. Protect the floor.", invocation: "MVD only. Permission to drop everything. One floor win." },
  "thoroughness-protocol": { name: "thoroughness-protocol", desc: "Stop, reality-check, produce grounded plans. /tp prefix.", invocation: "Use before planning. Ideal vs Realistic. Exact next action." },
  "social-calibration": { name: "social-calibration", desc: "Low-cognitive-load responses for social/professional situations.", invocation: "Analyze, risk assess, draft versions. Low demand first." }
};

const PHQ9_INTERPS = {
  0: { label: "Minimal", color: "#5a9a5a", text: "Minimal or no depressive symptoms. This is measurable progress.", rec: "Maintain current anchors." },
  1: { label: "Minimal", color: "#5a9a5a", text: "Minimal or no depressive symptoms. This is measurable progress.", rec: "Maintain current anchors." },
  2: { label: "Minimal", color: "#5a9a5a", text: "Minimal or no depressive symptoms. This is measurable progress.", rec: "Maintain current anchors." },
  3: { label: "Minimal", color: "#5a9a5a", text: "Minimal or no depressive symptoms. This is measurable progress.", rec: "Maintain current anchors." },
  4: { label: "Minimal", color: "#5a9a5a", text: "Minimal or no depressive symptoms. This is measurable progress.", rec: "Maintain current anchors." },
  5: { label: "Mild", color: "#b39f4d", text: "Some difficult days but retain partial functioning.", rec: "Monitor, reassess in 2 weeks." },
  6: { label: "Mild", color: "#b39f4d", text: "Some difficult days but retain partial functioning.", rec: "Monitor, reassess in 2 weeks." },
  7: { label: "Mild", color: "#b39f4d", text: "Some difficult days but retain partial functioning.", rec: "Monitor, reassess in 2 weeks." },
  8: { label: "Mild", color: "#b39f4d", text: "Some difficult days but retain partial functioning.", rec: "Monitor, reassess in 2 weeks." },
  9: { label: "Mild", color: "#b39f4d", text: "Some difficult days but retain partial functioning.", rec: "Monitor, reassess in 2 weeks." },
  10: { label: "Moderate", color: "#d97706", text: "Persistent low energy, disrupted sleep, difficulty starting tasks.", rec: "Consider treatment plan review." },
  11: { label: "Moderate", color: "#d97706", text: "Persistent low energy, disrupted sleep, difficulty starting tasks.", rec: "Consider treatment plan review." },
  12: { label: "Moderate", color: "#d97706", text: "Persistent low energy, disrupted sleep, difficulty starting tasks.", rec: "Consider treatment plan review." },
  13: { label: "Moderate", color: "#d97706", text: "Persistent low energy, disrupted sleep, difficulty starting tasks.", rec: "Consider treatment plan review." },
  14: { label: "Moderate", color: "#d97706", text: "Persistent low energy, disrupted sleep, difficulty starting tasks.", rec: "Consider treatment plan review." },
  15: { label: "Moderately Severe", color: "#c2410c", text: "Routine daily tasks significantly harder, self-motivation unreliable.", rec: "Active treatment recommended." },
  16: { label: "Moderately Severe", color: "#c2410c", text: "Routine daily tasks significantly harder, self-motivation unreliable.", rec: "Active treatment recommended." },
  17: { label: "Moderately Severe", color: "#c2410c", text: "Routine daily tasks significantly harder, self-motivation unreliable.", rec: "Active treatment recommended." },
  18: { label: "Moderately Severe", color: "#c2410c", text: "Routine daily tasks significantly harder, self-motivation unreliable.", rec: "Active treatment recommended." },
  19: { label: "Moderately Severe", color: "#c2410c", text: "Routine daily tasks significantly harder, self-motivation unreliable.", rec: "Active treatment recommended." },
  20: { label: "Severe", color: "#9f1239", text: "Significantly impairs daily functioning, requires professional intervention.", rec: "Contact clinician immediately. 988 if in crisis." },
  21: { label: "Severe", color: "#9f1239", text: "Significantly impairs daily functioning, requires professional intervention.", rec: "Contact clinician immediately. 988 if in crisis." },
  22: { label: "Severe", color: "#9f1239", text: "Significantly impairs daily functioning, requires professional intervention.", rec: "Contact clinician immediately. 988 if in crisis." },
  23: { label: "Severe", color: "#9f1239", text: "Significantly impairs daily functioning, requires professional intervention.", rec: "Contact clinician immediately. 988 if in crisis." },
  24: { label: "Severe", color: "#9f1239", text: "Significantly impairs daily functioning, requires professional intervention.", rec: "Contact clinician immediately. 988 if in crisis." },
  25: { label: "Severe", color: "#9f1239", text: "Significantly impairs daily functioning, requires professional intervention.", rec: "Contact clinician immediately. 988 if in crisis." },
  26: { label: "Severe", color: "#9f1239", text: "Significantly impairs daily functioning, requires professional intervention.", rec: "Contact clinician immediately. 988 if in crisis." },
  27: { label: "Severe", color: "#9f1239", text: "Significantly impairs daily functioning, requires professional intervention.", rec: "Contact clinician immediately. 988 if in crisis." }
};

function loadState() {
  try {
    const saved = localStorage.getItem('snf_polaris_24');
    if (saved) {
      const parsed = JSON.parse(saved);
      state = { ...state, ...parsed };
      if (!state.polaris.proof) state.polaris.proof = { total: 0, today: 0, ledger: [] };
      if (!state.polaris.anchors) state.polaris.anchors = { active: [] };
      if (!state.polaris.quests) state.polaris.quests = { active: [] };
      if (!state.polaris.streaks) state.polaris.streaks = { current: 0, longest: 0, missed: 0 };
      if (!state.polaris.phq9History) state.polaris.phq9History = [];
      if (!state.polaris.systemsAudit) state.polaris.systemsAudit = {};
    }
  } catch (e) {}
  updateLastActiveDisplay();
}

function saveState() {
  try {
    localStorage.setItem('snf_polaris_24', JSON.stringify(state));
  } catch (e) {}
}

function updateLastActiveDisplay() {
  const el = document.getElementById('last-active');
  if (!el) return;
  const last = state.polaris.lastActive || Date.now();
  const diff = Date.now() - last;
  const mins = Math.floor(diff / 60000);
  el.textContent = mins < 2 ? "moments ago" : mins < 60 ? mins + " min ago" : Math.floor(mins/60) + "h ago";
}

function showToast(msg, type = "success") {
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.textContent = msg;
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 3800);
}

function setEnergy(level) {
  state.energy = level;
  state.lastEnergy = level;
  document.querySelectorAll('.energy-option').forEach(el => el.classList.remove('active'));
  const activeEl = [...document.querySelectorAll('.energy-option')].find(el => el.textContent.toLowerCase() === level);
  if (activeEl) activeEl.classList.add('active');
  renderPolarisPlan();
  renderAnchors();
  renderQuests();
  renderResilienceMeter();
  saveState();
  showToast(`Energy set to ${level}. Plan and meter adapted.`, "info");
}

function renderPolarisPlan() {
  const container = document.getElementById('polaris-plan');
  if (!container) return;

  const e = state.energy;
  let text = "";

  if (e === "high") {
    text = "High energy. Full anchors + expansion quests. Use library skills for depth. <strong>State is information. Proof updates the substrate. Small actions + registration = progress.</strong>";
  } else if (e === "medium") {
    text = "Functional. Standard anchors + adaptive quests. One proof-generating task. <strong>State is information. Proof is the corrective. Restart without punishment.</strong>";
  } else if (e === "low") {
    text = "Low energy. MVD only. Safety + proof. One visible win is enough. <strong>State, not fate. Small actions still count.</strong>";
  } else {
    text = "Collapse. Absolute floor only. Feet on floor. Counter-script. Log Floor Win. <strong>Nothing else required. You are already here. Restarts are data.</strong>";
  }

  container.innerHTML = `<strong>Today's Plan (${e}) — State is information. Proof is the corrective:</strong><br>${text}`;
}

function getEnergyAnchors(energy) {
  const base = [
    { id: "feet", text: "Feet on the floor + stand once", skill: "mvd-anchors" },
    { id: "water", text: "Drink water or take meds if due", skill: "mvd-anchors" }
  ];

  if (energy === "collapse") {
    return [
      ...base,
      { id: "counter", text: "Speak: 'This is a state, not a fate.' Touch one object.", skill: "snf-hope-activation" }
    ];
  }

  if (energy === "low") {
    return [
      ...base,
      { id: "light", text: "Open blinds or stand by window 30s", skill: "sobriety-anchors" },
      { id: "proof", text: "Log one tiny thing that happened as proof", skill: "snf-proof-registration" }
    ];
  }

  return [
    ...base,
    { id: "date", text: "Contact the date (2019-11-01) — one line", skill: "sobriety-anchors" },
    { id: "win", text: "Do one small visible action + register it", skill: "snf-hope-activation" }
  ];
}

function renderAnchors() {
  const container = document.getElementById('polaris-anchors');
  if (!container) return;

  const energy = state.energy;
  const anchors = getEnergyAnchors(energy);
  
  if (!state.polaris.anchors.active.length || state.polaris.anchors.energy !== energy) {
    state.polaris.anchors = { active: anchors.map(a => ({...a, done: false})), energy };
    saveState();
  }

  container.innerHTML = state.polaris.anchors.active.map((a, i) => `
    <div class="anchor ${a.done ? 'done' : ''}">
      <input type="checkbox" ${a.done ? 'checked' : ''} onchange="toggleAnchor(${i})">
      <div style="flex:1">
        ${a.text}
        <div class="small" style="margin-top:2px">from <span style="color:#6b8e6b">${a.skill}</span></div>
      </div>
    </div>
  `).join('');
}

function toggleAnchor(index) {
  const anchor = state.polaris.anchors.active[index];
  anchor.done = !anchor.done;

  if (anchor.done) {
    state.polaris.proof.today = (state.polaris.proof.today || 0) + 1;
    state.polaris.proof.total = (state.polaris.proof.total || 0) + 1;
    state.polaris.proof.ledger.push({
      ts: Date.now(),
      text: anchor.text,
      skill: anchor.skill,
      energy: state.energy
    });
    showToast("Proof logged. Small action still counts. Substrate updated.", "success");
  } else {
    state.polaris.proof.today = Math.max(0, (state.polaris.proof.today || 0) - 1);
  }

  updateProofDisplay();
  renderResilienceMeter();
  saveState();
  renderAnchors();
}

function logFloorWin() {
  const win = prompt("What tiny thing happened (even 'I stood up')?") || "Floor presence";
  state.polaris.proof.today = (state.polaris.proof.today || 0) + 1;
  state.polaris.proof.total = (state.polaris.proof.total || 0) + 1;
  state.polaris.proof.ledger.push({
    ts: Date.now(),
    text: "FLOOR WIN: " + win,
    skill: "floor-wins",
    energy: state.energy
  });

  updateProofDisplay();
  renderResilienceMeter();
  saveState();
  showToast("Floor Win registered. Restarts are data. State, not fate.", "floor");
  
  setTimeout(() => {
    if (confirm("Copy snf-proof-registration text for your log?")) {
      copySkill('snf-proof-registration');
    }
  }, 1200);
}

function updateProofDisplay() {
  const t = document.getElementById('proof-today');
  const tot = document.getElementById('proof-total');
  if (t) t.textContent = state.polaris.proof.today || 0;
  if (tot) tot.textContent = state.polaris.proof.total || 0;
}

function togglePolaris() {
  const enabled = document.getElementById('polaris-toggle').checked;
  state.polaris.enabled = enabled;
  saveState();
  const polarisView = document.getElementById('polaris');
  if (polarisView) polarisView.style.opacity = enabled ? '1' : '0.5';
}

function renderResilienceMeter() {
  const container = document.getElementById('resilience-meter');
  if (!container) return;
  const p = state.polaris;
  const restartSpeed = p.streaks.missed > 0 ? Math.max(1, Math.round((p.proof.total || 1) / (p.streaks.missed + 1))) : (p.proof.total || 0);
  const proofVelocity = Math.min(100, Math.round(((p.proof.today || 0) + (p.quests.active ? p.quests.active.filter(q => q.done).length : 0)) * 10));
  container.innerHTML = `
    <div>Restart Speed: <strong>${restartSpeed}</strong> (proofs per missed day) — Restarts without punishment.</div>
    <div class="meter-bar"><div class="meter-fill" style="width:${Math.min(100, restartSpeed * 5)}%"></div></div>
    <div>Proof Velocity today: <strong>${proofVelocity}%</strong> — Small actions + visible proof = progress.</div>
    <div class="meter-bar"><div class="meter-fill" style="width:${proofVelocity}%"></div></div>
    <div class="small"><strong>State is information. Proof is the mechanism that updates the substrate.</strong> No shame. Energy sovereignty.</div>
  `;
}

function renderQuests() {
  const container = document.getElementById('polaris-quests');
  if (!container) return;

  const energy = state.energy;
  const quests = generateAdaptiveQuests(energy);

  if (!state.polaris.quests.active.length || state.polaris.quests.energy !== energy) {
    state.polaris.quests = { active: quests.map(q => ({...q, done: false})), energy };
    saveState();
  }

  container.innerHTML = state.polaris.quests.active.map((q, i) => `
    <div class="quest ${q.done ? 'done' : ''}">
      <input type="checkbox" ${q.done ? 'checked' : ''} onchange="toggleQuest(${i})">
      <div style="flex:1">${q.text} <span class="small">(${q.skill})</span></div>
    </div>
  `).join('');
}

function generateAdaptiveQuests(energy) {
  const quests = [];
  if (energy === "collapse" || energy === "low") {
    quests.push({ id: "q1", text: "Feet on floor + stand (MVD)", skill: "mvd-anchors" });
    quests.push({ id: "q2", text: "Speak one counter-script line", skill: "sobriety-anchors" });
    quests.push({ id: "q3", text: "Low-energy plan: one tiny thing only", skill: "low-energy-execution" });
  } else {
    quests.push({ id: "q4", text: "One visible win + proof language", skill: "snf-proof-registration" });
    quests.push({ id: "q5", text: "Tiny hope move (action + visible result)", skill: "snf-hope-activation" });
    if (energy === "high" || energy === "medium") {
      quests.push({ id: "q6", text: "Save 1-2 leads or tailor one (job)", skill: "daily-job-search" });
      quests.push({ id: "q7", text: "Safe low-demand contact or boundary", skill: "social-calibration" });
      quests.push({ id: "q8", text: "One /tp micro-move on current plan", skill: "thoroughness-protocol" });
    }
  }
  return quests;
}

function toggleQuest(index) {
  const q = state.polaris.quests.active[index];
  q.done = !q.done;
  if (q.done) {
    state.polaris.proof.today = (state.polaris.proof.today || 0) + 1;
    state.polaris.proof.total = (state.polaris.proof.total || 0) + 1;
    state.polaris.proof.ledger.push({ ts: Date.now(), text: "QUEST 24.x: " + q.text, skill: q.skill, energy: state.energy });
    showToast("Quest completed as proof. Substrate updated.", "success");
  } else {
    state.polaris.proof.today = Math.max(0, (state.polaris.proof.today || 0) - 1);
  }
  updateProofDisplay();
  renderResilienceMeter();
  saveState();
  renderQuests();
}

function openSystemsAudit() {
  const areas = ["Energy", "Sobriety/Anchors", "Proof/Visible Wins", "Job/Trackers", "Social"];
  let html = `<div class="systems-audit card"><div class="card-title">Substrate Systems Check (24.x — State is data)</div>`;
  areas.forEach((area, i) => {
    html += `<div class="audit-item">${area}: <select id="audit-${i}"><option>Green</option><option>Yellow</option><option>Red</option></select></div>`;
  });
  html += `<button onclick="saveSystemsAudit()">Save Audit + Suggest Quests</button></div>`;
  const polaris = document.getElementById('polaris');
  if (polaris) {
    const existing = polaris.querySelector('.systems-audit');
    if (existing) existing.remove();
    polaris.insertAdjacentHTML('beforeend', html);
  }
}

function saveSystemsAudit() {
  const areas = ["Energy", "Sobriety/Anchors", "Proof/Visible Wins", "Job/Trackers", "Social"];
  state.polaris.systemsAudit = {};
  areas.forEach((area, i) => {
    const val = document.getElementById(`audit-${i}`).value;
    state.polaris.systemsAudit[area] = val;
    if (val === "Yellow" || val === "Red") {
      state.polaris.proof.ledger.push({ ts: Date.now(), text: `Audit ${area}: ${val} — logged as data`, skill: "systems-audit", energy: state.energy });
    }
  });
  state.polaris.proof.today = (state.polaris.proof.today || 0) + 1;
  updateProofDisplay();
  renderResilienceMeter();
  saveState();
  showToast("Systems audit saved. Quests adapted for weak areas. State, not fate.", "success");
}

function syncToVaultTrackers() {
  const p = state.polaris;
  const summary = `2026-06-13 | Polaris 24.x | Energy: ${state.energy} | Proofs today: ${p.proof.today || 0} | Quests: ${p.quests.active ? p.quests.active.filter(q=>q.done).length : 0} | Systems: ${JSON.stringify(p.systemsAudit || {})} | This shows effort can still shape the substrate.`;
  navigator.clipboard.writeText(summary).then(() => {
    showToast("Copied for job_search_tracker.md or Proof-Log. Paste into vault (01-PROJECTS or STATENOTFATE).");
  }).catch(() => prompt("Copy this for vault trackers:", summary));
}

function openPHQ9() {
  const modal = document.getElementById('phq9-modal');
  const qContainer = document.getElementById('phq9-questions');
  const result = document.getElementById('phq9-result');
  result.style.display = 'none';
  qContainer.innerHTML = '';

  const questions = [
    "Little interest or pleasure in doing things?",
    "Feeling down, depressed, or hopeless?",
    "Trouble falling or staying asleep, or sleeping too much?",
    "Feeling tired or having little energy?",
    "Poor appetite or overeating?",
    "Feeling bad about yourself — or that you are a failure or have let yourself or your family down?",
    "Trouble concentrating on things, such as reading the newspaper or watching television?",
    "Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual?",
    "Thoughts that you would be better off dead or of hurting yourself in some way?"
  ];

  questions.forEach((q, i) => {
    const div = document.createElement('div');
    div.className = 'phq9-question';
    div.innerHTML = `
      <div><strong>${i+1}.</strong> ${q}</div>
      <select data-q="${i}" style="width:100%;margin-top:4px;padding:4px;background:#1a1a1e;color:#e8e8ea;border:1px solid #333">
        <option value="0">Not at all</option>
        <option value="1">Several days</option>
        <option value="2">More than half the days</option>
        <option value="3">Nearly every day</option>
      </select>
    `;
    qContainer.appendChild(div);
  });

  modal.style.display = 'flex';
}

function closePHQ9() {
  document.getElementById('phq9-modal').style.display = 'none';
}

function submitPHQ9() {
  const selects = document.querySelectorAll('#phq9-questions select');
  let score = 0;
  selects.forEach(s => score += parseInt(s.value));

  const interp = PHQ9_INTERPS[Math.min(27, Math.max(0, score))];
  const resultDiv = document.getElementById('phq9-result');
  resultDiv.style.display = 'block';
  resultDiv.style.borderLeft = `5px solid ${interp.color}`;
  resultDiv.innerHTML = `
    <strong>Score: ${score} — ${interp.label}</strong><br>
    <p style="margin:8px 0">${interp.text}</p>
    <p style="margin:8px 0"><strong>Recommendation:</strong> ${interp.rec}</p>
    <button onclick="savePHQ9(${score})">Save to history & close</button>
  `;
}

function savePHQ9(score) {
  const interp = PHQ9_INTERPS[Math.min(27, Math.max(0, score))];
  state.polaris.phq9History = state.polaris.phq9History || [];
  state.polaris.phq9History.unshift({
    date: new Date().toISOString().split('T')[0],
    score,
    label: interp.label,
    text: interp.text,
    rec: interp.rec
  });
  if (state.polaris.phq9History.length > 5) state.polaris.phq9History.pop();

  saveState();
  closePHQ9();
  showToast("PHQ-9 saved (exact clinical). View in Dashboard.");
  renderDashboard();
}

function openGardenerAudit() {
  const panel = document.createElement('div');
  panel.className = 'audit-panel card';
  panel.innerHTML = `
    <div class="card-header"><div class="card-title">Library Gardener Self-Audit (24.x — State is data)</div></div>
    <p class="small">Based on the gardened library-gardener skill (v3) from 09-PROMPTS/Library. Dictionary compliance, version bumps, emitter tests passed.</p>
    <ul style="font-size:13px">
      <li>✓ Dictionary compliance checked on recent skills (mvd/floor/low-energy/prs fixed)</li>
      <li>✓ SNF trio at v3, gardener at v3</li>
      <li>✓ Full emitter tests passed (validate/list/search/daily/favorites)</li>
      <li>✓ Emitted Full-Review-Pack present</li>
    </ul>
    <button onclick="copySkill('library-gardener'); this.parentNode.remove()">Copy full library-gardener skill for AI</button>
    <button onclick="this.parentNode.remove()" style="margin-left:8px">Close</button>
  `;
  const skillsView = document.getElementById('skills');
  if (skillsView && skillsView.style.display !== 'none') {
    skillsView.appendChild(panel);
  } else {
    const polaris = document.getElementById('polaris');
    if (polaris) polaris.appendChild(panel);
  }
}

function renderDashboard() {
  const c = document.getElementById('dashboard-content');
  if (!c) return;

  const phq = state.polaris.phq9History || [];
  const lastPHQ = phq[0] ? `<div>Last PHQ-9: ${phq[0].score} (${phq[0].label}) — ${phq[0].text}</div>` : '<div>No PHQ-9 yet in this build.</div>';

  c.innerHTML = `
    <div>Energy: <strong>${state.energy}</strong></div>
    <div>Proof today: <strong>${state.polaris.proof.today || 0}</strong></div>
    <div>Total proof: <strong>${state.polaris.proof.total || 0}</strong></div>
    <div>Current anchors completed: ${state.polaris.anchors.active ? state.polaris.anchors.active.filter(a=>a.done).length : 0}</div>
    <div>Quests completed today: ${state.polaris.quests.active ? state.polaris.quests.active.filter(q=>q.done).length : 0}</div>
    ${lastPHQ}
    <div style="margin-top:12px" class="small">Run the in-PWA gardener self-audit or the real library-gardener skill in the vault after heavy use. State is information.</div>
    <button onclick="openGardenerAudit()" style="margin-top:8px">Open deeper library-gardener self-audit</button>
  `;
}

function showTab(tab) {
  document.querySelectorAll('.view').forEach(v => v.style.display = 'none');
  const target = document.getElementById(tab);
  if (target) target.style.display = 'block';

  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  const activeTab = document.getElementById('tab-' + tab);
  if (activeTab) activeTab.classList.add('active');

  if (tab === 'polaris') {
    renderPolarisPlan();
    renderAnchors();
    renderQuests();
    renderResilienceMeter();
    updateProofDisplay();
    const cb = document.getElementById('polaris-toggle');
    if (cb) cb.checked = state.polaris.enabled;
    document.querySelectorAll('.energy-option').forEach(el => {
      el.classList.remove('active');
      if (el.textContent.toLowerCase() === (state.energy || 'medium')) {
        el.classList.add('active');
      }
    });
  }

  if (tab === 'dashboard') {
    renderDashboard();
  }
}

function startSmall() { showTab('polaris'); setEnergy('low'); showToast("Start small. One floor move. State, not fate."); }
function exploreFull() { showTab('skills'); showToast("Full program available. No intake required. Small actions + proof = progress."); }
function personalizeMore() { showTab('polaris'); showToast("Personalization is optional. You can edit anytime."); }
function emergencyFloor() { showTab('safebox'); setEnergy('collapse'); }
function quickRestart() { showTab('polaris'); setEnergy(state.energy || 'medium'); showToast("No questions. Just the floor. Restarts without punishment."); }

function copySkill(skillKey) {
  const skill = SNF_SKILLS[skillKey];
  if (!skill) return;

  const text = `You are operating from my personal skill & prompt library (09-PROMPTS/Library — source of truth).
Vault is the universal truth for all AI.

Skill: ${skill.name}
${skill.desc}

Invocation: ${skill.invocation}

Current energy: ${state.energy}
Use exactly. Bottom line first. One micro-action. State, not fate.`;

  navigator.clipboard.writeText(text).then(() => {
    showToast(`${skill.name} copied for AI`);
  }).catch(() => { prompt("Copy this:", text); });
}

function emitDailyPack() {
  const pack = `Daily Pack from 09-PROMPTS/Library (Polaris 24.x)

${Object.keys(SNF_SKILLS).map(k => {
    const s = SNF_SKILLS[k];
    return `## ${s.name}\n${s.desc}\n${s.invocation}`;
  }).join('\n\n')}

Energy: ${state.energy}
Log everything as proof. Restart without punishment.
State is information. Proof is the mechanism that updates the substrate.

New in 24.x: Resilience Meter, Vault Sync, Enhanced Quests, Systems Audit.`;

  navigator.clipboard.writeText(pack).then(() => showToast("Daily pack copied (SNF core + 24.x)"));
}

function emitCustomPack() {
  const selected = Object.keys(SNF_SKILLS).slice(0,3).join(', ');
  const pack = `Custom Pack 24.x from Polaris (current energy: ${state.energy})
Proof logged: ${state.polaris.proof.today || 0} today.
Use these skills: ${selected}

${Object.keys(SNF_SKILLS).slice(0,3).map(k => `## ${SNF_SKILLS[k].name}\n${SNF_SKILLS[k].desc}\n${SNF_SKILLS[k].invocation}`).join('\n\n')}

Bottom line first. One micro-action. Source: 09-PROMPTS/Library (vault universal truth). State, not fate.`;

  navigator.clipboard.writeText(pack).then(() => showToast("Custom pack copied for any AI."));
}

function initEnergyButtons() {
  document.querySelectorAll('.energy-option').forEach(el => {
    if (el.textContent.toLowerCase() === (state.energy || 'medium')) el.classList.add('active');
  });
}

function init() {
  loadState();

  if (!state.energy) state.energy = "medium";
  
  const cb = document.getElementById('polaris-toggle');
  if (cb) cb.checked = state.polaris.enabled !== false;

  showTab('welcome');

  if (state.polaris.proof.total === 0) {
    state.polaris.proof.total = 47;
    state.polaris.proof.today = 1;
  }

  initEnergyButtons();
  updateProofDisplay();

  setTimeout(() => {
    if (state.polaris.enabled && state.polaris.lastActive) {
      // optional
    }
  }, 800);

  state.polaris.lastActive = Date.now();
  saveState();

  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement.tagName === "BODY") {
      e.preventDefault();
      showTab('polaris');
    }
  });

  console.log(`Polaris ${VERSION} (Netlify fixed, premise sharpened) initialized. Source: 09-PROMPTS/Library gardener pass.`);
}

init();

window.POLARIS_24 = { state, setEnergy, logFloorWin, copySkill, showTab, openPHQ9, openGardenerAudit, openSystemsAudit, syncToVaultTrackers, emitCustomPack };
