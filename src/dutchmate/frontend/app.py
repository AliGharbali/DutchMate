import streamlit as st

st.set_page_config(page_title="DutchMate", layout="centered")

st.title("🇳🇱 DutchMate – B1 Dutch Tutor")

st.sidebar.header("Navigation")
lesson = st.sidebar.selectbox("Choose a lesson", [f"Lesson {i+1}" for i in range(10)])

st.write(f"## {lesson}")

st.info("This is a prototype interface. Lesson content and activities will appear here.")

st.markdown("""
**Features coming soon:**
- Interactive reading, listening, speaking, and writing activities
- Automated scoring and feedback
- Progress tracking and adaptive rehearsal
""")
