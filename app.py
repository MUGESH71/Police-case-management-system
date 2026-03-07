import streamlit as st
import pandas as pd
from models.case import Case
from utils import load_case,save_case

st.title("Police Case Management System")
st.header("Welcome to Dashboard")

menu=st.sidebar.selectbox(
    "Menu",
    [
        "Register Officer",
        "View Officers",
        "Register Case",
        "Assign Officer to Case",
        "Search Case",
        "Update Case Status",
        "Case Dashboard"
        #Ashwin changed this line
    ]
    )


if menu=="Register Officer":
    pass
elif menu=="View Officer":
    pass
elif menu== "Register Case":
    Case_details=load_case()
    st.header("Register New Case")
    case_id=st.text_input("Case ID")
    title=st.text_input("Case title")
    description=st.text_input("Case description")
    assigned_officer=st.text_input("Assigned officer")
    status=st.selectbox("Case status",["Open","Under Investigation","Closed"])
    date=st.date_input("Date Created")

    if st.button("Register_case"):
        new_case=Case(
            case_id,
            title,
            description,
            status,
            assigned_officer,
            str(date)
        )
        Case_details.append(new_case.to_dict())
        save_case(Case_details)
        st.success("Registered sucessfully")

elif menu=="Assign Officer to Case":
    pass
elif menu=="Search Case":
    pass
elif menu=="Update Case Status":
    pass
elif menu == "Case Dashboard":
    pass
