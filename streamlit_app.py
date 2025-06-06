import streamlit as st
import requests

# Compatibility dictionary
compatibility_map = {
    "INTJ": ["ENFP", "INFP", "INTJ"],
    "INTP": ["ENFJ", "INFJ", "INTP"],
    "ENTJ": ["INFP", "ISFP", "ENTJ"],
    "ENTP": ["INFJ", "ISFJ", "ENTP"],
    "INFJ": ["ENFP", "ENTP", "INFJ"],
    "INFP": ["ENFJ", "ENTJ", "INFP"],
    "ENFJ": ["INFP", "ISFP", "ENFJ"],
    "ENFP": ["INFJ", "INTJ", "ENFP"],
    "ISTJ": ["ESFP", "ISFJ", "ISTJ"],
    "ISFJ": ["ESTP", "ESFP", "ISFJ"],
    "ESTJ": ["ISFP", "INFP", "ESTJ"],
    "ESFJ": ["ISFP", "ISTP", "ESFJ"],
    "ISTP": ["ESFJ", "ENFJ", "ISTP"],
    "ISFP": ["ESTJ", "ESFJ", "ISFP"],
    "ESTP": ["ISFJ", "ISTJ", "ESTP"],
    "ESFP": ["ISTJ", "ISFJ", "ESFP"],
}

# MBTI descriptions
mbti_description_map = {
    "INTJ": "Strategic, analytical, independent",
    "INTP": "Logical, curious, inventive",
    "ENTJ": "Bold, confident, strategic leaders",
    "ENTP": "Quick-witted, enthusiastic, inventive",
    "INFJ": "Idealistic, compassionate, deep thinkers",
    "INFP": "Empathetic, imaginative, values-driven",
    "ENFJ": "Charismatic, altruistic, team-focused",
    "ENFP": "Energetic, imaginative, warm",
    "ISTJ": "Responsible, sincere, logical",
    "ISFJ": "Loyal, practical, nurturing",
    "ESTJ": "Efficient, organized, traditional",
    "ESFJ": "Sociable, caring, cooperative",
    "ISTP": "Independent, adaptable, practical",
    "ISFP": "Gentle, flexible, artistic",
    "ESTP": "Energetic, pragmatic, spontaneous",
    "ESFP": "Playful, enthusiastic, friendly",
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
            res1 = requests.get("https://vibe-986836536410.europe-west1.run.app/predict", params={"tweet": tweet1}).json()
            res2 = requests.get("https://vibe-986836536410.europe-west1.run.app/predict", params={"tweet": tweet2}).json()

            mbti_1 = res1["MBTI personality result"].upper()
            mbti_2 = res2["MBTI personality result"].upper()

            st.subheader("🧠 Predictions")
            col1, col2 = st.columns(2)
            with col1:
                st.success(f"**Tweet 1:** {mbti_1}")
                st.caption(mbti_description_map.get(mbti_1, ""))
            with col2:
                st.success(f"**Tweet 2:** {mbti_2}")
                st.caption(mbti_description_map.get(mbti_2, ""))

            # Compatibility check
            compatible_types = compatibility_map.get(mbti_1, [])
            st.subheader("🔗 Compatibility Score")
            if mbti_2 in compatible_types:
                st.progress(100)
                st.success("✅ These personalities are **highly compatible**!")
            else:
                st.progress(30)
                st.warning("⚠️ These personalities may **clash or need work to align**.")

        except Exception as e:
            st.error(f"Error during prediction: {e}")
    else:
        st.warning("Please enter both tweets first.")
