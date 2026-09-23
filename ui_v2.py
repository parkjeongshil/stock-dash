from __future__ import annotations

import html
import streamlit as st


NAV_ITEMS = [
    ("홈", "⌂"),
    ("시장 현황", "▥"),
    ("종목 분석", "◫"),
    ("공시 분석", "▤"),
    ("테마 & 섹터", "◇"),
    ("포트폴리오", "▣"),
    ("관심 종목", "☆"),
    ("AI 인사이트", "✦"),
    ("데이터 연결 관리", "⚙"),
]


def apply_theme():
    st.markdown(
        """
<style>
:root{
  --bg:#06101f; --bg2:#08182b; --surface:#0b1b30; --surface2:#0e233d;
  --line:#173453; --line2:#24496f; --text:#edf5ff; --muted:#86a0bd;
  --blue:#168cff; --cyan:#26b7ff; --up:#ff466d; --down:#1597ff; --green:#20d3a1;
}
html,body,[class*="css"]{font-family:Pretendard,"Noto Sans KR","Apple SD Gothic Neo",sans-serif}
.stApp{background:radial-gradient(circle at 75% 0%,#102a49 0%,var(--bg) 42%,#040b15 100%);color:var(--text)}
.block-container{max-width:1760px;padding-top:1rem;padding-bottom:3rem}
header[data-testid="stHeader"]{background:rgba(5,14,27,.72);backdrop-filter:blur(16px)}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#061526 0%,#071b31 100%);border-right:1px solid var(--line)}
section[data-testid="stSidebar"]>div{padding-top:1rem}
[data-testid="stSidebar"] .stRadio>label{display:none}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"]{gap:5px}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label{
  border-radius:11px;padding:.55rem .65rem;color:#9bb4ce;transition:.15s;background:transparent
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover{background:#0d2743;color:#e9f5ff}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked){
  background:linear-gradient(90deg,#0c3762,#0b2948);color:#fff;font-weight:800;
  box-shadow:inset 3px 0 var(--blue)
}
h1,h2,h3,h4{color:var(--text);letter-spacing:-.035em}
h1{font-weight:850}h2,h3{font-weight:800}
p,li{line-height:1.55}
[data-testid="stCaptionContainer"],[data-testid="stCaptionContainer"] p{color:var(--muted)}
[data-testid="stMetric"]{
  background:linear-gradient(145deg,#0d223b,#091a2e);border:1px solid var(--line);
  border-radius:13px;padding:15px 17px;box-shadow:0 10px 28px rgba(0,0,0,.18)
}
[data-testid="stMetricLabel"]{color:#7795b5}
[data-testid="stMetricValue"]{color:#f2f7ff;font-weight:850}
[data-testid="stVerticalBlockBorderWrapper"]{
  border-color:var(--line)!important;border-radius:14px!important;
  background:linear-gradient(145deg,rgba(13,34,59,.96),rgba(8,24,42,.96));
  box-shadow:0 12px 30px rgba(0,0,0,.16)
}
.stButton>button,.stFormSubmitButton>button{
  border-radius:10px;min-height:2.65rem;font-weight:750;
  background:#0d2744;border:1px solid #1e4770;color:#eaf5ff
}
.stButton>button[kind="primary"],.stFormSubmitButton>button[kind="primary"]{
  background:linear-gradient(135deg,#087df0,#159eff);border-color:#159eff;color:#fff
}
.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb="select"]>div{
  border-radius:10px!important;background:#071a2e!important;border-color:#214667!important;color:#eef6ff!important
}
.stTabs [data-baseweb="tab-list"]{gap:6px;border-bottom:1px solid var(--line)}
.stTabs [data-baseweb="tab"]{border-radius:9px 9px 0 0;padding:9px 13px;color:#86a0bd}
.stTabs [aria-selected="true"]{color:#fff;background:#0c2947}
.stDataFrame{border:1px solid var(--line);border-radius:12px;overflow:hidden}
.planx-brand{display:flex;align-items:center;gap:11px;margin:3px 0 22px}
.planx-brand-mark{
 width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;
 background:linear-gradient(145deg,#087df0,#26b7ff);color:white;font-size:20px;font-weight:900;
 box-shadow:0 8px 22px rgba(22,140,255,.25)
}
.planx-brand-title{font-size:19px;line-height:1.1;font-weight:850;color:#f4f8ff;letter-spacing:-.03em}
.planx-brand-sub{font-size:10px;color:#6385a8;margin-top:3px}
.planx-hero{
 background:linear-gradient(135deg,rgba(10,31,53,.9),rgba(8,24,43,.9));
 border:1px solid var(--line);border-radius:18px;padding:23px 25px;margin-bottom:16px;
 box-shadow:0 16px 42px rgba(0,0,0,.18);position:relative;overflow:hidden
}
.planx-hero:after{
 content:"";position:absolute;right:-90px;top:-110px;width:300px;height:220px;
 background:radial-gradient(circle,rgba(22,140,255,.18),transparent 68%)
}
.planx-eyebrow{color:#36aaff;font-size:11px;font-weight:850;letter-spacing:.12em;text-transform:uppercase;margin-bottom:7px}
.planx-hero h1{margin:0;font-size:30px;line-height:1.18}
.planx-hero p{margin:8px 0 0;color:#8da7c2;font-size:13px;max-width:850px}
.planx-card{
 background:linear-gradient(145deg,#0d223b,#09192c);border:1px solid var(--line);border-radius:13px;
 padding:16px 17px;min-height:112px;box-shadow:0 10px 26px rgba(0,0,0,.14);position:relative;overflow:hidden
}
.planx-card:before{content:"";position:absolute;left:0;top:0;width:3px;height:100%;background:linear-gradient(#168cff,#26b7ff)}
.planx-card-title{font-size:11px;color:#7e9ab7;margin-bottom:8px;font-weight:750}
.planx-card-value{font-size:23px;color:#f3f8ff;font-weight:850;letter-spacing:-.035em}
.planx-card-note{margin-top:6px;font-size:10px;color:#6784a2}
.planx-empty{background:#091a2d;border:1px dashed #285174;border-radius:13px;padding:21px;color:#7f9ab6}
.planx-source{display:inline-flex;align-items:center;gap:5px;color:#8ba5c0;background:#0a2037;border:1px solid #214667;padding:4px 8px;border-radius:999px;font-size:10px}
.planx-status-ok{color:#53e2bd;background:#092d2a;border-color:#1a6657}
.planx-status-wait{color:#ffd36b;background:#33290e;border-color:#6b541c}
.planx-status-bad{color:#ff7891;background:#351522;border-color:#6d2940}
hr{border-color:var(--line)!important}
[data-testid="stAlert"]{background:#0c2035;border-color:#214667;color:#d9e9f8}
a{color:#51b6ff}
div[data-testid="stMarkdownContainer"] strong{color:#f0f6ff}
.market-up{color:var(--up)!important}.market-down{color:var(--down)!important}.market-flat{color:#8da7c2!important}
.dashboard-section{font-size:12px;color:#7694b2;font-weight:800;letter-spacing:.08em;text-transform:uppercase;margin:8px 0 10px}
.dash-heading{padding:12px 3px 18px}.dash-heading h1{font-size:clamp(26px,3vw,38px);margin:0 0 5px}.dash-heading p{color:var(--muted);margin:0}
.dash-panel{border:1px solid var(--line);background:linear-gradient(145deg,#0d223b,#09192c);border-radius:14px;padding:18px;min-height:136px}
.dash-panel-label{color:#a8c4df;font-size:13px;font-weight:750}.dash-panel-value{font-size:25px;font-weight:850;margin:11px 0 4px}.dash-panel-note{font-size:12px;color:var(--muted)}
.dash-placeholder{border:1px dashed #285174;border-radius:10px;padding:24px;color:#8ba5c0;background:#091a2d;margin-top:12px}
.dash-tag{font-size:11px;border:1px solid #315474;border-radius:100px;color:#9fbbd5;padding:3px 8px;margin-left:7px}
.dash-subtitle{font-weight:800;font-size:17px;margin:0 0 12px}.dash-positive{color:var(--up)}.dash-negative{color:var(--down)}
.dash-watch{border-bottom:1px solid var(--line);padding:9px 0;display:flex;justify-content:space-between;gap:10px;font-size:13px}.dash-watch:last-child{border:0}
.dash-chart-empty{height:285px;border:1px solid #204667;border-radius:10px;background:linear-gradient(160deg,#091d33,#071728);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;color:#91acc7;text-align:center;padding:18px;margin:14px 0}
.dash-chart-empty span{font-size:42px;color:#4886bf}.dash-chart-empty strong{font-size:17px;color:#d4e6f7}.dash-chart-empty small{font-size:12px}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:nth-child(1) p:before{content:"⌂"}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:nth-child(2) p:before{content:"▥"}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:nth-child(3) p:before{content:"◫"}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:nth-child(4) p:before{content:"▤"}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:nth-child(5) p:before{content:"◇"}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:nth-child(6) p:before{content:"◉"}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:nth-child(7) p:before{content:"♡"}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:nth-child(8) p:before{content:"✦"}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:nth-child(9) p:before{content:"☷"}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label p:before{display:inline-block;width:24px;margin-right:10px;color:#9bc8ff;font-size:18px}
@media(max-width:900px){.block-container{padding-left:1rem;padding-right:1rem}.planx-hero{padding:20px}.planx-hero h1{font-size:26px}}
</style>
""",
        unsafe_allow_html=True,
    )


