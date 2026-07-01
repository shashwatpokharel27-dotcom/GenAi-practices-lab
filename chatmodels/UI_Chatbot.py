import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Mistral Chat",
    page_icon="✦",
    layout="centered",
)

# ── Styling ───────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap');

  html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0f0f11;
    color: #e8e6e3;
  }

  /* Hide Streamlit chrome */
  #MainMenu, footer, header { visibility: hidden; }
  .block-container { padding: 2rem 1.5rem 6rem; max-width: 760px; }

  /* Header */
  .chat-header {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 1.2rem 0 1.6rem;
    border-bottom: 1px solid #222226;
    margin-bottom: 1.5rem;
  }
  .chat-header .logo {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, #7c6af7, #bf9bff);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px; line-height: 1;
  }
  .chat-header h1 {
    margin: 0; font-size: 1.15rem; font-weight: 600;
    color: #f0eef8; letter-spacing: -0.01em;
  }
  .chat-header p {
    margin: 0; font-size: 0.78rem; color: #6b6880;
  }
  .model-badge {
    margin-left: auto;
    background: #1a1a22; border: 1px solid #2d2d38;
    border-radius: 6px; padding: 4px 10px;
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem; color: #7c6af7;
  }

  /* Message bubbles */
  .msg-row { display: flex; gap: 10px; margin-bottom: 1.1rem; align-items: flex-start; }
  .msg-row.user { flex-direction: row-reverse; }

  .avatar {
    width: 30px; height: 30px; border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; flex-shrink: 0; margin-top: 2px;
  }
  .avatar.bot { background: linear-gradient(135deg, #7c6af7, #bf9bff); }
  .avatar.user { background: #1e1e28; border: 1px solid #2d2d38; }

  .bubble {
    max-width: 82%;
    padding: 0.7rem 1rem;
    border-radius: 14px;
    line-height: 1.55;
    font-size: 0.92rem;
  }
  .bubble.bot {
    background: #17171f;
    border: 1px solid #252530;
    color: #dddae8;
    border-top-left-radius: 4px;
  }
  .bubble.user {
    background: #7c6af7;
    color: #fff;
    border-top-right-radius: 4px;
  }

  /* Empty state */
  .empty-state {
    text-align: center;
    padding: 3.5rem 1rem;
    color: #4a4860;
  }
  .empty-state .icon { font-size: 2.5rem; margin-bottom: 0.75rem; }
  .empty-state p { font-size: 0.9rem; line-height: 1.6; }

  /* Typing indicator */
  .typing { display: flex; gap: 5px; padding: 10px 14px; align-items: center; }
  .typing span {
    width: 7px; height: 7px; border-radius: 50%;
    background: #7c6af7; display: inline-block;
    animation: bounce 1.2s infinite;
  }
  .typing span:nth-child(2) { animation-delay: 0.2s; }
  .typing span:nth-child(3) { animation-delay: 0.4s; }
  @keyframes bounce {
    0%, 80%, 100% { transform: translateY(0); opacity: 0.4; }
    40%            { transform: translateY(-6px); opacity: 1; }
  }

  /* Input row */
  .stChatInputContainer, [data-testid="stChatInput"] {
    background: #17171f !important;
    border: 1px solid #252530 !important;
    border-radius: 14px !important;
  }
  [data-testid="stChatInput"] textarea {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.92rem !important;
    color: #e8e6e3 !important;
    background: transparent !important;
  }

  /* Clear button */
  .stButton button {
    background: transparent;
    border: 1px solid #252530;
    color: #6b6880;
    font-size: 0.78rem;
    border-radius: 7px;
    padding: 4px 12px;
    transition: all 0.15s;
  }
  .stButton button:hover {
    border-color: #7c6af7;
    color: #7c6af7;
  }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="chat-header">
  <div class="logo">✦</div>
  <div>
    <h1>Mistral Chat</h1>
    <p>Powered by mistral-small-2603</p>
  </div>
  <div class="model-badge">mistral-small-2603</div>
</div>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a funny AI agent. Keep responses concise and entertaining.")
    ]
if "display" not in st.session_state:
    st.session_state.display = []   # list of {"role": "user"|"bot", "text": "..."}

# ── Model ─────────────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    return ChatMistralAI(model="mistral-small-2603")

model = load_model()

# ── Clear button ──────────────────────────────────────────────────────────────
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("Clear"):
        st.session_state.messages = [
            SystemMessage(content="You are a funny AI agent. Keep responses concise and entertaining.")
        ]
        st.session_state.display = []
        st.rerun()

# ── Render conversation ───────────────────────────────────────────────────────
if not st.session_state.display:
    st.markdown("""
    <div class="empty-state">
      <div class="icon">💬</div>
      <p>Start a conversation.<br>Ask anything — this bot has a sense of humor.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    for msg in st.session_state.display:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="msg-row user">
              <div class="avatar user">🙂</div>
              <div class="bubble user">{msg["text"]}</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="msg-row">
              <div class="avatar bot">✦</div>
              <div class="bubble bot">{msg["text"]}</div>
            </div>""", unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
prompt = st.chat_input("Type a message…")

if prompt:
    # Show user message immediately
    st.session_state.display.append({"role": "user", "text": prompt})
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Render the new user bubble before the bot responds
    st.markdown(f"""
    <div class="msg-row user">
      <div class="avatar user">🙂</div>
      <div class="bubble user">{prompt}</div>
    </div>""", unsafe_allow_html=True)

    # Typing indicator + model call
    placeholder = st.empty()
    placeholder.markdown("""
    <div class="msg-row">
      <div class="avatar bot">✦</div>
      <div class="bubble bot">
        <div class="typing"><span></span><span></span><span></span></div>
      </div>
    </div>""", unsafe_allow_html=True)

    response = model.invoke(st.session_state.messages)
    reply = response.content

    st.session_state.messages.append(AIMessage(content=reply))
    st.session_state.display.append({"role": "bot", "text": reply})

    placeholder.empty()
    st.rerun()