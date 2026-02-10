import streamlit as st
import pandas as pd

# -----------------------------
# Helper logic (simple versions)
# -----------------------------
def planner_logic(subjects, difficulties, days_left, daily_hours):
    total_weight = sum(difficulties)
    plan = []

    for subject, diff, days in zip(subjects, difficulties, days_left):
        weight = diff / total_weight
        hours_per_day = round(weight * daily_hours, 2)
        plan.append({
            "Subject": subject,
            "Difficulty": diff,
            "Days Left": days,
            "Hours / Day": hours_per_day
        })

    return plan


def ai_tips(difficulty):
    if difficulty >= 4:
        return "Focus on revision and lots of practice."
    elif difficulty == 3:
        return "Use a mix of revision and practice."
    else:
        return "Light revision is enough."


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📚 AI Study Planner")

st.write("Enter your subjects and study details below.")

num_subjects = st.number_input(
    "Number of subjects",
    min_value=1,
    max_value=10,
    value=3
)

subjects = []
difficulties = []
days_left = []

st.subheader("Subjects")

for i in range(num_subjects):
    col1, col2, col3 = st.columns(3)

    with col1:
        subject = st.text_input(f"Subject {i+1}", key=f"sub_{i}")
    with col2:
        difficulty = st.slider(
            "Difficulty (1–5)",
            1, 5, 3,
            key=f"diff_{i}"
        )
    with col3:
        days = st.number_input(
            "Exam days left",
            min_value=1,
            value=7,
            key=f"days_{i}"
        )

    subjects.append(subject)
    difficulties.append(difficulty)
    days_left.append(days)

daily_hours = st.number_input(
    "Daily available study hours",
    min_value=1.0,
    max_value=24.0,
    value=4.0
)

# -----------------------------
# Generate plan
# -----------------------------
if st.button("Generate Study Plan"):
    plan = planner_logic(subjects, difficulties, days_left, daily_hours)

    df = pd.DataFrame(plan)

    st.subheader("📅 Study Timetable")
    st.table(df)

    st.subheader("🤖 AI Study Tips")
    for subject, diff in zip(subjects, difficulties):
        st.write(f"**{subject}:** {ai_tips(diff)}")

