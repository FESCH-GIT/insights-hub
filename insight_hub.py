import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import base64
from datetime import datetime
import json

# Set page configuration with custom theme
st.set_page_config(
    page_title="Insight Hub",
    page_icon="🔍",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
    }
    .main .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "page_index" not in st.session_state:
    st.session_state.page_index = 0
    st.session_state.creation_date = datetime.now().strftime("%Y-%m-%d")
    st.session_state.last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Define the page sequence with icons
pages = [
    "👥 WHO - Stakeholders & Team",
    "🎯 WHY - Business Justification",
    "📋 WHAT - Project Scope",
    "⚙️ HOW - Execution Plan",
    "📅 WHEN - Timeline & Milestones",
    "📑 Summary & Export"
]

# Sidebar
with st.sidebar:
    st.title("🚀 Insight Hub")
    st.markdown("---")
    selected_page = st.radio("Navigation", pages, index=st.session_state.page_index)
    st.markdown("---")
    st.markdown("### Project Info")
    st.markdown(f"Created: {st.session_state.creation_date}")
    st.markdown(f"Last Modified: {st.session_state.last_modified}")

# Sync sidebar selection with navigation
if selected_page != pages[st.session_state.page_index]:
    st.session_state.page_index = pages.index(selected_page)

def navigate(direction):
    new_index = st.session_state.page_index + direction
    if 0 <= new_index < len(pages):
        st.session_state.page_index = new_index
        st.session_state.last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_required_fields(fields):
    """Validate that required fields are not empty"""
    return all(st.session_state.get(field, "").strip() for field in fields)

# Main content area
st.title("🚀 Insight Hub - Define Your Project")

# Step 1: WHO
if pages[st.session_state.page_index] == "👥 WHO - Stakeholders & Team":
    st.subheader("👥 WHO: Stakeholders & Team")
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.owner = st.text_input(
            "Project Owner *",
            st.session_state.get("owner", ""),
            help="The primary person responsible for the project"
        )
    with col2:
        st.session_state.owner_role = st.selectbox(
            "Owner's Role *",
            ["Project Manager", "Technical Lead", "Business Analyst", "Department Head", "Other"],
            index=0 if "owner_role" not in st.session_state else ["Project Manager", "Technical Lead", "Business Analyst", "Department Head", "Other"].index(st.session_state.owner_role)
        )
    
    st.session_state.team = st.text_area(
        "Team Members & Stakeholders *",
        st.session_state.get("team", ""),
        help="List key team members and stakeholders, one per line",
        height=150
    )

    st.session_state.department = st.multiselect(
        "Involved Departments",
        ["IT", "Finance", "Marketing", "Operations", "HR", "Sales", "R&D", "Legal"],
        st.session_state.get("department", [])
    )

