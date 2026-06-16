// Polaris 22.x — State Not Fate PWA
// Built 2026-06-13 per Grok Build master prompt v2 + full library gardener pass
// Source of truth integration: 09-PROMPTS/Library (SNF skills + Dictionary principles)

const VERSION = "22.x";

let state = {
  version: VERSION,
  energy: "medium",
  polaris: {
    enabled: true,
    proof: { total: 0, today: 0, ledger: [] },
    anchors: { active: [] },
    streaks: { current: 0, longest: 0, missed: 0 },
    lastReset: null,
    lastActive: Date.now()
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

function loadState() {
  try {
    const saved = localStorage.getItem('snf_polaris_22');
    if (saved) {
      const parsed = JSON.parse(saved);
      state = { ...state, ...parsed };
      // Ensure nested polaris
      if (!state.polaris.proof) state.polaris.proof = { total: 0, today: 0, ledger: [] };
      if (!state.polaris.anchors) state.polaris.anchors = { active: [] };
      if (!state.polaris.streaks) state.polaris.streaks = { current: 0, longest: 0, missed: 0 };
      // Fix for 22.x: ensure anchors has energy key for render logic
      if (typeof state.polaris.anchors.energy === 'undefined') {
        state.polaris.anchors.energy = state.energy || 'medium';
      }
    }
  } catch (e) {}
  updateLastActiveDisplay();
}

function saveState() {
  try {
    localStorage.setItem('snf_polaris_22', JSON.stringify(state));
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
  saveState();
  showToast(`Energy set to ${level}. Plan adapted.`, "info");
}

function renderPolarisPlan() {
  const container = document.getElementById('polaris-plan');
  if (!container) return;

  const e = state.energy;
  let text = "";

  if (e === "high") {
    text = "High energy. Full anchors + one meaningful expansion move. Use the library skills for depth.";
  } else if (e === "medium") {
    text = "Functional. Standard anchors + one proof-generating task from the SNF skills.";
  } else if (e === "low") {
    text = "Low energy. MVD only. Protect the floor. One visible win is enough. Restart without punishment.";
  } else {
    text = "Collapse. Absolute floor only. Feet on floor. Water/meds if due. One line of counter-script. Log as Floor Win. Nothing else required.";
  }

  container.innerHTML = `<strong>Today's Plan (${e}):</strong><br>${text}`;
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
  
  // Reset today's anchors if energy changed significantly or new day
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
  
  // Tie to proof-registration skill
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

function restartToday() {
  if (!confirm("Restart only today's progress? Streaks and total proof stay.")) return;
  state.polaris.proof.today = 0;
  state.polaris.anchors.active.forEach(a => a.done = false);
  state.polaris.lastReset = Date.now();
  saveState();
  renderAnchors();
  updateProofDisplay();
  showToast("Today reset. Nothing erased. Start with the floor.");
}

function setPolarisEnabled(enabled) {
  state.polaris.enabled = enabled;
  const cb = document.getElementById('polaris-toggle');
  if (cb) cb.checked = enabled;
  saveState();
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
    updateProofDisplay();
    const cb = document.getElementById('polaris-toggle');
    if (cb) cb.checked = state.polaris.enabled;
    // 22.x fix: ensure energy bar highlights current after tab switch
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

  if (tab === 'skills') {
    // nothing extra
  }
}

function renderDashboard() {
  const c = document.getElementById('dashboard-content');
  if (!c) return;
  c.innerHTML = `
    <div>Energy: <strong>${state.energy}</strong></div>
    <div>Proof today: <strong>${state.polaris.proof.today || 0}</strong></div>
    <div>Total proof: <strong>${state.polaris.proof.total || 0}</strong></div>
    <div>Current anchors completed: ${state.polaris.anchors.active ? state.polaris.anchors.active.filter(a=>a.done).length : 0}</div>
    <div style="margin-top:12px" class="small">Library gardener recommends running full audit after using multiple skills.</div>
    <button onclick="copySkill('library-gardener')" style="margin-top:8px">Run library-gardener (copy for AI)</button>
  `;
}

function startSmall() {
  showTab('polaris');
  setEnergy('low');
  showToast("Start small. One floor move.");
}

function exploreFull() {
  showTab('skills');
  showToast("Full program available. No intake required.");
}

function personalizeMore() {
  showTab('polaris');
  showToast("Personalization is optional. You can edit anytime.");
}

function emergencyFloor() {
  showTab('safebox');
  setEnergy('collapse');
}

function quickRestart() {
  showTab('polaris');
  setEnergy(state.energy || 'medium');
  showToast("No questions. Just the floor.");
}

function copySkill(skillKey) {
  const skill = SNF_SKILLS[skillKey];
  if (!skill) return;

  const text = `You are operating from my personal skill & prompt library (09-PROMPTS/Library).
Source of truth: Obsidian vault.

Skill: ${skill.name}
${skill.desc}

Invocation: ${skill.invocation}

Current energy: ${state.energy}
Use exactly. Bottom line first. One micro-action.`;

  navigator.clipboard.writeText(text).then(() => {
    showToast(`${skill.name} copied for AI`);
  }).catch(() => {
    // fallback
    prompt("Copy this:", text);
  });
}

function emitDailyPack() {
  const pack = `Daily Pack from 09-PROMPTS/Library (Polaris 22.x)

${Object.keys(SNF_SKILLS).slice(0,4).map(k => {
    const s = SNF_SKILLS[k];
    return `## ${s.name}\n${s.desc}\n${s.invocation}`;
  }).join('\n\n')}

Energy: ${state.energy}
Log everything as proof. Restart without punishment.`;

  navigator.clipboard.writeText(pack).then(() => showToast("Daily pack copied (SNF core)"));
}

function initEnergyButtons() {
  // Set initial active (22.x fix: removed redundant empty listener)
  document.querySelectorAll('.energy-option').forEach(el => {
    if (el.textContent.toLowerCase() === (state.energy || 'medium')) {
      el.classList.add('active');
    }
  });
}

function init() {
  loadState();

  // Initial energy
  if (!state.energy) state.energy = "medium";
  
  // Polaris toggle initial
  const cb = document.getElementById('polaris-toggle');
  if (cb) cb.checked = state.polaris.enabled !== false;

  // Show default tab
  showTab('welcome');

  // Seed some demo proof if first run
  if (state.polaris.proof.total === 0) {
    state.polaris.proof.total = 47; // example from previous use
    state.polaris.proof.today = 1;
  }

  initEnergyButtons();
  updateProofDisplay();

  // Auto-show Polaris if enabled and not brand new
  setTimeout(() => {
    if (state.polaris.enabled && state.polaris.lastActive) {
      // optional: showTab('polaris');
    }
  }, 800);

  // Update last active
  state.polaris.lastActive = Date.now();
  saveState();

  // Keyboard support (very light)
  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement.tagName === "BODY") {
      e.preventDefault();
      showTab('polaris');
    }
  });

  console.log(`Polaris ${VERSION} initialized. Source: 09-PROMPTS/Library + STATENOTFATE.`);
}

// Boot
init();

// Expose for debugging / future AI integration
window.POLARIS_22 = { state, setEnergy, logFloorWin, copySkill, showTab };
