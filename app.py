import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title="Insight Hub", page_icon="🔍", layout="centered", initial_sidebar_state="expanded")

from utils.navigation import set_page, get_current_page
from sections import who, why, what, how, when, summary 

# Define available pages
PAGES = {
    "👥 WHO - Stakeholders & Team": who,
    "🎯 WHY - Business Justification": why,
    "📋 WHAT - Project Scope": what,
    "⚙️ HOW - Execution Plan": how,
    "📅 WHEN - Timeline & Milestones": when,
    "📑 Summary & Export": summary,
}

# Restore Sidebar Navigation
with st.sidebar:
    st.title("🚀 Insight Hub")
    selected_page = st.radio("Navigation", PAGES.keys(), index=list(PAGES.keys()).index(get_current_page()))
    if selected_page != get_current_page():
        set_page(selected_page)
        st.rerun()

# Determine the current page and show it
current_page = get_current_page()
if current_page in PAGES:
    PAGES[current_page].show_page()
