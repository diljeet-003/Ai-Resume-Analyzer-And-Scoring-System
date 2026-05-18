import streamlit as st
from utils import extract_text
from courses import *
from skills import SKILLS_DB
import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import base64
import plotly.graph_objects as go

# -------- PAGE CONFIG --------
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# -------- ADVANCED UI CSS --------
st.markdown("""
<style>

/* ===== FULL BACKGROUND LAYER ===== */
.stApp {
    background: linear-gradient(135deg, #eef2ff, #f0fdfa, #f8fafc);
    background-attachment: fixed;
}

/* ===== MAIN FRAME (BORDER AROUND WHOLE APP) ===== */
.main {
    background: rgba(255,255,255,0.6);
    padding: 20px;
    border-radius: 20px;
    border: 1px solid rgba(99,102,241,0.2);
    box-shadow: 0px 15px 40px rgba(0,0,0,0.1);
}

/* ===== LIMIT WIDTH ===== */
.block-container {
    max-width: 1000px;
    margin: auto;
}

/* ===== CARD ===== */
.card {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(12px);
    padding: 22px;
    border-radius: 18px;
    margin-top: 22px;
    margin-bottom: 22px;
    border: 1px solid rgba(255,255,255,0.4);
    box-shadow: 0px 10px 30px rgba(0,0,0,0.08);
    transition: 0.3s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0px 14px 35px rgba(0,0,0,0.12);
}

/* ===== TITLES ===== */
.card-title {
    font-size: 26px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 12px;
    color: #1e3a8a;
}

.subtitle {
    text-align: center;
    font-size: 32px;
    margin-bottom: 25px;
    color: #0f172a;
    font-weight: 700;
}

/* ===== UPLOADER ===== */
[data-testid="stFileUploader"] {
    border: 2px dashed #6366f1;
    border-radius: 14px;
    padding: 18px;
    background-color: #f8fafc;
}

/* ===== SKILLS ===== */
.skill {
    display: inline-block;
    background: linear-gradient(135deg, #6366f1, #06b6d4);
    color: white;
    padding: 6px 14px;
    margin: 6px;
    border-radius: 20px;
    font-size: 13px;
}

/* ===== PROGRESS ===== */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #6366f1, #06b6d4);
}

</style>
""", unsafe_allow_html=True)

# -------- HERO --------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("assets/logo.png", width=400)

st.markdown("<div class='subtitle'>  AI Resume Analyzer And Scoring System</div>", unsafe_allow_html=True)

# -------- INPUT --------
st.markdown("<h3 style='text-align:center; font-weight:800; color:#1e3a8a;'>📤 Upload Your Resume</h3>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
job_role = st.text_input("Enter Target Job Role")

# -------- PDF PREVIEW --------
def show_pdf(file):
    file.seek(0)
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}"
    width="100%" height="520"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

# -------- MAIN --------
if uploaded_file:

    # ===== PREVIEW =====
    st.markdown("<div class='card'><div class='card-title'>📄 Resume Preview</div>", unsafe_allow_html=True)

    if uploaded_file.type == "application/pdf":
        show_pdf(uploaded_file)
    else:
        st.info("Preview only available for PDF files")

    st.markdown("</div>", unsafe_allow_html=True)

    uploaded_file.seek(0)
    text = extract_text(uploaded_file)

    # ===== SKILLS =====
    st.markdown("<div class='card'><div class='card-title'>💡 Detected Skills</div>", unsafe_allow_html=True)

    detected_skills = [skill for skill in SKILLS_DB if skill.lower() in text.lower()]

    if detected_skills:
        st.markdown("".join([f"<span class='skill'>{s}</span>" for s in detected_skills]), unsafe_allow_html=True)
    else:
        st.warning("No skills detected")

    st.markdown("</div>", unsafe_allow_html=True)

    # ===== ROLE =====
    if "machine learning" in text or "data science" in text:
        job = "Data Scientist"
        courses = ds_course
    elif "android" in text:
        job = "Android Developer"
        courses = android_course
    elif "html" in text or "css" in text:
        job = "Web Developer"
        courses = web_course
    else:
        job = "General IT Role"
        courses = []

    st.markdown("<div class='card'><div class='card-title'>💼 Recommended Role</div>", unsafe_allow_html=True)
    st.success(job)
    st.markdown("</div>", unsafe_allow_html=True)

    # ===== MATCH =====
    if job_role:
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([text, job_role.lower()])
        similarity = cosine_similarity(vectors)[0][1]
        match_percentage = round(similarity * 100, 2)

        st.markdown("<div class='card'><div class='card-title'>🎯 Match Score</div>", unsafe_allow_html=True)
        st.progress(int(match_percentage))
        st.info(f"{match_percentage}% Match with Job Role")
        st.markdown("</div>", unsafe_allow_html=True)

        # ===== DASHBOARD =====
        st.markdown("<div class='card'><div class='card-title'>📊 Match Dashboard</div>", unsafe_allow_html=True)

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=match_percentage,
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#6366f1"},
                'steps': [
                    {'range': [0, 40], 'color': "#e0e7ff"},
                    {'range': [40, 70], 'color': "#a5b4fc"},
                    {'range': [70, 100], 'color': "#6366f1"}
                ],
            },
            number={'font': {'size': 32}}
        ))

        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ===== SCORE =====
    score = sum([
        "project" in text,
        "skill" in text,
        "experience" in text,
        "education" in text,
        "objective" in text
    ]) * 20

    st.markdown("<div class='card'><div class='card-title'>📝 Resume Score</div>", unsafe_allow_html=True)
    st.progress(score)
    st.success(f"{score}/100")
    st.markdown("</div>", unsafe_allow_html=True)

    # ===== COURSES =====
    st.markdown("<div class='card'><div class='card-title'>🎓 Recommended Courses</div>", unsafe_allow_html=True)

    for c in courses:
        st.markdown(f"<div style='text-align:center;'>• {c[0]}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ===== VIDEOS =====
    st.markdown("<div class='card'><div class='card-title'>🎥 Career Tips</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.video(random.choice(resume_videos))
    with col2:
        st.video(random.choice(interview_videos))

    st.markdown("</div>", unsafe_allow_html=True)