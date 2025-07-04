import streamlit as st
import pandas as pd
import plotly.graph_objects as go
 
# --- Initialize session state ---
if "responses" not in st.session_state:
    st.session_state.responses = {}
 
# --- Define dimensions and questions ---
data = {
    "Data-Driven Culture": [
        "There is a shared belief and valuesystem that encourages people to understand,use, and optimizate data.",
        "There is a culture that is open to change and innovation."
    ],
    "Organizational Alignment": [
        "Data analytics or AI initiatives are in line with their department's overall vision and objectives.",
        "These initiatives comply to the existing company-wide regulations, policies, and standards."
    ],
    "Data Capability": [
        "They have the appropriate tools for the transition towards a data-driven department (e.g. analytics tools).",
        "They have the appropriate processes in place for the transition towards a data-driven department (e.g. information transfer process).",
        "They have the appropriate people in place for the transition towards a data-driven department (e.g. data experts).",
        "They have the appropriate skills for the transition towards a data-driven department (e.g. data analytics skills)."
    ],
    "Management's Digital Literacy and Leadership": [
        "The departmentmanager has anunderstandingof data anddigital literacy.",
        "The department manager has the capability to lead the team in the complexities of shifting to a data-driven department."
    ],
    "Access to relevant high-quality data": [
        "There is relevant, contextualized, high-quality and harmonized data available.",
        "They also haveaccess to thisrelevant data."
    ],
    "Data Utilization": [
        "Data-driven insights are used in business decision-making.",
        "Data-driven insights are used in creating value such as improving services or developing new products."
    ]
}
 
likert_options = {
    "Strongly Disagree": 1,
    "Disagree": 2,
    "Neutral": 3,
    "Agree": 4,
    "Strongly Agree": 5
}
# --- Intro Text ---
st.markdown("""
# Welcome to the Data-Drivenness Assessment Tool

This interactive tool helps you evaluate how data-driven your department is across six key dimensions:
culture, alignment, capabilities, leadership, access, and utilization.

You’ll be guided through:
1. A short diagnostic questionnaire  
2. A radar chart visualizing your results  
3. A summary of which dimensions may need attention  
4. A tip on how to improve  

""")
# --- App Title ---
st.title("📊 Data-drivenness Assessment")
 
# --- Step 1: Respond to Questions ---
st.header("Step 1: Respond to Diagnostic Questions")
st.markdown("_Please rate the extent to which you agree with the following statements based on your experience with your client. Your responses will help identify strengths and improvement areas across six key dimensions._")
 
for dimension, questions in data.items():
    st.subheader(dimension)
    for i, question in enumerate(questions):
        key = f"{dimension}_{i}"
        selected_label = st.radio(
            question,
            options=list(likert_options.keys()),
            index=2,
            key=key,
            horizontal=True
        )
        st.session_state.responses[key] = likert_options[selected_label]
 
# --- Step 2: Calculate Scores ---
dimension_scores = {}
for dimension, questions in data.items():
    keys = [f"{dimension}_{i}" for i in range(len(questions))]
    values = [st.session_state.responses[k] for k in keys]
    avg_score = sum(values) / len(values)
    dimension_scores[dimension] = avg_score
 
# --- Step 3: Radar Chart ---
st.header("Step 2: Review Overall Diagnostic Results")
st.markdown("_The radar chart below visualizes your client's current state across the six dimensions. Each axis represents one dimension, and the closer to the edge, the stronger the dimension._")

 
categories = list(dimension_scores.keys())
values = list(dimension_scores.values())
 
fig = go.Figure(
    data=[go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself'
    )]
)
fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[1, 5])),
    showlegend=False
)
st.plotly_chart(fig)
 
# --- Step 4: Priorities ---
st.header("Step 3: Identify High Priority Areas")
st.markdown("_Dimensions scoring below the threshold (3.0) are highlighted here. These are potential focus areas for improvement to enhance your client's data-drivenness._")

 
priority_threshold = 3.0
priorities = [d for d, score in dimension_scores.items() if score < priority_threshold]
 
if priorities:
    st.warning("⚠️ The following dimensions scored below the threshold of 3.0 and need attention:")
    for p in priorities:
        st.write(f"- **{p}** (Score: {dimension_scores[p]:.2f})")
else:
    st.success("✅ All dimensions are above the threshold.")
 
# --- Step 5: Improvement link ---
st.header("Step 4: Click on the link below")

st.markdown("""
<hr>
<a href="https://brightcape.sharepoint.com/sites/TowardsDataDrivenDepartment?xsdata=MDV8MDJ8fGYyNDA0ZTU4YzU3NTQxZTk3Zjk2MDhkZGFjZDNkOWIyfGQ2MjhmMjgxNjQwYTQ4Y2U5MGVhYzk0ZTkwMTBmMTM4fDB8MHw2Mzg4NTY3NDgwNDY5MDkzMzR8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxMMk5vWVhSekx6RTVPalpoWTJZeU16STFMV1E1TnpNdE5HRXpZUzA1WlRabUxUZGxNVGs1WVRrMU9HWm1NbDltT0dVME1tVmtaQzA0WldGaUxUUm1ZekF0T0dFMU5TMHpaREV4WXpGbU9HWXlabUZBZFc1eExtZGliQzV6Y0dGalpYTXZiV1Z6YzJGblpYTXZNVGMxTURBM09EQXdOREEwTnc9PXwxOWM5MmFkMTllZGY0ZDdlN2Y5NjA4ZGRhY2QzZDliMnxlYTczN2IwZWY2NzI0NmNiYjBjNzJkOWZjNGQzYzNiZA%3D%3D&sdata=WVZiN2xjeWhLYmcxNUwreHNHTVVQSDB4NWxNZFVDd1I0SFV4UllzMXA2UT0%3D&ovuser=8d37411e-55a6-402d-b6b4-95be13019b71%2Cs.vandenbrink-shahsavari%40brightcape.nl&OR=Teams-HL&CT=1751020894170&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI0OS8yNTA2MDIwNjYxNiIsIkhhc0ZlZGVyYXRlZFVzZXIiOnRydWV9"_blank">
<p style="font-size:50px; text-align:center; color:#3366cc;">
        How to improve or enable the dimensions?
</p>
</a>
""", unsafe_allow_html=True)
