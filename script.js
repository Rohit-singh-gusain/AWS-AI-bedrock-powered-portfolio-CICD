// ═══════════════════════════════════════════════
//  Rohit Singh Gusain — Portfolio Script
//  Scroll Reveal · Navbar · Terminal · Chatbox
// ═══════════════════════════════════════════════

// ── Scroll Reveal ────────────────────────────────
const revealObserver = new IntersectionObserver(
  entries => entries.forEach(e => {
    if (e.isIntersecting) e.target.classList.add('visible');
  }),
  { threshold: 0.08 }
);
document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// ── Navbar shadow on scroll ──────────────────────
window.addEventListener('scroll', () => {
  document.getElementById('navbar').classList.toggle('scrolled', window.scrollY > 40);
});

// ── Terminal cursor blink ────────────────────────
setInterval(() => {
  const c = document.querySelector('.t-cursor');
  if (c) c.style.opacity = c.style.opacity === '0' ? '1' : '0';
}, 530);

// ── Chatbox ──────────────────────────────────────

// ⚠️  DO NOT edit this line manually
// This value is automatically injected by GitHub Actions from Terraform output "chat_api_url"
const API_URL = 'REPLACE_WITH_API_URL';

const fab      = document.getElementById('chatFab');
const win      = document.getElementById('chatWindow');
const closeBtn = document.getElementById('chatClose');
const fabIcon  = document.getElementById('fabIcon');
const input    = document.getElementById('chatInput');
const sendBtn  = document.getElementById('chatSend');
const msgBox   = document.getElementById('chatMessages');
let chatOpen   = false;

const ICON_CHAT = `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>`;
const ICON_CLOSE = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>`;

// Toggle chat open / close
function toggleChat() {
  chatOpen = !chatOpen;
  win.classList.toggle('open', chatOpen);
  fab.classList.toggle('active', chatOpen);
  fabIcon.innerHTML = chatOpen ? ICON_CLOSE : ICON_CHAT;
  if (chatOpen) setTimeout(() => input.focus(), 250);
}
fab.addEventListener('click', toggleChat);
closeBtn.addEventListener('click', toggleChat);

// Suggestion chips
document.querySelectorAll('.suggestion-chip').forEach(chip => {
  chip.addEventListener('click', () => {
    sendMessage(chip.textContent.trim());
    document.querySelector('.chat-suggestions')?.remove();
  });
});

// Send on button click or Enter key
sendBtn.addEventListener('click', () => sendMessage(input.value));
input.addEventListener('keydown', e => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage(input.value);
  }
});

// ── Core send function ───────────────────────────
async function sendMessage(text) {
  const prompt = text.trim();
  if (!prompt) return;

  document.querySelector('.chat-suggestions')?.remove();

  appendBubble('user', prompt);
  input.value = '';
  setLoading(true);

  const typingEl = appendTyping();

  try {
    const res = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: prompt })
    });

    typingEl.remove();

    if (!res.ok) {
      const errText = await res.text();
      throw new Error(`API ${res.status}: ${errText}`);
    }

    const data = await res.json();

    const reply =
      (typeof data === 'string' ? data : null) ||
      data.reply || data.message || data.response || data.answer ||
      JSON.stringify(data);

    appendBubble('bot', reply);

  } catch (err) {
    typingEl.remove();
    appendBubble('bot', `⚠️ Something went wrong: ${err.message}. Please try again.`);
    console.error('Chatbox error:', err);
  }

  setLoading(false);
  input.focus();
}

// ── Helpers ──────────────────────────────────────
function appendBubble(role, text) {
  const wrap = document.createElement('div');
  wrap.className = `chat-msg ${role}`;
  const bubble = document.createElement('div');
  bubble.className = 'chat-bubble';
  bubble.textContent = text;
  wrap.appendChild(bubble);
  msgBox.appendChild(wrap);
  msgBox.scrollTop = msgBox.scrollHeight;
  return wrap;
}

function appendTyping() {
  const wrap = document.createElement('div');
  wrap.className = 'chat-msg bot';
  wrap.innerHTML = `<div class="chat-bubble typing-bubble"><span></span><span></span><span></span></div>`;
  msgBox.appendChild(wrap);
  msgBox.scrollTop = msgBox.scrollHeight;
  return wrap;
}

function setLoading(state) {
  sendBtn.disabled      = state;
  input.disabled        = state;
  sendBtn.style.opacity = state ? '0.5' : '1';
}