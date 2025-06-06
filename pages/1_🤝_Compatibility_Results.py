import streamlit as st

# Compatibility and descriptions
compatibility_map = {
    "INTJ": ["ENFP", "INFP", "INTJ"],
    "INTP": ["ENFJ", "INFJ", "INTP"],
    # ... (keep full dictionary here)
}

mbti_description_map = {
    "INTJ": "Strategic, analytical, independent",
    # ... (full descriptions)
}

# Page config
st.set_page_config(page_title="Compatibility Results", layout="centered")
st.title("🤝 MBTI Compatibility Results")

# Retrieve session data
mbti_1 = st.session_state.get("mbti_1")
mbti_2 = st.session_state.get("mbti_2")

if not mbti_1 or not mbti_2:
    st.warning("Please start from the main page to enter tweets.")
    st.page_link("streamlit_app.py", label="← Go to Main Page")
else:
    st.subheader("Your Results")
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"**Tweet 1:** {mbti_1}")
        st.caption(mbti_description_map.get(mbti_1, ""))
    with col2:
        st.success(f"**Tweet 2:** {mbti_2}")
        st.caption(mbti_description_map.get(mbti_2, ""))

    # Compatibility check
    compatible = mbti_2 in compatibility_map.get(mbti_1, [])
    st.subheader("🔗 Compatibility Score")
    if compatible:
        st.progress(100)
        st.success("✅ These personalities are **highly compatible**!")
        st.markdown(
            "They're likely to share complementary traits that support mutual growth and deep understanding."
        )
    else:
        st.progress(30)
        st.warning("⚠️ These personalities might **clash or require effort**.")
        st.markdown(
            "While differences can enrich relationships, communication and understanding will be key for alignment."
        )

    st.page_link("streamlit_app.py", label="← Try with different tweets", icon="🔁")
