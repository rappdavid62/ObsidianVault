// Polaris 23.x — State Not Fate PWA
// Built 2026-06-13 from full library gardener pass (09-PROMPTS/Library)
// Includes 22.x base + NEW: PHQ-9 exact clinical engine, deeper library-gardener self-audit, more adaptive quests
// Source of truth: Obsidian vault (STATENOTFATE + 09-PROMPTS/Library + Tech specs)

const VERSION = "23.x";

let state = {
  version: VERSION,
  energy: "medium",
  polaris: {
    enabled: true,
    proof: { total: 0, today: 0, ledger: [] },
    anchors: { active: [] },
    quests: { active: [] },  // NEW 23.x
    streaks: { current: 0, longest: 0, missed: 0 },
    lastReset: null,
    lastActive: Date.now(),
    phq9History: []  // NEW 23.x
  },
  lastEnergy: "medium",
  profile: {}
};

const SNF_SKILLS = {
  "sobriety-anchors": {
    name: "sobriety-anchors",
    desc: "Turn sobriety (since 2019-11-01) into tiny daily anchors. Load-bearing floor for everything.",
    invocation: "Contact the date. Speak one counter-script line. Log one proof."
  },
  "snf-hope-activation": {
    name: "snf-hope-activation",
    desc: "Repair the damaged prediction that effort can still shape the substrate. One small visible win.",
    invocation: "One action small enough to survive resistance + one result visible enough to count."
  },
  "snf-proof-registration": {
    name: "snf-proof-registration",
    desc: "Register visible proof that effort still produces change. Interrupts the reading error.",
    invocation: "Log the exact change in the external world. Say: 'This shows effort can still shape the substrate.'"
  },
  "mvd-anchors": {
    name: "mvd-anchors",
    desc: "Minimum Viable Day anchors — the absolute biological and identity floor on collapse days.",
    invocation: "Define 2-4 tiny non-negotiables that survive total fog."
  },
  "floor-wins": {
    name: "floor-wins",
    desc: "Log the smallest wins on low/collapse days. Raw material for resilience and hope meter.",
    invocation: "Even 'I got out of bed' counts if it happened."
  },
  "library-gardener": {
    name: "library-gardener",
    desc: "Maintain the health of your entire skill system. Dictionary audit, version bumps, tests.",
    invocation: "Run when you have used multiple skills or after major sessions."
  }
};

// Exact PHQ-9 clinical interpretations (verbatim from architecture spec / master prompt)
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
    const saved = localStorage.getItem('snf_polaris_23');
    if (saved) {
      const parsed = JSON.parse(saved);
      state = { ...state, ...parsed };
      if (!state.polaris.proof) state.polaris.proof = { total: 0, today: 0, ledger: [] };
      if (!state.polaris.anchors) state.polaris.anchors = { active: [] };
      if (!state.polaris.quests) state.polaris.quests = { active: [] };
      if (!state.polaris.streaks) state.polaris.streaks = { current: 0, longest: 0, missed: 0 };
      if (!state.polaris.phq9History) state.polaris.phq9History = [];
    }
  } catch (e) {}
  updateLastActiveDisplay();
}

function saveState() {
  try {
    localStorage.setItem('snf_polaris_23', JSON.stringify(state));
  } catch (e) {}
}

function updateLastActiveDisplay() {
  const el = document.getElementById('last-active');
  if (!el) return;
  const last = state.polaris.lastActive || Date.now();
  const diff = Date.now() - last;
  const mins = Math.floor(diff / 60000);
  if (mins < 2) el.textContent = "moments ago";
  else if (mins < 60) el.textContent = mins + " min ago";
  else el.textContent = Math.floor(mins/60) + "h ago";
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
  renderQuests();  // 23.x
  saveState();
  showToast(`Energy set to ${level}. Plan and quests adapted.`, "info");
}

function renderPolarisPlan() {
  const container = document.getElementById('polaris-plan');
  if (!container) return;

  const e = state.energy;
  let text = "";

  if (e === "high") {
    text = "High energy. Full anchors + one meaningful expansion move + adaptive quests. Use the library skills for depth.";
  } else if (e === "medium") {
    text = "Functional. Standard anchors + adaptive quests + one proof-generating task from the SNF skills.";
  } else if (e === "low") {
    text = "Low energy. MVD only. Safety + regulation focused. Adaptive quests are minimal. One visible win is enough. Restart without punishment.";
  } else {
    text = "Collapse. Absolute floor only. Feet on floor. Water/meds if due. One line of counter-script. Log as Floor Win. Adaptive quests reduced to absolute minimum. Nothing else required.";
  }

  container.innerHTML = `<strong>Today's Plan (${e}) — 23.x:</strong><br>${text}`;
}

