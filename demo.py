import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Udaan - Mentorship Demo", layout="centered")

# Title & Introduction
st.title("🛫 Welcome to Udaan")
st.markdown("""
Udaan is a mentorship platform built to connect students with mentors who can guide them through academic and career choices.  
We aim to reduce information gaps, empower students, and foster a support ecosystem from high school onwards.
""")

# Choose user type
user_type = st.radio("Who are you?", ("🎓 Student", "🎓 Mentor"))

# Student Form
if user_type == "🎓 Student":
    st.header("Student Registration")
    name = st.text_input("Full Name")
    school = st.text_input("School / Institution")
    interests = st.text_area("What subjects or careers are you interested in?")
    challenges = st.text_area("What kind of guidance are you looking for?")

    if st.button("Submit as Student"):
        if name and school:
            st.success(f"Thanks, {name}! Your interests have been recorded.")
            st.markdown(f"🔍 We'll try to match you with a suitable mentor based on your interests in:\n- {interests}")

            new_data = {
                "Name": name,
                "School": school,
                "Interests": interests,
                "Challenges": challenges
            }

            df = pd.DataFrame([new_data])
            file_path = "student_submissions.csv"
            if os.path.exists(file_path):
                df.to_csv(file_path, mode='a', header=False, index=False)
            else:
                df.to_csv(file_path, index=False)
        else:
            st.warning("Please fill out at least your name and school.")

# Mentor Form
elif user_type == "🎓 Mentor":
    st.header("Mentor Sign-Up")
    name = st.text_input("Full Name")
    background = st.text_input("Educational/Professional Background")
    expertise = st.text_area("What areas can you mentor in?")
    availability = st.selectbox("How often can you mentor?", ["Once a month", "Twice a month", "Weekly", "Flexible"])

    if st.button("Submit as Mentor"):
        if name and background:
            st.success(f"Welcome aboard, {name}! Your willingness to mentor in:\n- {expertise}\n is deeply appreciated.")
            st.markdown("🧠 We'll reach out when a suitable student match is available.")

            new_data = {
                "Name": name,
                "Background": background,
                "Expertise": expertise,
                "Availability": availability
            }

            df = pd.DataFrame([new_data])
            file_path = "mentor_submissions.csv"
            if os.path.exists(file_path):
                df.to_csv(file_path, mode='a', header=False, index=False)
            else:
                df.to_csv(file_path, index=False)
        else:
            st.warning("Please fill out at least your name and background.")

# Footer
st.markdown("---")
st.caption("🚀 This is a demo version of Udaan. Full platform coming soon!")
