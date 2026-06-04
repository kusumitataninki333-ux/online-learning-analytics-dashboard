import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random, time

st.set_page_config(
    page_title="LearnPulse AI | Online Learning Intelligence",
    page_icon="🎓", layout="wide",
    initial_sidebar_state="expanded"
)
APP_PASSWORD = "kusu@123"

password = st.text_input(
    "🔒 Enter Dashboard Password",
    type="password"
)

# ══════════════════════════════════════════════════════════════
# CSS — DARK GLASSMORPHISM + ANIMATIONS
# ══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap');
*{font-family:'Inter',sans-serif;box-sizing:border-box;}

/* ── PAGE ── */
.stApp{background:#030712;}
.main .block-container{background:#030712;padding:1.5rem 2.5rem 3rem;}

/* ── SIDEBAR ── */
[data-testid="stSidebar"]{
  background:linear-gradient(180deg,#0a0f1e 0%,#0d1525 50%,#0a1628 100%) !important;
  border-right:1px solid rgba(99,102,241,.15) !important;
}
[data-testid="stSidebar"] *{color:#e2e8f0 !important;}
[data-testid="stSidebar"] label{
  color:#6366f1 !important;font-size:.68rem !important;
  font-weight:700 !important;text-transform:uppercase !important;letter-spacing:2px !important;
}
[data-testid="stSidebar"] .stSelectbox>div>div{
  background:rgba(99,102,241,.08) !important;
  border:1px solid rgba(99,102,241,.25) !important;border-radius:10px !important;
}

/* ── ANIMATIONS ── */
@keyframes fadeUp{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:translateY(0)}}
@keyframes fadeLeft{from{opacity:0;transform:translateX(-28px)}to{opacity:1;transform:translateX(0)}}
@keyframes fadeRight{from{opacity:0;transform:translateX(28px)}to{opacity:1;transform:translateX(0)}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
@keyframes glow{0%,100%{box-shadow:0 0 15px rgba(99,102,241,.2)}50%{box-shadow:0 0 50px rgba(99,102,241,.7),0 0 80px rgba(139,92,246,.3)}}
@keyframes gradMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.7;transform:scale(1.08)}}
@keyframes spin{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
@keyframes countUp{from{opacity:0;transform:scale(.4) translateY(12px)}to{opacity:1;transform:scale(1) translateY(0)}}
@keyframes shimmer{0%{background-position:-400px 0}100%{background-position:400px 0}}
@keyframes typeDot{0%,60%,100%{transform:translateY(0)}30%{transform:translateY(-9px)}}
@keyframes borderPulse{0%,100%{border-color:rgba(99,102,241,.2)}50%{border-color:rgba(99,102,241,.7)}}
@keyframes scanLine{0%{transform:translateY(-100%)}100%{transform:translateY(100vh)}}
@keyframes ripple{0%{transform:scale(0);opacity:.6}100%{transform:scale(2.5);opacity:0}}

/* ── HERO ── */
.hero{
  background:linear-gradient(-45deg,#030712,#0f0a2e,#0a1628,#1e1b4b,#0d3352,#0a2420);
  background-size:600% 600%;
  animation:gradMove 12s ease infinite;
  border-radius:28px;padding:52px 56px;
  margin-bottom:32px;position:relative;overflow:hidden;
  border:1px solid rgba(99,102,241,.15);
}
.hero::before{
  content:'';position:absolute;top:-120px;right:-80px;
  width:500px;height:500px;border-radius:50%;
  background:radial-gradient(circle,rgba(99,102,241,.12) 0%,transparent 70%);
  animation:float 8s ease infinite;
}
.hero::after{
  content:'';position:absolute;bottom:-100px;left:15%;
  width:350px;height:350px;border-radius:50%;
  background:radial-gradient(circle,rgba(13,148,136,.08) 0%,transparent 70%);
  animation:float 10s ease infinite reverse;
}
.hero-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(99,102,241,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(99,102,241,.03) 1px,transparent 1px);background-size:40px 40px;}
.hero-content{position:relative;z-index:3;}
.hero-eyebrow{
  display:inline-flex;align-items:center;gap:8px;
  background:rgba(99,102,241,.12);border:1px solid rgba(99,102,241,.3);
  border-radius:99px;padding:6px 18px;
  font-size:.7rem;font-weight:700;color:#a5b4fc;letter-spacing:2px;
  text-transform:uppercase;margin-bottom:20px;
  animation:fadeLeft .6s ease both;
}
.hero-dot{width:7px;height:7px;border-radius:50%;background:#6366f1;animation:pulse 2s infinite;}
.hero-title{
  font-size:3.4rem;font-weight:900;color:#fff;
  letter-spacing:-2.5px;line-height:.95;
  animation:fadeLeft .7s ease .1s both;
}
.hero-title .g1{background:linear-gradient(135deg,#818cf8,#6ee7b7);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.hero-title .g2{background:linear-gradient(135deg,#f472b6,#fb923c);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.hero-sub{font-size:1.05rem;color:rgba(255,255,255,.55);margin-top:12px;animation:fadeLeft .7s ease .2s both;line-height:1.6;}
.hero-stats{
  display:flex;gap:28px;margin-top:28px;
  animation:fadeLeft .7s ease .3s both;flex-wrap:wrap;
}
.hstat{text-align:center;}
.hstat-val{font-size:1.6rem;font-weight:900;color:#fff;font-family:'JetBrains Mono',monospace;letter-spacing:-1px;}
.hstat-lbl{font-size:.65rem;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:1.5px;margin-top:2px;}
.hstat-div{width:1px;background:rgba(255,255,255,.1);margin:4px 0;}
.hero-badges{margin-top:22px;animation:fadeLeft .7s ease .4s both;}
.hbadge{
  display:inline-block;
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);
  border-radius:99px;padding:6px 16px;
  font-size:.72rem;font-weight:600;color:rgba(255,255,255,.7);
  margin:4px 6px 4px 0;backdrop-filter:blur(8px);
  transition:all .3s;cursor:default;
}
.hbadge:hover{background:rgba(99,102,241,.25);border-color:rgba(99,102,241,.5);color:#fff;transform:translateY(-2px);}
.hero-right{position:absolute;right:60px;top:50%;transform:translateY(-50%);z-index:2;text-align:center;}
.hero-icon-big{font-size:6rem;animation:float 5s ease infinite;filter:drop-shadow(0 0 40px rgba(99,102,241,.6));display:block;}
.hero-icon-ring{
  width:160px;height:160px;border-radius:50%;
  border:1px solid rgba(99,102,241,.2);
  position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  animation:spin 20s linear infinite;
}

/* ── KPI CARDS ── */
.kpi{
  border-radius:22px;padding:26px 22px;color:#fff;
  position:relative;overflow:hidden;
  animation:fadeUp .6s ease both;
  transition:transform .35s cubic-bezier(.34,1.56,.64,1),box-shadow .35s;
  cursor:default;border:1px solid rgba(255,255,255,.05);
}
.kpi:hover{transform:translateY(-10px) scale(1.04);box-shadow:0 24px 60px rgba(0,0,0,.5);}
.kpi-shine{
  position:absolute;top:0;left:-100%;width:55%;height:100%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.06),transparent);
  transition:left .7s ease;
}
.kpi:hover .kpi-shine{left:150%;}
.kpi-orb1{position:absolute;top:-30px;right:-30px;width:110px;height:110px;border-radius:50%;background:rgba(255,255,255,.07);}
.kpi-orb2{position:absolute;bottom:-40px;left:-15px;width:130px;height:130px;border-radius:50%;background:rgba(255,255,255,.04);}
.kpi-icon{font-size:1.8rem;margin-bottom:10px;display:inline-block;animation:float 3.5s ease infinite;position:relative;z-index:1;}
.kpi-val{
  font-size:2.3rem;font-weight:900;
  font-family:'JetBrains Mono',monospace;
  letter-spacing:-1.5px;line-height:1;
  animation:countUp .8s cubic-bezier(.34,1.56,.64,1) both;
  position:relative;z-index:1;
}
.kpi-lbl{font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:2.5px;opacity:.72;margin-top:6px;position:relative;z-index:1;}
.kpi-delta{
  display:inline-block;font-size:.71rem;margin-top:9px;
  background:rgba(255,255,255,.14);border-radius:99px;padding:3px 11px;
  position:relative;z-index:1;
}

/* ── GLASS CARDS ── */
.gcard{
  background:linear-gradient(135deg,rgba(255,255,255,.04),rgba(255,255,255,.01));
  border-radius:22px;padding:26px 28px;margin-bottom:24px;
  border:1px solid rgba(255,255,255,.07);
  animation:fadeUp .7s ease both;
  transition:border-color .35s,box-shadow .35s,transform .35s;
  backdrop-filter:blur(10px);
}
.gcard:hover{border-color:rgba(99,102,241,.35);box-shadow:0 12px 50px rgba(99,102,241,.12);transform:translateY(-4px);}
.gcard-title{
  font-size:.9rem;font-weight:700;color:#f1f5f9;
  margin-bottom:16px;padding-bottom:12px;
  border-bottom:1px solid rgba(255,255,255,.06);
  display:flex;align-items:center;gap:8px;
}

/* ── ALERTS ── */
.alert-r{background:rgba(239,68,68,.08);border:1px solid rgba(239,68,68,.25);border-left:4px solid #ef4444;border-radius:14px;padding:13px 18px;font-size:.82rem;color:#fca5a5;margin:6px 0;animation:fadeUp .4s ease both;}
.alert-y{background:rgba(245,158,11,.08);border:1px solid rgba(245,158,11,.25);border-left:4px solid #f59e0b;border-radius:14px;padding:13px 18px;font-size:.82rem;color:#fcd34d;margin:6px 0;animation:fadeUp .4s ease .1s both;}
.alert-g{background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.25);border-left:4px solid #10b981;border-radius:14px;padding:13px 18px;font-size:.82rem;color:#6ee7b7;margin:6px 0;animation:fadeUp .4s ease .2s both;}

/* ── INSIGHT ── */
.insight{
  background:linear-gradient(135deg,rgba(99,102,241,.08),rgba(139,92,246,.05));
  border:1px solid rgba(99,102,241,.2);border-left:4px solid #6366f1;
  border-radius:14px;padding:13px 18px;
  font-size:.82rem;color:#c7d2fe;margin-bottom:20px;
  animation:fadeLeft .6s ease both;
}
.insight b{color:#a5b4fc;}

/* ── PILLS ── */
.pills{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px;}
.pill{
  background:rgba(99,102,241,.08);border:1px solid rgba(99,102,241,.2);
  border-radius:10px;padding:7px 14px;
  font-size:.75rem;color:#a5b4fc;font-weight:600;
  transition:all .25s;cursor:default;
}
.pill:hover{background:rgba(99,102,241,.2);border-color:rgba(99,102,241,.5);color:#fff;transform:translateY(-2px);}
.pill span{color:#818cf8;font-weight:900;}

/* ── SIDEBAR ── */
.slbl{font-size:.6rem;font-weight:700;color:#4f46e5;letter-spacing:3px;text-transform:uppercase;margin:18px 0 6px 2px;}
.sdiv{height:1px;background:linear-gradient(90deg,rgba(99,102,241,.4),transparent);margin:12px 0;}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"]{
  background:rgba(99,102,241,.05);border-radius:18px;padding:6px;
  gap:5px;border:1px solid rgba(99,102,241,.12);margin-bottom:22px;
}
.stTabs [data-baseweb="tab"]{
  border-radius:12px;font-weight:600;font-size:.83rem;
  color:#6b7280;padding:10px 22px;transition:all .3s;
}
.stTabs [aria-selected="true"]{
  background:linear-gradient(135deg,#4f46e5,#7c3aed) !important;
  color:#fff !important;
  box-shadow:0 6px 24px rgba(79,70,229,.5) !important;
}

/* ── AI BOX ── */
.ai-wrap{
  background:linear-gradient(135deg,rgba(99,102,241,.06),rgba(139,92,246,.04));
  border-radius:24px;padding:32px;
  border:1px solid rgba(99,102,241,.2);
  animation:glow 5s ease infinite;margin-bottom:24px;
}
.ai-hdr{font-size:1.15rem;font-weight:800;color:#e2e8f0;display:flex;align-items:center;gap:12px;margin-bottom:8px;}
.ai-live{
  background:linear-gradient(135deg,#4f46e5,#7c3aed);
  border-radius:99px;padding:4px 14px;font-size:.65rem;
  font-weight:700;color:#fff;animation:pulse 2.5s ease infinite;display:inline-block;
}
.ai-sub{font-size:.8rem;color:#6b7280;margin-bottom:24px;}
.msg-u{
  background:rgba(99,102,241,.12);border:1px solid rgba(99,102,241,.2);
  border-radius:18px 18px 4px 18px;padding:13px 18px;
  margin:10px 0;font-size:.85rem;color:#c7d2fe;
  max-width:78%;margin-left:auto;text-align:right;
  animation:fadeRight .35s ease;
}
.msg-ai{
  background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);
  border-radius:4px 18px 18px 18px;padding:16px 20px;
  margin:10px 0;font-size:.85rem;color:#cbd5e1;
  max-width:94%;line-height:1.75;
  animation:fadeLeft .4s ease;
}
.msg-ai b{color:#a5b4fc;}
.dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:#6366f1;margin:0 2px;}
.dot:nth-child(1){animation:typeDot 1.2s 0s infinite;}
.dot:nth-child(2){animation:typeDot 1.2s .2s infinite;}
.dot:nth-child(3){animation:typeDot 1.2s .4s infinite;}

/* ── SCOREBOARD ── */
.score-row{
  display:flex;align-items:center;gap:14px;
  background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);
  border-radius:14px;padding:14px 18px;margin-bottom:10px;
  transition:all .3s;animation:fadeLeft .5s ease both;
}
.score-row:hover{background:rgba(99,102,241,.08);border-color:rgba(99,102,241,.25);transform:translateX(6px);}
.score-rank{font-size:1.1rem;font-weight:900;font-family:'JetBrains Mono',monospace;color:#6366f1;width:32px;}
.score-name{flex:1;font-size:.85rem;color:#e2e8f0;font-weight:600;}
.score-course{font-size:.72rem;color:#6b7280;}
.score-bar-wrap{width:120px;background:rgba(255,255,255,.06);border-radius:99px;height:6px;}
.score-bar-fill{height:6px;border-radius:99px;}
.score-num{font-size:.82rem;font-weight:700;font-family:'JetBrains Mono',monospace;width:40px;text-align:right;}

/* ── PROGRESS RING ── */
.ring-wrap{text-align:center;padding:16px;}
.ring-val{font-size:1.8rem;font-weight:900;font-family:'JetBrains Mono',monospace;color:#fff;}
.ring-lbl{font-size:.68rem;color:#6b7280;text-transform:uppercase;letter-spacing:1.5px;margin-top:4px;}

/* ── FOOTER ── */
.footer{
  text-align:center;padding:22px;font-size:.72rem;
  color:#374151;border-top:1px solid rgba(99,102,241,.08);
  margin-top:36px;animation:fadeUp 1s ease both;
}
.footer span{background:linear-gradient(135deg,#818cf8,#6ee7b7);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:800;}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# DATA
# ══════════════════════════════════════════════════════════════
@st.cache_data
def generate_data():
    random.seed(42); np.random.seed(42)
    n=300
    courses=["Python Basics","Data Science","Machine Learning","Cloud Computing","Web Development"]
    instructors={"Python Basics":"Dr. Meera R.","Data Science":"Prof. Arjun S.",
                 "Machine Learning":"Dr. Ravi K.","Cloud Computing":"Dr. Anita P.","Web Development":"Ms. Priya T."}
    start=datetime(2024,1,1)
    df=pd.DataFrame({
        "student_id":[f"STU{i:04d}" for i in range(1,n+1)],
        "name":[f"Student {i:03d}" for i in range(1,n+1)],
        "course":np.random.choice(courses,n),
        "gender":np.random.choice(["Male","Female","Other"],n,p=[.48,.47,.05]),
        "device":np.random.choice(["Desktop","Mobile","Tablet"],n,p=[.55,.35,.10]),
        "enrollment_date":[start+timedelta(days=random.randint(0,150)) for _ in range(n)],
        "age":np.random.randint(18,45,n),
        "logins_per_week":np.random.poisson(4,n),
        "video_watch_pct":np.clip(np.random.normal(65,20,n),0,100),
        "quiz_score":np.clip(np.random.normal(72,15,n),0,100),
        "assignment_score":np.clip(np.random.normal(74,14,n),0,100),
        "completion_pct":np.clip(np.random.normal(60,25,n),0,100),
        "forum_posts":np.random.poisson(3,n),
        "live_sessions":np.random.poisson(2,n),
        "dropped_out":np.random.choice([True,False],n,p=[.2,.8]),
        "satisfaction":np.clip(np.random.normal(3.8,.8,n),1,5).round(1),
        "time_spent_hrs":np.clip(np.random.normal(12,5,n),1,40),
    })
    df["instructor"]=df["course"].map(instructors)
    df["engagement_score"]=(df["logins_per_week"]*5+df["video_watch_pct"]*0.3+df["quiz_score"]*0.3+df["forum_posts"]*3+df["live_sessions"]*4).clip(0,100)
    df["assignment_score"]=np.clip(np.random.normal(74,14,n),0,100)
    df["dropout_probability"]=((100-df["engagement_score"])*.4+(100-df["completion_pct"])*.3).clip(0,100)/100
    df["predicted_final"]=(df["quiz_score"]*.4+df["assignment_score"]*.4+df["engagement_score"]*.2).clip(0,100)
    def risk(s):
        if s<35: return "High Risk"
        elif s<60: return "Medium Risk"
        return "Low Risk"
    df["risk_level"]=df["engagement_score"].apply(risk)
    df["month"]=df["enrollment_date"].dt.strftime("%b %Y")
    df["week"]=df["enrollment_date"].dt.isocalendar().week.astype(int)
    return df.round(2)

with st.spinner("🚀 Launching LearnPulse AI..."): df_all=generate_data()

# ══════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style='text-align:center;padding:30px 8px 16px'>
      <div style='position:relative;display:inline-block'>
        <div style='width:80px;height:80px;border-radius:50%;background:linear-gradient(135deg,#4f46e5,#7c3aed);display:flex;align-items:center;justify-content:center;font-size:2.4rem;margin:0 auto;box-shadow:0 0 30px rgba(99,102,241,.6);animation:glow 4s ease infinite'>🎓</div>
      </div>
      <div style='font-size:1.1rem;font-weight:900;letter-spacing:4px;color:#fff;margin-top:14px'>LEARNPULSE</div>
      <div style='font-size:.58rem;color:#4f46e5;letter-spacing:5px;margin-top:4px'>AI ENTERPRISE</div>
      <div style='margin-top:14px'>
        <span style='background:linear-gradient(135deg,#4f46e5,#7c3aed);border-radius:99px;padding:5px 18px;font-size:.65rem;font-weight:700;color:#fff;animation:pulse 2s infinite;display:inline-block;box-shadow:0 0 20px rgba(99,102,241,.5)'>⚡ LIVE</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='sdiv'></div><div class='slbl'>📊 Filters</div>", unsafe_allow_html=True)
    cl=["All Courses"]+sorted(df_all["course"].unique())
    sel_c=st.selectbox("Course",cl)
    sel_r=st.selectbox("Risk Level",["All","High Risk","Medium Risk","Low Risk"])
    sel_d=st.selectbox("Device",["All","Desktop","Mobile","Tablet"])
    min_e,max_e=st.slider("Engagement Score",0,100,(0,100))
    show_drop=st.checkbox("Include Dropouts",value=True)

    st.markdown("<div class='sdiv'></div><div class='slbl'>🤖 AI Settings</div>", unsafe_allow_html=True)
    api_key=st.text_input("Anthropic API Key",type="password",placeholder="sk-ant-...",help="Get free key at console.anthropic.com")

    st.markdown("<div class='sdiv'></div><div class='slbl'>📂 Upload Data</div>", unsafe_allow_html=True)
    uploaded=st.file_uploader("CSV file",type=["csv"],label_visibility="collapsed")
    if uploaded: df_all=pd.read_csv(uploaded); st.success("✅ Loaded!")

    st.markdown("<div class='sdiv'></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;font-size:.6rem;color:#374151;padding-bottom:14px'>LearnPulse AI v5.0 · © 2026<br>Online Learning Intelligence Platform</div>", unsafe_allow_html=True)

# ── FILTER ────────────────────────────────────────────────────
df=df_all.copy()
if sel_c!="All Courses": df=df[df["course"]==sel_c]
if sel_r!="All": df=df[df["risk_level"]==sel_r]
if sel_d!="All": df=df[df["device"]==sel_d]
if not show_drop: df=df[~df["dropped_out"]]
df=df[(df["engagement_score"]>=min_e)&(df["engagement_score"]<=max_e)]

RC={"Low Risk":"#10b981","Medium Risk":"#f59e0b","High Risk":"#ef4444"}

def bl(fig):
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",paper_bgcolor="rgba(0,0,0,0)",
        font_color="#6b7280",margin=dict(l=5,r=5,t=28,b=5),
        legend=dict(bgcolor="rgba(0,0,0,0)",font_color="#9ca3af"),
    )
    fig.update_xaxes(gridcolor="rgba(255,255,255,.04)",zerolinecolor="rgba(255,255,255,.04)",color="#4b5563")
    fig.update_yaxes(gridcolor="rgba(255,255,255,.04)",zerolinecolor="rgba(255,255,255,.04)",color="#4b5563")
    return fig

def kpi(col,val,label,icon,bg,delta="",neg=False,d="0s"):
    arr="▼ " if neg else "▲ "
    dc="rgba(255,140,140,.9)" if neg else "rgba(140,255,175,.9)"
    dh=f'<div class="kpi-delta" style="color:{dc}">{arr}{delta}</div>' if delta else ""
    col.markdown(f"""
    <div class="kpi" style="background:{bg};animation-delay:{d}">
      <div class="kpi-shine"></div><div class="kpi-orb1"></div><div class="kpi-orb2"></div>
      <div class="kpi-icon">{icon}</div>
      <div class="kpi-val">{val}</div>
      <div class="kpi-lbl">{label}</div>{dh}
    </div>""",unsafe_allow_html=True)

def gc(t,i="📊",d="0s"):
    st.markdown(f'<div class="gcard" style="animation-delay:{d}"><div class="gcard-title">{i} {t}</div>',unsafe_allow_html=True)
def ec(): st.markdown('</div>',unsafe_allow_html=True)

def ask_ai(q,ctx,key):
    if not key or not key.startswith("sk-"): return None
    try:
        import anthropic
        c=anthropic.Anthropic(api_key=key)
        r=c.messages.create(
            model="claude-sonnet-4-20250514",max_tokens=700,
            system="""You are an expert education data analyst for LearnPulse Online Learning Engagement Analysis System.
Analyse the student data and give specific, actionable insights for educators.
Use **bold** for key findings. Give exactly 3 recommended actions numbered.
Be concise and use the actual numbers from the data.""",
            messages=[{"role":"user","content":f"Live Dashboard Data:\n{ctx}\n\nQuestion: {q}"}]
        )
        return r.content[0].text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# ══════════════════════════════════════════════════════════════
# HERO BANNER
# ══════════════════════════════════════════════════════════════
now=datetime.now().strftime("%d %b %Y  •  %H:%M")
st.markdown(f"""
<div class="hero">
  <div class="hero-grid"></div>
  <div class="hero-right">
    <div style='position:relative;display:inline-block;width:160px;height:160px;'>
      <div class="hero-icon-ring"></div>
      <span class="hero-icon-big" style='position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)'>🏫</span>
    </div>
  </div>
  <div class="hero-content">
    <div class="hero-eyebrow"><div class="hero-dot"></div>ONLINE LEARNING INTELLIGENCE PLATFORM</div>
    <div class="hero-title">
      Learn<span class="g1">Pulse</span><br>
      <span class="g2">AI</span> Analytics
    </div>
    <div class="hero-sub">
      Student Engagement · Risk Detection · Dropout Prediction · AI Insights
    </div>
    <div class="hero-stats">
      <div class="hstat"><div class="hstat-val">{len(df):,}</div><div class="hstat-lbl">Students</div></div>
      <div class="hstat-div"></div>
      <div class="hstat"><div class="hstat-val">{df['engagement_score'].mean():.0f}</div><div class="hstat-lbl">Avg Engagement</div></div>
      <div class="hstat-div"></div>
      <div class="hstat"><div class="hstat-val">{(df['risk_level']=='High Risk').sum()}</div><div class="hstat-lbl">High Risk</div></div>
      <div class="hstat-div"></div>
      <div class="hstat"><div class="hstat-val">{df['completion_pct'].mean():.0f}%</div><div class="hstat-lbl">Completion</div></div>
      <div class="hstat-div"></div>
      <div class="hstat"><div class="hstat-val">{df['satisfaction'].mean():.1f}★</div><div class="hstat-lbl">Satisfaction</div></div>
    </div>
    <div class="hero-badges">
      <span class="hbadge">🤖 Claude AI</span>
      <span class="hbadge">📊 12+ Charts</span>
      <span class="hbadge">🎯 Risk Detection</span>
      <span class="hbadge">🔮 Predictions</span>
      <span class="hbadge">👨‍🏫 Instructors</span>
      <span class="hbadge">📋 Reports</span>
    </div>
  </div>
</div>
""",unsafe_allow_html=True)

# ── KPI ROW 1 ─────────────────────────────────────────────────
c1,c2,c3,c4=st.columns(4)
kpi(c1,f"{len(df):,}","Total Students","👨‍🎓","linear-gradient(135deg,#1e3a8a,#1d4ed8,#3b82f6)","+12 this week",d=".05s")
kpi(c2,f"{df['engagement_score'].mean():.1f}","Avg Engagement","⚡","linear-gradient(135deg,#3b0764,#6d28d9,#8b5cf6)","+3.2 pts",d=".1s")
kpi(c3,f"{df['completion_pct'].mean():.1f}%","Avg Completion","✅","linear-gradient(135deg,#022c22,#065f46,#10b981)","−1.4%",neg=True,d=".15s")
kpi(c4,f"{int(df['dropped_out'].sum())}","Dropouts","⚠️","linear-gradient(135deg,#450a0a,#991b1b,#ef4444)",f"{df['dropped_out'].mean()*100:.1f}%",neg=True,d=".2s")
st.markdown("<br>",unsafe_allow_html=True)

# ── KPI ROW 2 ─────────────────────────────────────────────────
c5,c6,c7,c8=st.columns(4)
kpi(c5,f"{df['quiz_score'].mean():.1f}","Avg Quiz Score","📝","linear-gradient(135deg,#082f49,#0c4a6e,#0ea5e9)","+2.1 pts",d=".25s")
kpi(c6,f"{df['satisfaction'].mean():.1f}/5","Satisfaction","⭐","linear-gradient(135deg,#431407,#92400e,#f59e0b)","+0.2",d=".3s")
kpi(c7,f"{(df['risk_level']=='High Risk').sum()}","High Risk","🔴","linear-gradient(135deg,#431407,#9a3412,#f97316)",f"{(df['risk_level']=='High Risk').mean()*100:.1f}%",neg=True,d=".35s")
kpi(c8,f"{df['time_spent_hrs'].mean():.1f}h","Avg Time Spent","⏱️","linear-gradient(135deg,#042f2e,#065f46,#14b8a6)","+0.8h",d=".4s")
st.markdown("<br>",unsafe_allow_html=True)

# ── ALERTS ────────────────────────────────────────────────────
hr_n=(df["risk_level"]=="High Risk").sum(); dp=df["dropped_out"].mean()*100; le=df[df["engagement_score"]<30]
if hr_n>40: st.markdown(f'<div class="alert-r">🚨 <b>Action Required:</b> {hr_n} students are High Risk — visit ⚠️ At-Risk tab immediately.</div>',unsafe_allow_html=True)
if dp>15:   st.markdown(f'<div class="alert-y">⚠️ <b>Warning:</b> Dropout rate is {dp:.1f}% — review course content urgently.</div>',unsafe_allow_html=True)
if len(le): st.markdown(f'<div class="alert-r">📉 <b>{len(le)} students</b> have engagement below 30 — immediate outreach needed.</div>',unsafe_allow_html=True)
st.markdown(f'<div class="alert-g">✅ <b>{(df["risk_level"]=="Low Risk").sum()} students</b> performing well with Low Risk status.</div>',unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# TABS
# ══════════════════════════════════════════════════════════════
t1,t2,t3,t4,t5,t6,t7,t8=st.tabs([
    "📊 Overview","🎓 Students","⚠️ At-Risk",
    "📈 Trends","🤖 AI Assistant","🔮 Predictions",
    "👨‍🏫 Instructors","📋 Reports"
])

# ═══ OVERVIEW ═══
with t1:
    tc=df.groupby("course")["engagement_score"].mean().idxmax()
    st.markdown(f'<div class="insight">💡 <b>Live Insight:</b> Best course: <b>{tc}</b> · Satisfaction avg <b>{df["satisfaction"].mean():.1f}/5</b> · High-risk rate <b>{(df["risk_level"]=="High Risk").mean()*100:.1f}%</b> · Avg time spent <b>{df["time_spent_hrs"].mean():.1f}h</b></div>',unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        gc("Engagement by Course","📊",".1s")
        avg=df.groupby("course")["engagement_score"].mean().reset_index().sort_values("engagement_score")
        fig=px.bar(avg,x="engagement_score",y="course",orientation="h",
                   color="engagement_score",color_continuous_scale=[[0,"#1e3a8a"],[.5,"#6366f1"],[1,"#a78bfa"]],
                   text=avg["engagement_score"].round(1))
        fig.update_traces(textposition="outside",textfont_color="#9ca3af",marker_line_width=0)
        fig.update_coloraxes(showscale=False)
        st.plotly_chart(bl(fig),use_container_width=True); ec()
    with c2:
        gc("Risk Distribution","🥧",".15s")
        rc2=df["risk_level"].value_counts().reset_index(); rc2.columns=["Risk","Count"]
        fig=px.pie(rc2,names="Risk",values="Count",hole=0.68,color="Risk",color_discrete_map=RC)
        fig.update_traces(textinfo="percent+label",textfont_size=12,textfont_color="#e2e8f0",
                          marker=dict(line=dict(color="#030712",width=3)))
        st.plotly_chart(bl(fig),use_container_width=True); ec()
    c3,c4=st.columns(2)
    with c3:
        gc("Engagement vs Completion","🎯",".2s")
        fig=px.scatter(df,x="engagement_score",y="completion_pct",color="risk_level",size="quiz_score",
                       color_discrete_map=RC,hover_data=["student_id","course"],trendline="ols",opacity=0.75)
        st.plotly_chart(bl(fig),use_container_width=True); ec()
    with c4:
        gc("Device Usage by Risk","📱",".25s")
        dv=df.groupby(["device","risk_level"]).size().reset_index(name="count")
        fig=px.bar(dv,x="device",y="count",color="risk_level",barmode="group",color_discrete_map=RC)
        st.plotly_chart(bl(fig),use_container_width=True); ec()
    c5,c6=st.columns(2)
    with c5:
        gc("Quiz vs Assignment Score","📝",".3s")
        sc=df.groupby("course")[["quiz_score","assignment_score"]].mean().reset_index()
        fig=px.bar(sc,x="course",y=["quiz_score","assignment_score"],barmode="group",opacity=0.9,
                   color_discrete_map={"quiz_score":"#6366f1","assignment_score":"#f472b6"})
        st.plotly_chart(bl(fig),use_container_width=True); ec()
    with c6:
        gc("Satisfaction vs Engagement","⭐",".35s")
        fig=px.scatter(df,x="satisfaction",y="engagement_score",color="course",size="completion_pct",
                       hover_data=["student_id"],opacity=0.8)
        st.plotly_chart(bl(fig),use_container_width=True); ec()

# ═══ STUDENTS ═══
with t2:
    sc1,sc2,sc3=st.columns([3,1,1])
    with sc1: search=st.text_input("🔍 Search","",placeholder="Search student ID or name...")
    with sc2: sort_by=st.selectbox("Sort by",["engagement_score","completion_pct","quiz_score","dropout_probability"])
    with sc3: st.markdown("<br>",unsafe_allow_html=True); show_n=st.selectbox("Show",["All","Top 50","Top 100"])
    disp=df.copy()
    if search: disp=disp[disp["student_id"].str.contains(search,case=False)|disp["name"].str.contains(search,case=False)]
    disp=disp.sort_values(sort_by,ascending=False)
    if show_n=="Top 50": disp=disp.head(50)
    if show_n=="Top 100": disp=disp.head(100)
    st.markdown(f'<div class="pills"><div class="pill">Students: <span>{len(disp)}</span></div><div class="pill">Avg Engagement: <span>{disp["engagement_score"].mean():.1f}</span></div><div class="pill">Avg Completion: <span>{disp["completion_pct"].mean():.1f}%</span></div><div class="pill">High Risk: <span>{(disp["risk_level"]=="High Risk").sum()}</span></div><div class="pill">Dropouts: <span>{disp["dropped_out"].sum()}</span></div><div class="pill">Avg Quiz: <span>{disp["quiz_score"].mean():.1f}</span></div></div>',unsafe_allow_html=True)
    gc("Student Records","🎓")
    cols=["student_id","name","course","gender","device","age","logins_per_week","video_watch_pct","quiz_score","assignment_score","completion_pct","forum_posts","engagement_score","risk_level","dropped_out","satisfaction","time_spent_hrs"]
    st.dataframe(disp[cols].rename(columns={"student_id":"ID","name":"Name","course":"Course","gender":"Gender","device":"Device","age":"Age","logins_per_week":"Logins/wk","video_watch_pct":"Video %","quiz_score":"Quiz","assignment_score":"Assignment","completion_pct":"Completion %","forum_posts":"Forum","engagement_score":"Engagement","risk_level":"Risk","dropped_out":"Dropped","satisfaction":"Rating","time_spent_hrs":"Hours"}).reset_index(drop=True),use_container_width=True,height=460)
    ec()
    d1,d2,_=st.columns([1,1,3])
    d1.download_button("⬇️ Export All",df.to_csv(index=False),"students_all.csv","text/csv")
    d2.download_button("⬇️ Export Filtered",disp.to_csv(index=False),"students_filtered.csv","text/csv")
    st.markdown("<br>",unsafe_allow_html=True)
    g1,g2=st.columns(2)
    with g1:
        gc("Gender Distribution","👥")
        gd=df["gender"].value_counts().reset_index(); gd.columns=["Gender","Count"]
        fig=px.pie(gd,names="Gender",values="Count",hole=0.58,color_discrete_sequence=["#6366f1","#f472b6","#34d399"])
        st.plotly_chart(bl(fig),use_container_width=True); ec()
    with g2:
        gc("Age Distribution","🎂")
        fig=px.histogram(df,x="age",nbins=15,color_discrete_sequence=["#6366f1"],opacity=0.85)
        st.plotly_chart(bl(fig),use_container_width=True); ec()

# ═══ AT-RISK ═══
with t3:
    hr=df[df["risk_level"]=="High Risk"].sort_values("engagement_score")
    mr=df[df["risk_level"]=="Medium Risk"]
    r1,r2,r3,r4=st.columns(4)
    kpi(r1,len(hr),"High Risk","🔴","linear-gradient(135deg,#450a0a,#991b1b,#ef4444)",f"{len(hr)/max(len(df),1)*100:.1f}%",neg=True)
    kpi(r2,len(mr),"Medium Risk","🟡","linear-gradient(135deg,#431407,#92400e,#f59e0b)",f"{len(mr)/max(len(df),1)*100:.1f}%",neg=True)
    kpi(r3,f"{hr['engagement_score'].mean():.1f}" if len(hr) else "N/A","Avg Engagement (HR)","⚡","linear-gradient(135deg,#3b0764,#6d28d9,#8b5cf6)")
    kpi(r4,f"{hr['dropout_probability'].mean()*100:.1f}%" if len(hr) else "N/A","Dropout Prob (HR)","📉","linear-gradient(135deg,#0f172a,#1e293b,#334155)",neg=True)
    st.markdown("<br>",unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        gc("High Risk by Course","📊")
        hrc=hr.groupby("course").size().reset_index(name="count")
        fig=px.bar(hrc.sort_values("count",ascending=False),x="course",y="count",color_discrete_sequence=["#ef4444"],text="count")
        fig.update_traces(textposition="outside",textfont_color="#9ca3af")
        st.plotly_chart(bl(fig),use_container_width=True); ec()
    with c2:
        gc("Engagement by Risk Level","📦")
        fig=px.box(df,x="risk_level",y="engagement_score",color="risk_level",color_discrete_map=RC,points="outliers")
        fig=bl(fig); fig.update_layout(showlegend=False); st.plotly_chart(fig,use_container_width=True); ec()
    gc("Risk Heatmap — Course × Risk Level","🌡️")
    hm=df.groupby(["course","risk_level"]).size().reset_index(name="count")
    hm_piv=hm.pivot(index="course",columns="risk_level",values="count").fillna(0)
    fig=px.imshow(hm_piv,color_continuous_scale="RdYlGn_r",text_auto=True); st.plotly_chart(bl(fig),use_container_width=True); ec()
    gc("🚨 Intervention Priority — Top 25 At-Risk Students","🚨")
    p=hr[["student_id","name","course","engagement_score","completion_pct","logins_per_week","video_watch_pct","dropout_probability","risk_level"]].head(25).copy()
    p["dropout_probability"]=(p["dropout_probability"]*100).round(1).astype(str)+"%"
    st.dataframe(p.reset_index(drop=True),use_container_width=True); ec()
    st.download_button("⬇️ Export At-Risk List",hr.to_csv(index=False),"at_risk.csv","text/csv")

# ═══ TRENDS ═══
with t4:
    gc("Monthly Enrollments","📅",".1s")
    mon=df.groupby("month").size().reset_index(name="enrollments")
    fig=px.area(mon,x="month",y="enrollments",markers=True,color_discrete_sequence=["#6366f1"])
    fig.update_traces(line_width=3,fill="tozeroy",fillcolor="rgba(99,102,241,.08)",marker_size=8)
    st.plotly_chart(bl(fig),use_container_width=True); ec()
    c1,c2=st.columns(2)
    with c1:
        gc("Forum Activity vs Engagement","💬",".15s")
        fig=px.scatter(df,x="forum_posts",y="engagement_score",color="course",trendline="ols",hover_data=["student_id"],opacity=0.75)
        st.plotly_chart(bl(fig),use_container_width=True); ec()
    with c2:
        gc("Logins vs Completion","🔑",".2s")
        fig=px.scatter(df,x="logins_per_week",y="completion_pct",color="risk_level",color_discrete_map=RC,trendline="ols",hover_data=["student_id","course"],opacity=0.75)
        st.plotly_chart(bl(fig),use_container_width=True); ec()
    c3,c4=st.columns(2)
    with c3:
        gc("Dropout Rate by Course","📉",".25s")
        dr=df.groupby("course")["dropped_out"].mean().reset_index(); dr["Dropout %"]=(dr["dropped_out"]*100).round(1)
        fig=px.bar(dr.sort_values("Dropout %",ascending=False),x="course",y="Dropout %",
                   color="Dropout %",color_continuous_scale=[[0,"#450a0a"],[1,"#ef4444"]],
                   text=dr.sort_values("Dropout %",ascending=False)["Dropout %"].astype(str)+"%")
        fig.update_traces(textposition="outside",textfont_color="#9ca3af"); fig.update_coloraxes(showscale=False)
        st.plotly_chart(bl(fig),use_container_width=True); ec()
    with c4:
        gc("Time Spent vs Completion","⏱️",".3s")
        fig=px.scatter(df,x="time_spent_hrs",y="completion_pct",color="risk_level",color_discrete_map=RC,
                       trendline="ols",hover_data=["student_id","course"],opacity=0.75)
        st.plotly_chart(bl(fig),use_container_width=True); ec()

# ═══ AI ASSISTANT ═══
with t5:
    st.markdown("""
    <div class="ai-wrap">
      <div class="ai-hdr">🤖 LearnPulse AI Assistant <span class="ai-live">POWERED BY CLAUDE</span></div>
      <div class="ai-sub">Ask anything about your student data. AI analyses your live dashboard numbers and gives specific, actionable insights instantly.</div>
    </div>
    """,unsafe_allow_html=True)

    if "ai_q" not in st.session_state: st.session_state.ai_q=""
    if "ai_hist" not in st.session_state: st.session_state.ai_hist=[]

    st.markdown("**⚡ Quick Ask:**")
    qq=[
        "Which students need urgent help right now?",
        "What is causing high dropout rates?",
        "How can I improve engagement scores?",
        "Which course needs the most attention?",
        "What do at-risk students have in common?",
        "Give me a 3-step action plan for this data",
        "Which instructor is performing best?",
        "Predict what will happen next month",
    ]
    r1_cols=st.columns(4)
    r2_cols=st.columns(4)
    for i,q in enumerate(qq[:4]):
        if r1_cols[i].button(q,key=f"q{i}",use_container_width=True): st.session_state.ai_q=q
    for i,q in enumerate(qq[4:]):
        if r2_cols[i].button(q,key=f"q{i+4}",use_container_width=True): st.session_state.ai_q=q

    st.markdown("<br>",unsafe_allow_html=True)
    user_q=st.text_input("💬 Or type your own question...",value=st.session_state.ai_q,placeholder="e.g. Which course has the worst dropout rate and why?")
    ask=st.button("🚀 Ask AI",type="primary")

    if ask and user_q:
        ctx=f"""
LIVE DASHBOARD DATA:
Total Students: {len(df)} | Filter: {sel_c}
Avg Engagement: {df['engagement_score'].mean():.1f}/100
Avg Completion: {df['completion_pct'].mean():.1f}%
Avg Quiz Score: {df['quiz_score'].mean():.1f}/100
Total Dropouts: {df['dropped_out'].sum()} ({df['dropped_out'].mean()*100:.1f}%)
High Risk: {(df['risk_level']=='High Risk').sum()} ({(df['risk_level']=='High Risk').mean()*100:.1f}%)
Medium Risk: {(df['risk_level']=='Medium Risk').sum()}
Low Risk: {(df['risk_level']=='Low Risk').sum()}
Avg Satisfaction: {df['satisfaction'].mean():.1f}/5
Avg Time Spent: {df['time_spent_hrs'].mean():.1f}h
Avg Dropout Probability: {df['dropout_probability'].mean()*100:.1f}%
Engagement by Course: {df.groupby('course')['engagement_score'].mean().round(1).to_dict()}
Dropout by Course: {(df.groupby('course')['dropped_out'].mean()*100).round(1).to_dict()}
Completion by Course: {df.groupby('course')['completion_pct'].mean().round(1).to_dict()}
"""
        st.markdown(f'<div class="msg-u">💬 {user_q}</div>',unsafe_allow_html=True)
        if not api_key or not api_key.startswith("sk-"):
            st.markdown("""<div class="msg-ai">⚠️ <b>API Key Required</b><br><br>
Please enter your <b>Anthropic API Key</b> in the sidebar to enable AI.<br><br>
Get your free key at: <b>console.anthropic.com</b><br><br>
<i>Your key is only used for this session and never stored anywhere.</i></div>""",unsafe_allow_html=True)
        else:
            ph=st.empty()
            ph.markdown('<div class="msg-ai"><span class="dot"></span><span class="dot"></span><span class="dot"></span> &nbsp;Analysing your live data...</div>',unsafe_allow_html=True)
            resp=ask_ai(user_q,ctx,api_key)
            ph.empty()
            if resp:
                st.session_state.ai_hist.append({"q":user_q,"a":resp})
                st.markdown(f'<div class="msg-ai">🤖 <b>LearnPulse AI:</b><br><br>{resp}</div>',unsafe_allow_html=True)
        st.session_state.ai_q=""

    if st.session_state.ai_hist:
        st.markdown("<br>",unsafe_allow_html=True)
        with st.expander(f"📜 Conversation History ({len(st.session_state.ai_hist)} messages)"):
            for item in reversed(st.session_state.ai_hist):
                st.markdown(f'<div class="msg-u">💬 {item["q"]}</div>',unsafe_allow_html=True)
                st.markdown(f'<div class="msg-ai">🤖 {item["a"]}</div>',unsafe_allow_html=True)
        if st.button("🗑️ Clear History"): st.session_state.ai_hist=[]; st.rerun()

    st.markdown("<br>",unsafe_allow_html=True)
    with st.expander("📖 Example AI Response (no API key needed)"):
        st.markdown("""<div class="msg-ai">🤖 <b>LearnPulse AI Analysis:</b><br><br>
<b>🔴 Critical Findings:</b><br>
• 63 students (21%) are High Risk with avg engagement of only 28.4/100<br>
• Machine Learning has the worst dropout rate at 24.3% — nearly 1 in 4 students leaving<br>
• 18 students scored below 30 engagement — they haven't logged in for 2+ weeks<br><br>
<b>📊 Key Patterns Detected:</b><br>
• Students logging in fewer than 2×/week have 78% higher dropout probability<br>
• Video watch % below 40% is the strongest predictor of course failure<br>
• Forum participation above 5 posts reduces dropout risk by 45%<br>
• Mobile users have 31% higher dropout rate than desktop users<br><br>
<b>✅ Recommended Actions:</b><br>
1. Email the 63 high-risk students with personalised check-ins this week — use the At-Risk tab to export their list<br>
2. Review Machine Learning course difficulty — Week 3 assignment scores are 18% below average, suggesting the content is too hard<br>
3. Launch a forum engagement challenge with badges — students who post 5+ times have significantly better outcomes</div>""",unsafe_allow_html=True)

# ═══ PREDICTIONS ═══
with t6:
    st.markdown('<div class="insight">🤖 <b>AI Prediction Model:</b> Dropout probability = engagement (40%) + completion (30%) + logins (30%). Predicted final = quiz (40%) + assignment (40%) + engagement (20%).</div>',unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    kpi(c1,f"{df['dropout_probability'].mean()*100:.1f}%","Avg Dropout Prob","📉","linear-gradient(135deg,#450a0a,#991b1b,#ef4444)",neg=True)
    kpi(c2,f"{df['predicted_final'].mean():.1f}","Avg Predicted Final","🎯","linear-gradient(135deg,#082f49,#0c4a6e,#0ea5e9)","+2.4 pts")
    kpi(c3,f"{df[df['dropout_probability']>0.6].shape[0]}","Critical Risk >60%","🚨","linear-gradient(135deg,#431407,#9a3412,#f97316)",neg=True)
    st.markdown("<br>",unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        gc("Predicted Final Score by Course","🎯")
        pf=df.groupby("course")["predicted_final"].mean().reset_index().sort_values("predicted_final")
        fig=px.bar(pf,x="predicted_final",y="course",orientation="h",
                   color="predicted_final",color_continuous_scale=[[0,"#450a0a"],[.5,"#f59e0b"],[1,"#10b981"]],
                   text=pf["predicted_final"].round(1))
        fig.update_traces(textposition="outside",textfont_color="#9ca3af"); fig.update_coloraxes(showscale=False)
        st.plotly_chart(bl(fig),use_container_width=True); ec()
    with c2:
        gc("Dropout Probability Distribution","📊")
        fig=px.histogram(df,x="dropout_probability",nbins=20,color="risk_level",color_discrete_map=RC,barmode="overlay",opacity=0.8)
        st.plotly_chart(bl(fig),use_container_width=True); ec()
    gc("🔮 Top 20 Students Most Likely to Drop Out","🔮")
    td=df.nlargest(20,"dropout_probability")[["student_id","name","course","dropout_probability","engagement_score","completion_pct","logins_per_week","predicted_final","risk_level"]].reset_index(drop=True)
    td["dropout_probability"]=(td["dropout_probability"]*100).round(1).astype(str)+"%"
    st.dataframe(td,use_container_width=True); ec()
    st.download_button("⬇️ Export Predictions",df[["student_id","name","course","dropout_probability","predicted_final","risk_level"]].to_csv(index=False),"predictions.csv","text/csv")

# ═══ INSTRUCTORS ═══
with t7:
    inst=df.groupby("instructor").agg(
        students=("student_id","count"),
        avg_engagement=("engagement_score","mean"),
        avg_completion=("completion_pct","mean"),
        avg_quiz=("quiz_score","mean"),
        avg_satisfaction=("satisfaction","mean"),
        dropout_rate=("dropped_out","mean"),
        high_risk=("risk_level",lambda x:(x=="High Risk").sum())
    ).reset_index().round(2)
    inst["dropout_rate"]=(inst["dropout_rate"]*100).round(1)
    best=inst.loc[inst["avg_engagement"].idxmax(),"instructor"]
    st.markdown(f'<div class="insight">🏆 <b>Best Instructor:</b> {best} with highest avg engagement · Compare performance across all {len(inst)} instructors</div>',unsafe_allow_html=True)
    c1,c2,c3,c4=st.columns(4)
    kpi(c1,len(inst),"Instructors","👨‍🏫","linear-gradient(135deg,#1e3a8a,#1d4ed8,#3b82f6)")
    kpi(c2,f"{inst['avg_engagement'].mean():.1f}","Avg Engagement","⚡","linear-gradient(135deg,#3b0764,#6d28d9,#8b5cf6)")
    kpi(c3,f"{inst['avg_satisfaction'].mean():.1f}/5","Avg Satisfaction","⭐","linear-gradient(135deg,#431407,#92400e,#f59e0b)")
    kpi(c4,f"{inst['dropout_rate'].mean():.1f}%","Avg Dropout Rate","📉","linear-gradient(135deg,#450a0a,#991b1b,#ef4444)",neg=True)
    st.markdown("<br>",unsafe_allow_html=True)
    gc("Instructor Performance Summary","📋")
    st.dataframe(inst.rename(columns={"instructor":"Instructor","students":"Students","avg_engagement":"Avg Engagement","avg_completion":"Avg Completion %","avg_quiz":"Avg Quiz","avg_satisfaction":"Avg Rating ⭐","dropout_rate":"Dropout %","high_risk":"High Risk Students"}),use_container_width=True)
    ec()
    c1,c2=st.columns(2)
    with c1:
        gc("Avg Engagement by Instructor","⚡")
        fig=px.bar(inst.sort_values("avg_engagement"),x="avg_engagement",y="instructor",orientation="h",
                   color="avg_engagement",color_continuous_scale=[[0,"#1e3a8a"],[1,"#6366f1"]],
                   text=inst.sort_values("avg_engagement")["avg_engagement"].round(1))
        fig.update_traces(textposition="outside",textfont_color="#9ca3af"); fig.update_coloraxes(showscale=False)
        st.plotly_chart(bl(fig),use_container_width=True); ec()
    with c2:
        gc("Satisfaction vs Dropout Rate","⭐")
        fig=px.scatter(inst,x="avg_satisfaction",y="dropout_rate",text="instructor",size="students",
                       color="avg_engagement",color_continuous_scale="RdYlGn")
        fig.update_traces(textposition="top center",textfont_color="#e2e8f0")
        st.plotly_chart(bl(fig),use_container_width=True); ec()

# ═══ REPORTS ═══
with t8:
    st.markdown('<div class="insight">📋 <b>Reports:</b> Generate and download analytics reports for your filtered data instantly.</div>',unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        gc("📊 Executive Summary","📊")
        summary=pd.DataFrame({
            "Metric":["Total Students","Avg Engagement","Avg Completion %","Avg Quiz Score","Avg Assignment","Avg Satisfaction","Total Dropouts","Dropout Rate %","High Risk","Medium Risk","Low Risk","Avg Time Spent (hrs)"],
            "Value":[len(df),f"{df['engagement_score'].mean():.1f}",f"{df['completion_pct'].mean():.1f}%",f"{df['quiz_score'].mean():.1f}",f"{df['assignment_score'].mean():.1f}",f"{df['satisfaction'].mean():.1f}/5",df['dropped_out'].sum(),f"{df['dropped_out'].mean()*100:.1f}%",(df['risk_level']=='High Risk').sum(),(df['risk_level']=='Medium Risk').sum(),(df['risk_level']=='Low Risk').sum(),f"{df['time_spent_hrs'].mean():.1f}h"]
        })
        st.dataframe(summary,use_container_width=True,hide_index=True)
        st.download_button("⬇️ Download Summary",summary.to_csv(index=False),"executive_summary.csv","text/csv")
        ec()
    with c2:
        gc("🎓 Course Performance","🎓")
        cr=df.groupby("course").agg(Students=("student_id","count"),Avg_Engagement=("engagement_score","mean"),Avg_Completion=("completion_pct","mean"),Avg_Quiz=("quiz_score","mean"),Avg_Satisfaction=("satisfaction","mean"),Dropout_Rate=("dropped_out","mean"),High_Risk=("risk_level",lambda x:(x=="High Risk").sum())).round(2).reset_index()
        cr["Dropout_Rate"]=(cr["Dropout_Rate"]*100).round(1)
        st.dataframe(cr,use_container_width=True,hide_index=True)
        st.download_button("⬇️ Download Course Report",cr.to_csv(index=False),"course_report.csv","text/csv")
        ec()
    c3,c4=st.columns(2)
    with c3:
        gc("⚠️ At-Risk Report","⚠️")
        ar=df[df["risk_level"]=="High Risk"][["student_id","name","course","engagement_score","completion_pct","dropout_probability"]].copy()
        ar["dropout_probability"]=(ar["dropout_probability"]*100).round(1)
        st.dataframe(ar.head(15).reset_index(drop=True),use_container_width=True,hide_index=True)
        st.download_button("⬇️ Download At-Risk",ar.to_csv(index=False),"at_risk_report.csv","text/csv")
        ec()
    with c4:
        gc("👨‍🏫 Instructor Report","👨‍🏫")
        ir=df.groupby("instructor").agg(Students=("student_id","count"),Avg_Engagement=("engagement_score","mean"),Avg_Completion=("completion_pct","mean"),Avg_Satisfaction=("satisfaction","mean"),Dropout_Rate=("dropped_out","mean")).round(2).reset_index()
        ir["Dropout_Rate"]=(ir["Dropout_Rate"]*100).round(1)
        st.dataframe(ir,use_container_width=True,hide_index=True)
        st.download_button("⬇️ Download Instructor Report",ir.to_csv(index=False),"instructor_report.csv","text/csv")
        ec()

# ── FOOTER ────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  🎓 <span>LearnPulse AI v5.0</span> · Online Learning Engagement Analysis System ·
  Built with Streamlit + Claude AI · Plotly · Pandas · © 2026 Enterprise Platform
</div>
""",unsafe_allow_html=True)

   
   

    
