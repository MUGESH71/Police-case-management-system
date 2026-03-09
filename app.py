import streamlit as st
import pandas as pd
from models.case import Case
from models.officer import Officer
from utils import load_data,save_data

st.title("Police Case Management System")
st.header("Welcome to Dashboard")

menu=st.sidebar.selectbox(
    "Menu",
    [
        "Register Officer",
        "Search Officers",
        "Register Case",
        "Assign Officer to Case",
        "Search Case",
        "Update Case Status",
        "Case Dashboard"
        
    ]
    )


if menu=="Register Officer":
    st.header("Register Officer")
    
    officer_id=st.text_input("Officer ID")
    Name=st.text_input("Name")
    Rank=st.text_input("Rank")
    Station=st.text_input("Station")
    Case_Assigned=st.text_input("Case Assigned")
    Case_Pending=st.text_input("Case Pending")
    Case_solved=st.text_input("Case Solved")
    Contact_Number=st.text_input("Contact Number")
    if st.button("Add"):
        
        new_officer=Officer(
            
                int(officer_id),
                Name,
                Rank,
                Station,
                Case_Assigned,
                Case_Pending,
                Case_solved,
                Contact_Number

        )
 
        save_data("officers",new_officer.to_dict())
        st.success("Registered sucessfully")



elif menu=="Search Officers":
    st.header("Search Officers")
    Officers=load_data("officers")
    search_id=st.text_input("Enter officer ID")


    if search_id=="":
        st.warning("Please Enter Officer ID")
    else:
        search_id=int(search_id)
        if st.button("Search"):
            for officer in Officers:
                if officer["officer_id"]==search_id:
                    st.write(officer)
                    break
            else:
                st.write("Officer not found")



elif menu== "Register Case":
    
    st.header("Register New Case")


    case_id=st.text_input("Case ID")

    title=st.text_input("Case title")

    description=st.text_input("Case description")

    assigned_officer=st.text_input("Assigned officer")

    status=st.selectbox("Case status",["Open","Under Investigation","Closed"])

    date=st.date_input("Date Created")

    if st.button("Register_case"):
        if case_id=="" or title=="":
            st.error("Case ID and title are required")
        else:
            new_case=Case(
                int(case_id),
                title,
                description,
                status,
                assigned_officer,
                str(date)
            )

            save_data("cases",new_case.to_dict())

            st.success("Registered sucessfully")

elif menu=="Assign Officer to Case":
    pass
elif menu=="Search Case":
    cases=load_data("cases")
    st.header("Search Case")
    search_id=st.text_input("Enter case ID")
    if  search_id=="":
        st.warning("Please enter the case ID")
    else:
        if st.button("Search"):
            
            search_id=int(search_id)
            for case in cases:
                if case["Case_id"]==search_id:
                    st.write(case)
                    break
            else:
                st.write("Case not found")

elif menu=="Update Case Status":
    pass
elif menu == "Case Dashboard":
    pass








