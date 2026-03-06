import streamlit as st
import pandas as pd

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

