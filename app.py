import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Online Learning Engagement Analysis System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f5f7fb;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #143dff 0%,
        #2563eb 50%,
        #4f8dfd 100%
    );
}

[data-testid="stSidebar"] * {
    color: white;
}

/* HERO SECTION */

.hero-section {
    background: linear-gradient(
        135deg,
        #edf4ff 0%,
        #f5ebff 100%
    );
    border-radius: 28px;
    padding: 45px;
    margin-bottom: 28px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
}

/* KPI CARDS */

.kpi-card {
    background: white;
    border-radius: 24px;
    padding: 22px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.05);
    text-align: center;
    transition: 0.3s;
}

.kpi-card:hover {
    transform: translateY(-5px);
}

.kpi-number {
    font-size: 42px;
    font-weight: 800;
}

.kpi-title {
    font-size: 15px;
    font-weight: 600;
    color: #64748b;
}

.kpi-sub {
    font-size: 14px;
    color: #94a3b8;
}

/* CHART CARDS */

.chart-card {
    background: white;
    border-radius: 24px;
    padding: 24px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
    margin-bottom: 24px;
}

/* TABS */

.stTabs [data-baseweb="tab-list"] {
    gap: 16px;
}

.stTabs [data-baseweb="tab"] {
    background: white;
    border-radius: 12px;
    padding: 14px 28px;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    background: #2563eb !important;
    color: white !important;
}

/* FOOTER */

