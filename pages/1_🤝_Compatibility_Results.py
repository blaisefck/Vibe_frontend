import streamlit as st

# Compatibility and descriptions
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

st.set_page_config(page_title="Compatibility Results", layout="centered")

# Background and box styling
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

# Title
st.markdown('<div class="opaque-box"><h1>🤝 MBTI Compatibility Results</h1></div>', unsafe_allow_html=True)

# Get session state
mbti_1 = st.session_state.get("mbti_1")
mbti_2 = st.session_state.get("mbti_2")

if not mbti_1 or not mbti_2:
    st.warning("Please start from the main page to enter tweets.")
    st.page_link("streamlit_app.py", label="← Go to Main Page")
else:
    st.markdown('<div class="opaque-box">', unsafe_allow_html=True)
    st.subheader("Your Results")
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"**Person 1:** {mbti_1}")
        st.caption(mbti_description_map.get(mbti_1, ""))
    with col2:
        st.success(f"**Person 2:** {mbti_2}")
        st.caption(mbti_description_map.get(mbti_2, ""))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="opaque-box">', unsafe_allow_html=True)
    compatible = mbti_2 in compatibility_map.get(mbti_1, [])
    st.subheader("🔗 Compatibility Score")
    if compatible:
        st.progress(100)
        st.success("✅ These personalities are **highly compatible**!")
        st.markdown("They're likely to share complementary traits that support mutual growth and deep understanding.")
    else:
        st.progress(30)
        st.warning("⚠️ These personalities might **clash or require effort**.")
        st.markdown("While differences can enrich relationships, communication and understanding will be key for alignment.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.page_link("streamlit_app.py", label="← Try with different tweets", icon="🔁")
