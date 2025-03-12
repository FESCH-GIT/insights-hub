import streamlit as st
from utils.navigation import set_page, get_current_page
from sections import who, why, what, how, when, summary 

# Set Streamlit page configuration
st.set_page_config(page_title="Insight Hub", page_icon="🔍", layout="centered", initial_sidebar_state="expanded")

# Define available pages
PAGES = {
    "👥 WHO - Stakeholders & Team": who,
    "🎯 WHY - Business Justification": why,
    "📋 WHAT - Project Scope": what,
    "⚙️ HOW - Execution Plan": how,
    "📅 WHEN - Timeline & Milestones": when,
    "📑 Summary & Export": summary,
}

# Sidebar Navigation
selected_page = st.sidebar.radio("Navigation", list(PAGES.keys()))
set_page(selected_page)

# Display the selected page
PAGES[get_current_page()].show_page()
