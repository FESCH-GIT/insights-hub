import streamlit as st
from utils.helpers import format_expander_title
from utils.navigation import render_navigation_buttons

def show_page():
    st.subheader("📅 WHEN: Timeline & Milestones")

    with st.expander(format_expander_title("📅 WHEN: Timeline & Milestones", "📅 WHEN - Timeline & Milestones"), expanded=True):
        st.session_state.timeline = st.text_input("Project Duration *", st.session_state.get("timeline", ""))
        st.session_state.milestones = st.text_area("Key Milestones *", st.session_state.get("milestones", ""), height=150)
            
# **Call the centralized navigation buttons**
render_navigation_buttons()
