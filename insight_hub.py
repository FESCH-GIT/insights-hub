import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import base64
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Insight Hub",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "page_index" not in st.session_state:
    st.session_state.page_index = 0
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

# Define pages
pages = list(st.session_state.visited_pages.keys())

# Ensure department selection persists
if "department" not in st.session_state:
    st.session_state.department = []

# **Check if a page is fully completed**
def is_filled(section):
    required_fields = {
        "👥 WHO - Stakeholders & Team": ["owner", "team", "department"],
        "🎯 WHY - Business Justification": ["problem", "outcome", "success"],
        "📋 WHAT - Project Scope": ["type", "details"],
        "⚙️ HOW - Execution Plan": ["resources", "team_size", "budget"],
        "📅 WHEN - Timeline & Milestones": ["timeline", "milestones"]
    }
    for field in required_fields.get(section, []):
        value = st.session_state.get(field, "")
        if isinstance(value, list):  # Multi-select fields like department
            if not value:  # Empty list is not filled
                return False
        elif not str(value).strip():  # Strings and numbers
            return False
    return True  # All required fields are filled

# **Update completed pages**
for page in pages:
    st.session_state.completed_pages[page] = is_filled(page)
    st.session_state.visited_pages[page] = True  # Ensure all visited pages are marked

# **Sidebar Navigation with ✅ Checkmark for Completed Pages**
CHECK_MARK = "✅"  # Green checkmark for completed pages

sidebar_labels = [
    f"{page}{' ' * (40 - len(page))}{CHECK_MARK if st.session_state.completed_pages[page] else ''}"
    for page in pages
]

# **Fix: Sidebar with Correct Selection Matching**
selected_page = st.sidebar.radio(
    "Navigation", 
    pages,  
    format_func=lambda p: f"{p}{' ' * (40 - len(p))}{CHECK_MARK if st.session_state.completed_pages[p] else ''}",
    index=st.session_state.page_index,
    key="sidebar_nav"
)

# **Update visited page when switching**
if selected_page != pages[st.session_state.page_index]:
    st.session_state.page_index = pages.index(selected_page)
    st.session_state.visited_pages[selected_page] = True
    st.rerun()

# **Function to navigate between pages**
def navigate(direction):
    """ Navigate forward (+1) or backward (-1) """
    new_index = st.session_state.page_index + direction
    if 0 <= new_index < len(pages):
        st.session_state.page_index = new_index
        st.session_state.visited_pages[pages[new_index]] = True  # Mark new page as visited
        st.rerun()

# **Main Content Area**
st.title("🚀 Insight Hub - Define Your Project")

# **STEP 1: WHO**
if pages[st.session_state.page_index] == "👥 WHO - Stakeholders & Team":
    st.subheader("👥 WHO: Stakeholders & Team")
    st.session_state.owner = st.text_input("Project Owner *", st.session_state.get("owner", ""))
    st.session_state.owner_role = st.selectbox("Owner's Role *", ["Project Manager", "Technical Lead", "Business Analyst", "Department Head", "Other"], index=0)
    st.session_state.team = st.text_area("Team Members & Stakeholders *", st.session_state.get("team", ""), height=100)

    # **Fix: Ensure Multiselect Updates Instantly**
    selected_departments = st.multiselect(
        "Involved Departments *",
        ["IT", "Finance", "Marketing", "Operations", "HR", "Sales", "R&D", "Legal"],
        default=st.session_state.department
    )
    if selected_departments != st.session_state.department:
        st.session_state.department = selected_departments
        st.rerun()

# **STEP 2: WHY**
elif pages[st.session_state.page_index] == "🎯 WHY - Business Justification":
    st.subheader("🎯 WHY: Business Justification")
    st.session_state.problem = st.text_area("Problem Statement *", st.session_state.get("problem", ""), height=100)
    st.session_state.outcome = st.text_area("Expected Outcomes *", st.session_state.get("outcome", ""), height=100)
    st.session_state.success = st.text_area("Success Criteria *", st.session_state.get("success", ""), height=100)

# **STEP 3: WHAT**
elif pages[st.session_state.page_index] == "📋 WHAT - Project Scope":
    st.subheader("📋 WHAT: Project Scope")
    st.session_state.type = st.selectbox("Project Type *", ["Business Intelligence", "Data Engineering", "AI & Machine Learning", "Other"], index=0)
    st.session_state.details = st.text_area("Project Details *", st.session_state.get("details", ""), height=150)

# **STEP 4: HOW**
elif pages[st.session_state.page_index] == "⚙️ HOW - Execution Plan":
    st.subheader("⚙️ HOW: Execution Strategy")
    st.session_state.resources = st.text_area("Required Resources *", st.session_state.get("resources", ""), height=100)
    st.session_state.team_size = st.number_input("Team Size *", min_value=1, max_value=100, value=st.session_state.get("team_size", 5))
    st.session_state.budget = st.text_input("Estimated Budget *", st.session_state.get("budget", ""))

# **STEP 5: WHEN**
elif pages[st.session_state.page_index] == "📅 WHEN - Timeline & Milestones":
    st.subheader("📅 WHEN: Timeline & Milestones")
    st.session_state.timeline = st.text_input("Project Duration *", st.session_state.get("timeline", ""))
    st.session_state.milestones = st.text_area("Key Milestones *", st.session_state.get("milestones", ""), height=150)

# **STEP 6: SUMMARY & EXPORT**
elif pages[st.session_state.page_index] == "📑 Summary & Export":
    st.subheader("📑 Project Summary")
    st.write(f"**Project Owner:** {st.session_state.get('owner', 'Not provided')}")
    st.write(f"**Departments:** {', '.join(st.session_state.get('department', []))}")

# **Navigation Buttons**
col1, col2 = st.columns([0.5, 0.5])
with col1:
    if st.session_state.page_index > 0:
        if st.button("⬅️ Previous"):
            navigate(-1)
with col2:
    if st.session_state.page_index < len(pages) - 1:
        if st.button("Next ➡️"):
            navigate(1)

# **Progress Bar**
progress = (st.session_state.page_index + 1) / len(pages)
st.progress(progress)
