import streamlit as st
import requests

st.set_page_config(page_title="MBTI Predictor", layout="centered")

# Inject background image and opaque box style
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
                          url("https://daoinsights.com/wp-content/webp-express/webp-images/uploads/2022/04/mbti-types.png.webp");
        background-size: contain;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
    .opaque-box {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title & Description
st.markdown('<div class="opaque-box"><h1>🧠 Project Vibe: MBTI Tweet Classifier</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="opaque-box">Paste <b>two tweets</b> from different people and we\'ll predict their personalities.</div>', unsafe_allow_html=True)

# Initialize session state
if "tweet1" not in st.session_state:
    st.session_state["tweet1"] = ""
if "tweet2" not in st.session_state:
    st.session_state["tweet2"] = ""

# Inputs
col1, col2 = st.columns(2)
with col1:
    tweet1 = st.text_area("Tweet from one person", value=st.session_state["tweet1"], key="input1")
with col2:
    tweet2 = st.text_area("Tweet from another person", value=st.session_state["tweet2"], key="input2")

if st.button("Get MBTI Results"):
    if tweet1 and tweet2:
        try:
            res1 = requests.get("https://vibe-986836536410.europe-west1.run.app/predict", params={"tweet": tweet1}).json()
            res2 = requests.get("https://vibe-986836536410.europe-west1.run.app/predict", params={"tweet": tweet2}).json()

            mbti_1 = res1["MBTI personality result"].upper()
            mbti_2 = res2["MBTI personality result"].upper()

            st.session_state["tweet1"] = tweet1
            st.session_state["tweet2"] = tweet2
            st.session_state["mbti_1"] = mbti_1
            st.session_state["mbti_2"] = mbti_2

            st.markdown('<div class="opaque-box"><h3>🧠 Predictions</h3>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.success(f"**Tweet from Person 1:** {mbti_1}")
            with col2:
                st.success(f"**Tweet from Person 2:** {mbti_2}")
            st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("---")
            st.page_link("pages/1_🤝_Compatibility_Results.py", label="See Compatibility →")

        except Exception as e:
            st.error(f"Error during prediction: {e}")
    else:
        st.warning("Please enter both tweets.")
