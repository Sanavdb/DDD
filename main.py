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
        "We have the tools to manage and process data effectively.",
        "Our data infrastructure scales with our needs."
    ],
    "Management's Digital Literacy and Leadership": [
        "The departmentmanager has anunderstandingof data anddigital literacy.",
        "The department manager has the capability to lead the team in the complexities of shifting to a data-driven department."
    ],
    "Data Access": [
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
 
# --- App Title ---
st.title("📊 Data-drivenness Assessment")
 
# --- Step 1: Respond to Questions ---
st.header("Step 1: Respond to Diagnostic Questions")
 
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
 
priority_threshold = 3.0
priorities = [d for d, score in dimension_scores.items() if score < priority_threshold]
 
if priorities:
    st.warning("⚠️ The following dimensions scored below the threshold of 3.0 and need attention:")
    for p in priorities:
        st.write(f"- **{p}** (Score: {dimension_scores[p]:.2f})")
else:
    st.success("✅ All dimensions are above the threshold.")
 
# --- Step 5: Improvement link ---
st.markdown("""
<hr>
<a href="https://www.bol.com/nl/nl/?Referrer=ADVNLPPcef59e000569dccd000027c6ce681027056&utm_source=1027056&utm_medium=Affiliates&utm_campaign=CPS&utm_content=txl" target="_blank">
<p style="font-size:50px; text-align:center; color:#3366cc;">
        How to improve or enable the dimensions?
</p>
</a>
""", unsafe_allow_html=True)
