import streamlit as st
import json
import base64
from utils.helpers import is_filled, section_status_icon
from utils.navigation import render_navigation_buttons

def show_page():
    st.subheader("📑 Project Summary")

    def format_expander_title(title, section):
        """Formats the expander title with the status icon right next to it."""
        return f"{title} {section_status_icon(section)}"

    sections = [
        ("👥 WHO: Stakeholders & Team", "👥 WHO - Stakeholders & Team"),
        ("🎯 WHY: Business Justification", "🎯 WHY - Business Justification"),
        ("📋 WHAT: Project Scope", "📋 WHAT - Project Scope"),
        ("⚙️ HOW: Execution Plan", "⚙️ HOW - Execution Plan"),
        ("📅 WHEN: Timeline & Milestones", "📅 WHEN - Timeline & Milestones"),
    ]

    for title, section in sections:
        with st.expander(format_expander_title(title, section), expanded=True):
            if section == "👥 WHO - Stakeholders & Team":
                st.write(f"**Project Owner:** {st.session_state.get('owner', 'Not provided')}")
                st.write(f"**Team Members & Stakeholders:** {st.session_state.get('team', 'Not provided')}")
                st.write(f"**Departments Involved:** {', '.join(st.session_state.get('department', [])) if st.session_state.get('department') else 'Not specified'}")
            elif section == "🎯 WHY - Business Justification":
                st.write(f"**Problem Statement:** {st.session_state.get('problem', 'Not provided')}")
                st.write(f"**Expected Outcomes:** {st.session_state.get('outcome', 'Not provided')}")
                st.write(f"**Success Criteria:** {st.session_state.get('success', 'Not provided')}")
            elif section == "📋 WHAT - Project Scope":
                st.write(f"**Project Type:** {st.session_state.get('type', 'Not selected')}")
                st.write(f"**Project Details:** {st.session_state.get('details', 'Not provided')}")
            elif section == "⚙️ HOW - Execution Plan":
                st.write(f"**Required Resources:** {st.session_state.get('resources', 'Not provided')}")
                st.write(f"**Team Size:** {st.session_state.get('team_size', 'Not specified')}")
                st.write(f"**Budget Estimate:** {st.session_state.get('budget', 'Not specified')}")
            elif section == "📅 WHEN - Timeline & Milestones":
                st.write(f"**Project Duration:** {st.session_state.get('timeline', 'Not provided')}")
                st.write(f"**Key Milestones:** {st.session_state.get('milestones', 'Not provided')}")

    # **Export Options**
    st.markdown("---")
    st.subheader("Export Options")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📥 Export as JSON"):
            export_data = {k: v for k, v in st.session_state.items() if k not in ['page_index']}
            json_str = json.dumps(export_data, indent=2, default=str)
            b64 = base64.b64encode(json_str.encode()).decode()
            href = f'<a href="data:application/json;base64,{b64}" download="project_summary.json">Download JSON</a>'
            st.markdown(href, unsafe_allow_html=True)
    
    with col2:
        if st.button("📄 Export as PDF"):
            st.warning("PDF export functionality coming soon!")

    # **Legend at the bottom**
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; font-size: 14px;'>"
        "✅ All required fields are filled &nbsp;&nbsp;|&nbsp;&nbsp; "
        "⚠️ Some required fields are missing"
        "</div>", 
        unsafe_allow_html=True
    )
            
# **Call the centralized navigation buttons**
render_navigation_buttons()
