import streamlit as st

st.title("🎯 Insight Hub – Project Intake Form")

with st.form("project_intake"):
    client_name = st.text_input("Client Name")

    primary_goal = st.selectbox(
        "Primary goal of this project?",
        ["Solve a problem", "Capture opportunities", "Achieve strategic goals", "Other"]
    )

    goal_details = st.text_area("Clearly describe your goal or problem:")

    business_value = st.text_input("What measurable value do you expect (e.g., save X hours, increase revenue by Y%)?")

    data_needs = st.text_area("What specific data or insights do you need?")

    out_of_scope = st.text_area("What's explicitly out of scope?")

    preferred_tools = st.text_input("Preferred tools or technologies (e.g., Power BI, Snowflake)?")

    privacy = st.selectbox("Are there privacy concerns or sensitive data involved?", ["Yes", "No"])

    security = st.selectbox("Any specific security considerations?", ["Yes", "No"])

    success_criteria = st.text_area("How do we measure project success?")

    submitted = st.form_submit_button("Submit & Generate Summary")

if submitted:
    st.subheader("Your inputs:")
    st.write("Client Name:", client_name)
    st.write("Primary Goal:", primary_goal)
    st.write("Goal Details:", goal_details)
    st.write("Business Value:", business_value)
    st.write("Data Needs:", data_needs)
    st.write("Out of Scope:", out_of_scope)
    st.write("Preferred Tools:", preferred_tools)
    st.write("Privacy Concerns:", privacy)
    st.write("Security Considerations:", security)
    st.write("Success Criteria:", success_criteria)
