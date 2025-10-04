# cgpa_calculator.py
import streamlit as st

st.title("🎓 CGPA Calculator")

st.write("Enter the grades and credits for each subject to calculate your CGPA.")

# Default number of subjects
num_subjects = st.number_input("Number of subjects:", min_value=1, step=1, value=5)

grades = []
credits = []

for i in range(num_subjects):
    col1, col2 = st.columns(2)
    with col1:
        grade = st.number_input(f"Grade points (0-10) for Subject {i+1}:", min_value=0.0, max_value=10.0, step=0.1, key=f"grade_{i}")
    with col2:
        credit = st.number_input(f"Credits for Subject {i+1}:", min_value=0.1, step=0.1, key=f"credit_{i}")
    grades.append(grade)
    credits.append(credit)

if st.button("Calculate CGPA"):
    total_points = sum([g*c for g, c in zip(grades, credits)])
    total_credits = sum(credits)
    if total_credits == 0:
        st.warning("Total credits cannot be zero!")
    else:
        cgpa = total_points / total_credits
        st.success(f"Your CGPA is: {cgpa:.2f}")