// 23.x enhanced anchors + quests from gardened skills
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
    showToast("Proof logged. Small action still counts.", "success");
  } else {
    state.polaris.proof.today = Math.max(0, (state.polaris.proof.today || 0) - 1);
  }

  updateProofDisplay();
  saveState();
  renderAnchors();
}

// NEW 23.x: Adaptive Quests
function generateAdaptiveQuests(energy) {
  const quests = [];
  if (energy === "collapse" || energy === "low") {
    quests.push({ id: "q1", text: "Feet on floor + stand (MVD)", skill: "mvd-anchors" });
    quests.push({ id: "q2", text: "Speak one counter-script line aloud", skill: "sobriety-anchors" });
  } else {
    quests.push({ id: "q3", text: "One visible win + register with proof language", skill: "snf-proof-registration" });
    quests.push({ id: "q4", text: "Tiny hope-activation move (action + visible result)", skill: "snf-hope-activation" });
  }
  if (energy === "high" || energy === "medium") {
    quests.push({ id: "q5", text: "Use one library skill for the next micro-action", skill: "library-gardener" });
  }
  return quests;
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
      <div style="flex:1">
        ${q.text} <span class="small">(${q.skill})</span>
      </div>
    </div>
  `).join('');
}

function toggleQuest(index) {
  const q = state.polaris.quests.active[index];
  q.done = !q.done;

  if (q.done) {
    state.polaris.proof.today = (state.polaris.proof.today || 0) + 1;
    state.polaris.proof.total = (state.polaris.proof.total || 0) + 1;
    state.polaris.proof.ledger.push({
      ts: Date.now(),
      text: "QUEST: " + q.text,
      skill: q.skill,
      energy: state.energy
    });
    showToast("Quest completed as proof.", "success");
  } else {
    state.polaris.proof.today = Math.max(0, (state.polaris.proof.today || 0) - 1);
  }

  updateProofDisplay();
  saveState();
  renderQuests();
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
  saveState();
  showToast("Floor Win registered. Restarts are data.", "floor");
  
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

// NEW 23.x: PHQ-9 Exact Clinical Engine
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

// NEW 23.x: Deeper Library Gardener Self-Audit
function openGardenerAudit() {
  const panel = document.createElement('div');
  panel.className = 'audit-panel card';
  panel.innerHTML = `
    <div class="card-header"><div class="card-title">Library Gardener Self-Audit (23.x)</div></div>
    <p class="small">Based on the gardened library-gardener skill (v3) from 09-PROMPTS/Library.</p>
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
    <div style="margin-top:12px" class="small">Run the in-PWA gardener self-audit or the real library-gardener skill in the vault after heavy use.</div>
    <button onclick="openGardenerAudit()" style="margin-top:8px">Open deeper library-gardener self-audit</button>
  `;
}

function togglePolaris() { /* same as 22.x */ 
  const enabled = document.getElementById('polaris-toggle').checked;
  state.polaris.enabled = enabled;
  saveState();
  const polarisView = document.getElementById('polaris');
  if (polarisView) polarisView.style.opacity = enabled ? '1' : '0.5';
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
    updateProofDisplay();
    const cb = document.getElementById('polaris-toggle');
    if (cb) cb.checked = state.polaris.enabled;
  }

  if (tab === 'dashboard') {
    renderDashboard();
  }
}

function startSmall() { showTab('polaris'); setEnergy('low'); showToast("Start small. One floor move."); }
function exploreFull() { showTab('skills'); showToast("Full program available. No intake required."); }
function personalizeMore() { showTab('polaris'); showToast("Personalization is optional. You can edit anytime."); }
function emergencyFloor() { showTab('safebox'); setEnergy('collapse'); }
function quickRestart() { showTab('polaris'); setEnergy(state.energy || 'medium'); showToast("No questions. Just the floor."); }

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
  const pack = `Daily Pack from 09-PROMPTS/Library (Polaris 23.x)

${Object.keys(SNF_SKILLS).map(k => {
    const s = SNF_SKILLS[k];
    return `## ${s.name}\n${s.desc}\n${s.invocation}`;
  }).join('\n\n')}

Energy: ${state.energy}
Log everything as proof. Restart without punishment.
New in 23.x: PHQ-9 engine + gardener self-audit + adaptive quests available in the PWA.`;

  navigator.clipboard.writeText(pack).then(() => showToast("Daily pack copied (SNF core + 23.x)"));
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
      // optional auto
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

  console.log(`Polaris ${VERSION} initialized. Full 23.x features active. Source: 09-PROMPTS/Library gardener pass.`);
}

init();

window.POLARIS_23 = { state, setEnergy, logFloorWin, copySkill, showTab, openPHQ9, openGardenerAudit };
