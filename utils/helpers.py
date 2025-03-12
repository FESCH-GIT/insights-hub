import streamlit as st

def is_filled(section):
    """Checks if all required fields for a section are filled."""
    required_fields = {
        "👥 WHO - Stakeholders & Team": ["owner", "team", "department"],
        "🎯 WHY - Business Justification": ["problem", "outcome", "success"],
        "📋 WHAT - Project Scope": ["type", "details"],
        "⚙️ HOW - Execution Plan": ["resources", "team_size", "budget"],
        "📅 WHEN - Timeline & Milestones": ["timeline", "milestones"]
    }
    for field in required_fields.get(section, []):
        value = st.session_state.get(field, "")
        if isinstance(value, list) and not value:  # Multi-select fields like department
            return False
        elif not str(value).strip():  # Strings and numbers
            return False
    return True

def section_status_icon(section):
    """Returns the correct status icon for each section."""
    return "✅" if is_filled(section) else "⚠️"

def format_expander_title(title, section):
    """Formats the expander title with a status icon aligned properly."""
    return f"{title} {section_status_icon(section)}"
