import streamlit as st
import requests
import urllib.parse

# Page config
st.set_page_config(page_title="MBTI Predictor", layout="centered")
st.title("🧠 Project Vibe: MBTI Tweet Classifier")
st.markdown("Paste **two tweets** and we'll predict the personalities.")

# Inputs
col1, col2 = st.columns(2)
with col1:
    tweet1 = st.text_area("Tweet from one person", key="tweet1")
with col2:
    tweet2 = st.text_area("Tweet from another person", key="tweet2")

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

            st.subheader("🧠 Predictions")
            col1, col2 = st.columns(2)
            with col1:
                st.success(f"**Tweet 1:** {mbti_1}")
            with col2:
                st.success(f"**Tweet 2:** {mbti_2}")

            st.markdown("---")
            st.page_link("pages/1_🤝_Compatibility_Results.py", label="See Compatibility →")

        except Exception as e:
            st.error(f"Error during prediction: {e}")
    else:
        st.warning("Please enter both tweets.")
