import streamlit as st


def display_about_us():
    st.title("About Us")
    st.write("## TIGOR Team Members")

    team_members = [
        {"name": "Gladys Kimosop", "student-no": "34643245"},
        {"name": "Om Prakash Puri", "student-no": "34857674"},
        {"name": "Khuram Shahzad", "student-no": "32627109"},
        {"name": "Rabjot Kaur", "student-no": "34517096"},
        {"name": "Ian Kumu", "student-no": "34929478"},
        {"name": "Tan Phong Nguyen", "student-no": "34807741"}
    ]

    for member in team_members:
        st.write(f"**{member['name']}** - {member['student-no']}")


display_about_us()