# Step 2: WHY
elif pages[st.session_state.page_index] == "🎯 WHY - Business Justification":
    st.subheader("🎯 WHY: Business Justification")
    
    st.session_state.problem = st.text_area(
        "Problem Statement *",
        st.session_state.get("problem", ""),
        help="Clearly define the problem or opportunity",
        height=100
    )
    
    st.session_state.outcome = st.text_area(
        "Expected Outcomes *",
        st.session_state.get("outcome", ""),
        help="What are the expected benefits and impact?",
        height=100
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.priority = st.select_slider(
            "Project Priority",
            options=["Low", "Medium", "High", "Critical"],
            value=st.session_state.get("priority", "Medium")
        )
    with col2:
        st.session_state.complexity = st.select_slider(
            "Project Complexity",
            options=["Simple", "Moderate", "Complex", "Very Complex"],
            value=st.session_state.get("complexity", "Moderate")
        )
    
    st.session_state.success = st.text_area(
        "Success Criteria *",
        st.session_state.get("success", ""),
        help="Define measurable success criteria",
        height=100
    )

# Step 3: WHAT
elif pages[st.session_state.page_index] == "📋 WHAT - Project Scope":
    st.subheader("📋 WHAT: Project Scope")
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.type = st.selectbox(
            "Project Type *",
            ["Business Intelligence", "Data Engineering", "AI & Machine Learning", "Infrastructure", "Security", "Other"],
            index=["Business Intelligence", "Data Engineering", "AI & Machine Learning", "Infrastructure", "Security", "Other"].index(st.session_state.get("type", "Business Intelligence"))
        )
    with col2:
        st.session_state.category = st.selectbox(
            "Project Category *",
            ["New Development", "Enhancement", "Maintenance", "Research", "Integration"],
            index=0 if "category" not in st.session_state else ["New Development", "Enhancement", "Maintenance", "Research", "Integration"].index(st.session_state.category)
        )
    
    st.session_state.details = st.text_area(
        "Project Details *",
        st.session_state.get("details", ""),
        help="Detailed description of what needs to be built or solved",
        height=150
    )
    
    st.session_state.deliverables = st.text_area(
        "Key Deliverables",
        st.session_state.get("deliverables", ""),
        help="List the main deliverables, one per line",
        height=100
    )

# Step 4: HOW
elif pages[st.session_state.page_index] == "⚙️ HOW - Execution Plan":
    st.subheader("⚙️ HOW: Execution Strategy")
    
    st.session_state.resources = st.text_area(
        "Required Resources *",
        st.session_state.get("resources", ""),
        help="List all required resources, tools, and expertise",
        height=100
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.team_size = st.number_input(
            "Team Size *",
            min_value=1,
            max_value=100,
            value=st.session_state.get("team_size", 5)
        )
    with col2:
        st.session_state.budget = st.text_input(
            "Estimated Budget *",
            st.session_state.get("budget", ""),
            help="Enter the estimated budget (e.g., $50,000)"
        )
    
    st.session_state.risks = st.text_area(
        "Potential Risks",
        st.session_state.get("risks", ""),
        help="List potential risks and mitigation strategies",
        height=100
    )

# Step 5: WHEN
elif pages[st.session_state.page_index] == "📅 WHEN - Timeline & Milestones":
    st.subheader("📅 WHEN: Timeline & Milestones")
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.start_date = st.date_input(
            "Project Start Date *",
            value=datetime.strptime(st.session_state.get("start_date", datetime.now().strftime("%Y-%m-%d")), "%Y-%m-%d")
        )
    with col2:
        st.session_state.end_date = st.date_input(
            "Expected End Date *",
            value=datetime.strptime(st.session_state.get("end_date", datetime.now().strftime("%Y-%m-%d")), "%Y-%m-%d")
        )
    
    st.session_state.timeline = st.text_input(
        "Project Duration *",
        st.session_state.get("timeline", ""),
        help="e.g., 6 months, 1 year"
    )
    
    st.session_state.milestones = st.text_area(
        "Key Milestones *",
        st.session_state.get("milestones", ""),
        help="List major milestones and their target dates",
        height=150
    )
    
    st.session_state.dependencies = st.text_area(
        "Dependencies",
        st.session_state.get("dependencies", ""),
        help="List any external dependencies or prerequisites",
        height=100
    )

# Step 6: Summary
else:
    st.subheader("📑 Project Summary")
    
    # Create expandable sections for each category
    with st.expander("👥 WHO: Stakeholders & Team", expanded=True):
        st.write(f"**Project Owner:** {st.session_state.get('owner', 'Not provided')} ({st.session_state.get('owner_role', 'Not specified')})")
        st.write(f"**Team Members & Stakeholders:**\n{st.session_state.get('team', 'Not provided')}")
        st.write(f"**Departments:** {', '.join(st.session_state.get('department', []))}")

    with st.expander("🎯 WHY: Business Justification", expanded=True):
        st.write(f"**Problem Statement:**\n{st.session_state.get('problem', 'Not provided')}")
        st.write(f"**Expected Outcomes:**\n{st.session_state.get('outcome', 'Not provided')}")
        st.write(f"**Priority:** {st.session_state.get('priority', 'Not specified')} | **Complexity:** {st.session_state.get('complexity', 'Not specified')}")
        st.write(f"**Success Criteria:**\n{st.session_state.get('success', 'Not provided')}")

    with st.expander("📋 WHAT: Project Scope", expanded=True):
        st.write(f"**Project Type:** {st.session_state.get('type', 'Not selected')} ({st.session_state.get('category', 'Not specified')})")
        st.write(f"**Project Details:**\n{st.session_state.get('details', 'Not provided')}")
        st.write(f"**Key Deliverables:**\n{st.session_state.get('deliverables', 'Not provided')}")

    with st.expander("⚙️ HOW: Execution Plan", expanded=True):
        st.write(f"**Required Resources:**\n{st.session_state.get('resources', 'Not provided')}")
        st.write(f"**Team Size:** {st.session_state.get('team_size', 'Not provided')} | **Budget:** {st.session_state.get('budget', 'Not provided')}")
        st.write(f"**Potential Risks:**\n{st.session_state.get('risks', 'Not provided')}")

    with st.expander("📅 WHEN: Timeline & Milestones", expanded=True):
        st.write(f"**Duration:** {st.session_state.get('timeline', 'Not provided')}")
        st.write(f"**Start Date:** {st.session_state.get('start_date', 'Not set')} | **End Date:** {st.session_state.get('end_date', 'Not set')}")
        st.write(f"**Key Milestones:**\n{st.session_state.get('milestones', 'Not provided')}")
        st.write(f"**Dependencies:**\n{st.session_state.get('dependencies', 'Not provided')}")

    # Export options
    st.markdown("---")
    st.subheader("Export Options")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📥 Export as JSON"):
            # Create JSON export
            export_data = {k: v for k, v in st.session_state.items() if k not in ['page_index']}
            json_str = json.dumps(export_data, indent=2, default=str)
            b64 = base64.b64encode(json_str.encode()).decode()
            href = f'<a href="data:application/json;base64,{b64}" download="project_charter.json">Download JSON</a>'
            st.markdown(href, unsafe_allow_html=True)
    
    with col2:
        if st.button("📄 Export as PDF"):
            # Create PDF export (simplified version)
            st.warning("PDF export functionality coming soon!")

# Navigation buttons
col1, col2 = st.columns([0.5, 0.5])
with col1:
    if st.session_state.page_index > 0:
        st.button("⬅️ Previous", on_click=navigate, args=(-1,))
with col2:
    if st.session_state.page_index < len(pages) - 1:
        st.button("Next ➡️", on_click=navigate, args=(1,))

# Progress bar
progress = (st.session_state.page_index + 1) / len(pages)
st.progress(progress)
