import streamlit as st
import requests

st.set_page_config(page_title="MBTI Predictor", layout="centered")
st.markdown("""# Project Vibe
## 🧠 MBTI Tweet Classifier
    """)

tweet = st.text_area("Paste a tweet here:")

if st.button("Predict MBTI type"):
    if tweet:
        response = requests.get("https://vibe-986836536410.europe-west1.run.app/predict", params={"tweet": tweet})
        result = response.json()
        st.success(f"Prediction: {result['MBTI personality result']}")
    else:
        st.warning("Please enter a tweet first.")
