import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import base64

st.title("🚀 Insight Hub")

# Step 1: Why (Business Justification)
st.subheader("🔍 WHY: Business Justification")
business_problem = st.text_area("What is the problem or opportunity?")
expected_outcome = st.text_area("What is the expected value or impact?")
success_criteria = st.text_area("How will we measure success?")

# Step 2: What (Scope of the Project)
st.subheader("📌 WHAT: Project Scope")
project_type = st.selectbox(
    "Select the project type:",
    ["Business Intelligence", "Data Engineering", "AI & Machine Learning", "Other"]
)
project_details = st.text_area("Describe what needs to be built or solved.")

# Step 3: How (Execution Plan)
st.subheader("🛠 HOW: Execution Strategy")
required_resources = st.text_area("What resources (tools, data, expertise) are needed?")
team_size = st.number_input("Estimated team size", min_value=1, max_value=100, value=5)
budget = st.text_input("Estimated budget for the project")

# Step 4: When (Timeline & Milestones)
st.subheader("📅 WHEN: Timeline & Milestones")
timeline = st.text_input("Expected timeline for completion")
key_milestones = st.text_area("What are the key milestones or phases?")

# Generate PDF Report
def create_pdf(why, what, how, when):
    pdf_filename = "project_summary.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    
    c.drawString(100, 750, "Project Summary")
    
    c.drawString(100, 730, "🔍 WHY: Business Justification")
    c.drawString(100, 710, f"Problem/Opportunity: {why['problem'][:100]}")
    c.drawString(100, 690, f"Expected Outcome: {why['outcome'][:100]}")
    c.drawString(100, 670, f"Success Criteria: {why['success'][:100]}")
    
    c.drawString(100, 650, "📌 WHAT: Project Scope")
    c.drawString(100, 630, f"Project Type: {what['type']}")
    c.drawString(100, 610, f"Details: {what['details'][:100]}")
    
    c.drawString(100, 590, "🛠 HOW: Execution Plan")
    c.drawString(100, 570, f"Resources: {how['resources'][:100]}")
    c.drawString(100, 550, f"Team Size: {how['team_size']}")
    c.drawString(100, 530, f"Budget: {how['budget']}")
    
    c.drawString(100, 510, "📅 WHEN: Timeline & Milestones")
    c.drawString(100, 490, f"Timeline: {when['timeline']}")
    c.drawString(100, 470, f"Milestones: {when['milestones'][:100]}")
    
    c.save()
    return pdf_filename

def get_pdf_download_link(pdf_filename):
    with open(pdf_filename, "rb") as f:
        pdf_base64 = base64.b64encode(f.read()).decode()
    return f'<a href="data:application/pdf;base64,{pdf_base64}" download="project_summary.pdf">📥 Download PDF</a>'

# Generate PDF Button
if st.button("Generate Project Summary"):
    pdf_filename = create_pdf(
        why={"problem": business_problem, "outcome": expected_outcome, "success": success_criteria},
        what={"type": project_type, "details": project_details},
        how={"resources": required_resources, "team_size": team_size, "budget": budget},
        when={"timeline": timeline, "milestones": key_milestones}
    )
    st.markdown(get_pdf_download_link(pdf_filename), unsafe_allow_html=True)
