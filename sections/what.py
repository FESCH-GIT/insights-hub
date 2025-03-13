import streamlit as st
from utils.helpers import format_expander_title
from utils.navigation import render_navigation_buttons

def show_page():
    st.subheader("📋 WHAT: Project Scope")

    with st.expander(format_expander_title("📋 WHAT: Project Scope", "📋 WHAT - Project Scope"), expanded=True):
        st.session_state.type = st.selectbox(
            "Project Type *", 
            ["Business Intelligence", "Data Engineering", "AI & Machine Learning", "Other"], 
            index=0
        )
        st.session_state.details = st.text_area("Project Details *", st.session_state.get("details", ""), height=150)
            
# **Call the centralized navigation buttons**
render_navigation_buttons()
