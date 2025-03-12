import streamlit as st
from datetime import datetime

def set_page(page_name):
    """Stores the selected page in session state."""
    st.session_state["current_page"] = page_name

def get_current_page():
    """Retrieves the currently selected page."""
    return st.session_state.get("current_page", "👥 WHO - Stakeholders & Team")

# Initialize session state
if "creation_date" not in st.session_state:
    st.session_state.creation_date = datetime.now().strftime("%Y-%m-%d")
    st.session_state.last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.visited_pages = {page: False for page in [
        "👥 WHO - Stakeholders & Team",
        "🎯 WHY - Business Justification",
        "📋 WHAT - Project Scope",
        "⚙️ HOW - Execution Plan",
        "📅 WHEN - Timeline & Milestones",
        "📑 Summary & Export"
    ]}
    st.session_state.completed_pages = {page: False for page in st.session_state.visited_pages}
    st.session_state.department = []
