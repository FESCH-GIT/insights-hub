import streamlit as st
from utils.helpers import format_expander_title
from utils.navigation import render_navigation_buttons

def show_page():
    st.subheader("👥 WHO: Stakeholders & Team")

    with st.expander(format_expander_title("👥 WHO: Stakeholders & Team", "👥 WHO - Stakeholders & Team"), expanded=True):
        st.session_state.owner = st.text_input("Project Owner *", st.session_state.get("owner", ""))
        st.session_state.owner_role = st.selectbox("Owner's Role *", ["Project Manager", "Technical Lead", "Business Analyst", "Department Head", "Other"], index=0)
        st.session_state.team = st.text_area("Team Members & Stakeholders *", st.session_state.get("team", ""), height=100)

        selected_departments = st.multiselect(
            "Involved Departments *",
            ["IT", "Finance", "Marketing", "Operations", "HR", "Sales", "R&D", "Legal"],
            default=st.session_state.get("department", [])
        )
        if selected_departments != st.session_state.get("department", []):
            st.session_state["department"] = selected_departments
            st.rerun()

# **Call the centralized navigation buttons**
render_navigation_buttons()
