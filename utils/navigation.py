import streamlit as st
import re
from datetime import datetime

# Keep the original navigation state logic
def set_page(page_name):
    """Stores the selected page in session state and triggers a rerun."""
    st.session_state["current_page"] = page_name
    st.session_state["nav_counter"] += 1  # Update counter to make keys unique
    st.rerun()  # Forces Streamlit to refresh the UI with the new page

def get_current_page():
    """Retrieves the currently selected page from session state."""
    return st.session_state.get("current_page", "👥 WHO - Stakeholders & Team")

# Ensure session state variables exist
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "👥 WHO - Stakeholders & Team"

if "nav_counter" not in st.session_state:
    st.session_state["nav_counter"] = 0  # Counter to ensure button uniqueness

# Define the list of pages
PAGES = [
    "👥 WHO - Stakeholders & Team",
    "🎯 WHY - Business Justification",
    "📋 WHAT - Project Scope",
    "⚙️ HOW - Execution Plan",
    "📅 WHEN - Timeline & Milestones",
    "📑 Summary & Export"
]

def sanitize_key(text):
    """Removes emojis, spaces, and special characters to create a valid Streamlit key."""
    return re.sub(r"[^\w]", "_", text)

def render_navigation_buttons():
    """Ensures navigation buttons appear on every page with unique keys."""
    current_page = get_current_page()
    current_index = PAGES.index(current_page)
    sanitized_key = sanitize_key(current_page)

    # Update the navigation counter for unique keys
    st.session_state["nav_counter"] += 1
    unique_id = st.session_state["nav_counter"]

    col1, col2 = st.columns([0.5, 0.5])
    with col1:
        if current_index > 0:
            if st.button("⬅️ Previous", key=f"prev_{sanitized_key}_{unique_id}"):
                set_page(PAGES[current_index - 1])
    with col2:
        if current_index < len(PAGES) - 1:
            if st.button("Next ➡️", key=f"next_{sanitized_key}_{unique_id}"):
                set_page(PAGES[current_index + 1])
