import streamlit as st
from utils.helpers import format_expander_title
from utils.navigation import render_navigation_buttons

def show_page():
    st.subheader("🎯 WHY: Business Justification")

    with st.expander(format_expander_title("🎯 WHY: Business Justification", "🎯 WHY - Business Justification"), expanded=True):
        st.session_state.problem = st.text_area("Problem Statement *", st.session_state.get("problem", ""), height=100)
        st.session_state.outcome = st.text_area("Expected Outcomes *", st.session_state.get("outcome", ""), height=100)
        st.session_state.success = st.text_area("Success Criteria *", st.session_state.get("success", ""), height=100)

# **Call the centralized navigation buttons**
render_navigation_buttons()
