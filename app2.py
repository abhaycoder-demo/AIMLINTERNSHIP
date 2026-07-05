import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AI Student Performance Advisor",
    page_icon="🎓",
    layout="wide"
)

pipeline = joblib.load("student_pipeline.pkl")

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp{
    background:linear-gradient(135deg,#0f172a,#1e293b);
    color:white;
}

/* Hide Streamlit Menu */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* Title */
.big-title{
    font-size:46px;
    font-weight:900;
    text-align:center;
    background:linear-gradient(90deg,#38bdf8,#22d3ee,#8b5cf6);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle{
    text-align:center;
    color:#d1d5db;
    font-size:18px;
    margin-bottom:30px;
}

/* Cards */
.card{
    background:rgba(255,255,255,.08);
    border:1px solid rgba(255,255,255,.15);
    border-radius:18px;
    padding:20px;
    box-shadow:0 8px 25px rgba(0,0,0,.35);
    backdrop-filter:blur(15px);
}

/* Labels */
h4{
    color:white !important;
    font-size:20px !important;
    font-weight:700 !important;
}

/* Button */
.stButton>button{
    width:100%;
    height:55px;
    border:none;
    border-radius:12px;
    background:linear-gradient(90deg,#2563eb,#06b6d4);
    color:white;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    transform:scale(1.02);
    transition:.3s;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#111827;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    "<div class='big-title'>🎓 AI Student Performance Advisor</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Smart AI System to Predict & Improve Student Performance</div>",
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📊 Project Information")
st.sidebar.success("🤖 Model : Linear Regression")
st.sidebar.info("🎯 Student Performance Prediction")
st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍💻 Developer")
st.sidebar.success("Abhay Kumar")

# ---------------- INPUT ----------------
col1,col2=st.columns(2)

with col1:

    st.markdown("<div class='card'>",unsafe_allow_html=True)

    st.markdown("<h4>📚 Study Hours</h4>",unsafe_allow_html=True)
    hours=st.slider("",0,12,6,key="hours")

    st.markdown("<h4>😴 Sleep Hours</h4>",unsafe_allow_html=True)
    sleep=st.slider("",0,12,7,key="sleep")

    st.markdown("<h4>🏫 Attendance %</h4>",unsafe_allow_html=True)
    attendance=st.slider("",0,100,80,key="attendance")

    st.markdown("</div>",unsafe_allow_html=True)

with col2:

    st.markdown("<div class='card'>",unsafe_allow_html=True)

    st.markdown("<h4>📝 Previous Score</h4>",unsafe_allow_html=True)
    previous=st.slider("",0,100,75,key="previous")

    st.markdown("<h4>📄 Practice Papers</h4>",unsafe_allow_html=True)
    papers=st.slider("",0,10,5,key="papers")

    st.write("")
    predict=st.button(
        "🚀 Predict Performance",
        use_container_width=True,
        type="primary"
    )

    st.markdown("</div>",unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
if predict:

    input_df = pd.DataFrame({
        "Hours Studied": [hours],
        "Previous Scores": [previous],
        "Sleep Hours": [sleep],
        "Sample Question Papers Practiced": [papers],
        "Attendance": [attendance]
    })

    score = float(pipeline.predict(input_df)[0])

    st.markdown("## 📊 AI Performance Dashboard")

    # ---------------- Gauge ----------------
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text":"Predicted Score"},
        gauge={
            "axis":{"range":[0,100]},
            "bar":{"color":"#22c55e"},
            "steps":[
                {"range":[0,50],"color":"#ef4444"},
                {"range":[50,75],"color":"#facc15"},
                {"range":[75,100],"color":"#22c55e"}
            ]
        }
    ))

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font={"color":"white","size":18},
        height=420
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---------------- Hero Cards ----------------

    st.markdown("## 📌 Student Performance Snapshot")

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.metric("🎯 Predicted Score",f"{score:.1f}")

    with c2:
        st.metric("📚 Study Hours",hours)

    with c3:
        st.metric("😴 Sleep Hours",sleep)

    with c4:
        st.metric("🏫 Attendance",f"{attendance}%")

    # ---------------- AI Analysis ----------------

    st.markdown("## 🤖 AI Analysis")

    if score>=90:
        st.success("🌟 Outstanding! You are expected to achieve excellent results.")

    elif score>=75:
        st.info("✅ Very Good Performance. A little more practice can make you excellent.")

    elif score>=60:
        st.warning("📘 Average Performance. Increase study hours and practice papers.")

    else:
        st.error("⚠️ Performance is below average. Immediate improvement is recommended.")

    # ---------------- Breakdown ----------------

    st.markdown("## 📈 Performance Factors")

    impact={
        "Study Hours":hours*2,
        "Attendance":attendance*0.5,
        "Previous Score":previous*1.5,
        "Practice Papers":papers*3,
        "Sleep Hours":sleep*2
    }

    st.bar_chart(impact)

    # ---------------- Suggestions ----------------

    st.markdown("## 🚀 Personalized Suggestions")

    if hours<6:
        st.write("📚 Increase study time to at least **6–8 hours/day**.")

    if attendance<75:
        st.write("🏫 Maintain attendance above **75%**.")

    if papers<5:
        st.write("📝 Practice more sample question papers.")

    if sleep<6:
        st.write("😴 Sleep **6–8 hours** daily for better concentration.")

    if score>=85:
        st.balloons()

else:
    st.markdown("""
<div style="background:#1e3a8a;
padding:20px;
border-radius:15px;
text-align:center;
font-size:20px;
font-weight:bold;
color:white;">
👈 Enter all details and click <span style="color:#22d3ee;">🚀 Predict Performance</span> to generate your AI Report.
</div>
""",unsafe_allow_html=True)

# ---------------- Footer ----------------

st.markdown("---")

st.markdown("""
<div style="text-align:center;color:#cbd5e1;font-size:16px;">
🚀 <b>AI Student Performance Advisor</b><br>
Built with ❤️ using Streamlit, Machine Learning & Plotly<br><br>
👨‍💻 Developed by <b>Abhay Kumar</b>
</div>
""",unsafe_allow_html=True)