import streamlit as st
import requests

# Compatibility dictionary
compatibility_map = {
    "INTJ": ["ENFP", "INFP","INTJ"],
    "INTP": ["ENFJ", "INFJ","INTP"],
    "ENTJ": ["INFP", "ISFP","ENTJ"],
    "ENTP": ["INFJ", "ISFJ","ENTP"],
    "INFJ": ["ENFP", "ENTP","INFJ"],
    "INFP": ["ENFJ", "ENTJ","INFP"],
    "ENFJ": ["INFP", "ISFP","ENFJ"],
    "ENFP": ["INFJ", "INTJ","ENFP"],
    "ISTJ": ["ESFP", "ISFJ","ISTJ"],
    "ISFJ": ["ESTP", "ESFP","ISFJ"],
    "ESTJ": ["ISFP", "INFP","ESTJ"],
    "ESFJ": ["ISFP", "ISTP","ESFJ"],
    "ISTP": ["ESFJ", "ENFJ","ISTP"],
    "ISFP": ["ESTJ", "ESFJ","ISFP"],
    "ESTP": ["ISFJ", "ISTJ","ESTP"],
    "ESFP": ["ISTJ", "ISFJ","ESFP"],
}

# Page setup
st.set_page_config(page_title="MBTI Predictor", layout="centered")
st.title("🧠 Project Vibe: MBTI Tweet Classifier")
st.markdown("Paste **two tweets** and we'll predict the personalities and check their compatibility.")

# Inputs
col1, col2 = st.columns(2)
with col1:
    tweet1 = st.text_area("Tweet 1", key="tweet1")
with col2:
    tweet2 = st.text_area("Tweet 2", key="tweet2")

# Button
if st.button("Compare MBTI types"):
    if tweet1 and tweet2:
        try:
            # Call FastAPI endpoint for both tweets
            res1 = requests.get(
                "https://vibe-986836536410.europe-west1.run.app/predict", params={"tweet": tweet1}
            ).json()
            res2 = requests.get(
                "https://vibe-986836536410.europe-west1.run.app/predict", params={"tweet": tweet2}
            ).json()

            mbti_1 = res1["MBTI personality result"].upper()
            mbti_2 = res2["MBTI personality result"].upper()

            st.success(f"Tweet 1 MBTI: **{mbti_1}**")
            st.success(f"Tweet 2 MBTI: **{mbti_2}**")

            # Compatibility check
            compatible_types = compatibility_map.get(mbti_1, [])
            if mbti_2 in compatible_types:
                st.markdown("✅ These personalities are **compatible**!")
            else:
                st.markdown("⚠️ These personalities are **less likely to be compatible**.")
        except Exception as e:
            st.error(f"Error during prediction: {e}")
    else:
        st.warning("Please enter both tweets first.")