.footer {
    text-align:center;
    color:#64748b;
    padding:20px;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SAMPLE DATA
# =========================================================

@st.cache_data
def load_data():

    random.seed(42)
    np.random.seed(42)

    n = 300

    courses = [
        "Python Basics",
        "Data Science",
        "Machine Learning",
        "Cloud Computing",
        "Web Development"
    ]

    df = pd.DataFrame({

        "student_id": [
            f"Student_{i:03d}"
            for i in range(1, n + 1)
        ],

        "course": np.random.choice(courses, n),

        "engagement_score": np.random.randint(40, 95, n),

        "completion_pct": np.random.randint(20, 100, n),

        "risk_level": np.random.choice(
            ["Low Risk", "Medium Risk", "High Risk"],
            n,
            p=[0.45, 0.35, 0.20]
        ),

        "dropped_out": np.random.choice(
            [True, False],
            n,
            p=[0.2, 0.8]
        )

    })

    return df

df = load_data()

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div style='text-align:center;padding-top:20px;'>

    <div style='font-size:70px;'>🎓</div>

    <h1 style='margin-bottom:0;'>LearnPulse</h1>

    <p style='font-size:15px;margin-top:5px;font-weight:600;'>
    Online Learning Intelligence Platform
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("## Filters")

    selected_course = st.selectbox(
        "Select Course",
        ["All Courses"] + list(df["course"].unique())
    )

    selected_risk = st.selectbox(
        "Risk Level",
        ["All", "Low Risk", "Medium Risk", "High Risk"]
    )

    engagement_range = st.slider(
        "Engagement Score",
        0,
        100,
        (0, 100)
    )

    include_dropouts = st.checkbox(
        "Include Dropouts",
        value=True
    )

# =========================================================
# FILTER LOGIC
# =========================================================

filtered_df = df.copy()

# Course Filter
if selected_course != "All Courses":
    filtered_df = filtered_df[
        filtered_df["course"] == selected_course
    ]

# Risk Filter
if selected_risk != "All":
    filtered_df = filtered_df[
        filtered_df["risk_level"] == selected_risk
    ]

# Engagement Score Filter
filtered_df = filtered_df[
    (
        filtered_df["engagement_score"]
        >= engagement_range[0]
    )
    &
    (
        filtered_df["engagement_score"]
        <= engagement_range[1]
    )
]

# Dropout Filter
if not include_dropouts:
    filtered_df = filtered_df[
        filtered_df["dropped_out"] == False
    ]

# Empty Check
if filtered_df.empty:
    st.warning("No data available for selected filters.")
    st.stop()

# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero-section">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
flex-wrap:wrap;
">

<div>

<div style="
display:flex;
align-items:center;
gap:25px;
">

<div style="
background:linear-gradient(135deg,#2563eb,#7c3aed);
padding:26px;
border-radius:24px;
font-size:50px;
color:white;
">

🎓

</div>

<div>

<h1 style="
margin:0;
font-size:54px;
font-weight:800;
line-height:1.2;
color:#1e40af;
letter-spacing:-1px;
">

Online Learning Engagement Analysis System

</h1>

<p style="
font-size:24px;
margin-top:18px;
font-weight:800;
letter-spacing:0.5px;
color:#000000;
display:block;
">

AI-Powered Online Learning Analytics Dashboard

</p>

</div>

</div>

</div>

<div style="
font-size:180px;
">
🎓
</div>

</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# KPI CARDS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(f"""
    <div class="kpi-card">

    <div style="font-size:42px;">👨‍🎓</div>

    <div class="kpi-title">
    Total Students
    </div>

    <div class="kpi-number" style="color:#2563eb;">
    {len(filtered_df)}
    </div>

    <div class="kpi-sub">
    Active learners
    </div>

    </div>
    """, unsafe_allow_html=True)

with col2:

    avg_engagement = round(filtered_df['engagement_score'].mean(), 1)

    st.markdown(f"""
    <div class="kpi-card">

    <div style="font-size:42px;">📈</div>

    <div class="kpi-title">
    Avg Engagement
    </div>

    <div class="kpi-number" style="color:#7c3aed;">
    {avg_engagement}
    </div>

    <div class="kpi-sub">
    Engagement Score
    </div>

    </div>
    """, unsafe_allow_html=True)

with col3:

    avg_completion = round(filtered_df['completion_pct'].mean(), 1)

    st.markdown(f"""
    <div class="kpi-card">

    <div style="font-size:42px;">🏆</div>

    <div class="kpi-title">
    Completion
    </div>

    <div class="kpi-number" style="color:#16a34a;">
    {avg_completion}%
    </div>

    <div class="kpi-sub">
    Average Completion
    </div>

    </div>
    """, unsafe_allow_html=True)

with col4:

    dropout_count = filtered_df['dropped_out'].sum()

    st.markdown(f"""
    <div class="kpi-card">

    <div style="font-size:42px;">⚠️</div>

    <div class="kpi-title">
    Dropouts
    </div>

    <div class="kpi-number" style="color:#dc2626;">
    {dropout_count}
    </div>

    <div class="kpi-sub">
    At Risk Students
    </div>

    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3 = st.tabs([
    "📊 Overview",
    "🎓 Students",
    "📈 Trends"
])

# =========================================================
# OVERVIEW TAB
# =========================================================

with tab1:

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

        st.subheader("Engagement by Course")

        avg = (
            filtered_df.groupby("course")["engagement_score"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            avg,
            x="course",
            y="engagement_score",
            color="engagement_score",
            color_continuous_scale="Blues"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with c2:

        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

        st.subheader("Risk Distribution")

        risk = (
            filtered_df["risk_level"]
            .value_counts()
            .reset_index()
        )

        risk.columns = ["Risk", "Count"]

        fig = px.pie(
            risk,
            names="Risk",
            values="Count",
            hole=0.6
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# STUDENTS TAB
# =========================================================

with tab2:

    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

    st.subheader("Recent Students")

    st.dataframe(
        filtered_df.head(10),
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# TRENDS TAB
# =========================================================

with tab3:

    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

    st.subheader("Monthly Enrollments")

    months = pd.DataFrame({
        "Month": [
            "Jan", "Feb", "Mar",
            "Apr", "May", "Jun", "Jul"
        ],
        "Enrollments": [45, 55, 80, 66, 60, 70, 74]
    })

    fig = px.line(
        months,
        x="Month",
        y="Enrollments",
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class='footer'>

© 2026 LearnPulse Intelligence Platform

</div>
""", unsafe_allow_html=True)
   

   
  
    