def brand():
    st.markdown(
        """
<div class="planx-brand">
  <div class="planx-brand-mark">↗</div>
  <div>
    <div class="planx-brand-title">PLAN X</div>
    <div class="planx-brand-sub">더 넓은 시선, 더 나은 투자</div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


def hero(title: str, subtitle: str, eyebrow: str = "STOCK DASH"):
    st.markdown(
        f"""
<div class="planx-hero">
  <div class="planx-eyebrow">{html.escape(eyebrow)}</div>
  <h1>{html.escape(title)}</h1>
  <p>{html.escape(subtitle)}</p>
</div>
""",
        unsafe_allow_html=True,
    )


def card(title: str, value: str, note: str = "", status: str = ""):
    status_html = f'<div class="planx-card-note">{html.escape(status)}</div>' if status else ""
    st.markdown(
        f"""
<div class="planx-card">
  <div class="planx-card-title">{html.escape(title)}</div>
  <div class="planx-card-value">{html.escape(value)}</div>
  <div class="planx-card-note">{html.escape(note)}</div>
  {status_html}
</div>
""",
        unsafe_allow_html=True,
    )


def empty_state(title: str, message: str):
    st.markdown(
        f"""
<div class="planx-empty">
  <strong style="color:#edf5ff">{html.escape(title)}</strong><br>
  <span>{html.escape(message)}</span>
</div>
""",
        unsafe_allow_html=True,
    )


def source_badge(label: str, state: str = "wait"):
    cls = {"ok": "planx-status-ok", "bad": "planx-status-bad"}.get(state, "planx-status-wait")
    st.markdown(
        f'<span class="planx-source {cls}">{html.escape(label)}</span>',
        unsafe_allow_html=True,
    )
