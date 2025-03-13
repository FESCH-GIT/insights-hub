import streamlit as st
from utils.helpers import format_expander_title
from utils.navigation import render_navigation_buttons

def show_page():
    st.subheader("⚙️ HOW: Execution Plan")

    with st.expander(format_expander_title("⚙️ HOW: Execution Plan", "⚙️ HOW - Execution Plan"), expanded=True):
        st.session_state.resources = st.text_area("Required Resources *", st.session_state.get("resources", ""), height=100)
        st.session_state.team_size = st.number_input("Team Size *", min_value=1, max_value=100, value=st.session_state.get("team_size", 5))
        st.session_state.budget = st.text_input("Estimated Budget *", st.session_state.get("budget", ""))
            
# **Call the centralized navigation buttons**
render_navigation_buttons()
