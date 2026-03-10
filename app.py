import streamlit as st
import pandas as pd
from models.case import Case
from models.officer import Officer
from utils import load_data,save_data
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Police Case Management System")

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

elif menu == "Case Dashboard":

    st.subheader("📊 Case Analytics Dashboard")
    st.divider()

    sns.set_style("whitegrid")
    sns.set_palette("pastel")

    case = load_data("cases")
    officers = load_data("officers")

    df_cases = pd.DataFrame(case)
    df_officers = pd.DataFrame(officers)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Cases", len(df_cases))
    col2.metric("Open Cases", (df_cases["Case status"]=="Open").sum())
    col3.metric("Closed Cases", (df_cases["Case status"]=="Closed").sum())

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(6,4))

        sns.countplot(
            x="Case status",
            data=df_cases,
            palette="Set2",
            ax=ax
        )

        for container in ax.containers:
            ax.bar_label(container)

        ax.set_title("Case Status Distribution", fontsize=13, fontweight="bold")
        ax.set_xlabel("Case Status")
        ax.set_ylabel("Number of Cases")

        plt.xticks(rotation=20)
        plt.tight_layout()

        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(6,4))

        sns.countplot(
            y="Assigned officer",
            data=df_cases,
            order=df_cases["Assigned officer"].value_counts().index,
            palette="viridis",
            ax=ax
        )

        for container in ax.containers:
            ax.bar_label(container)

        ax.set_title("Cases per Officer", fontsize=13, fontweight="bold")

        plt.tight_layout()

        st.pyplot(fig)

    st.divider()

    status_counts = df_cases["Case status"].value_counts()

    fig, ax = plt.subplots(figsize=(6,6))

    status_counts.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90,
        pctdistance=0.8,
        wedgeprops={"edgecolor": "black"},
        ax=ax
    )

    ax.set_title("Case Status Breakdown", fontsize=14, fontweight="bold")
    ax.set_ylabel("")

    centre_circle = plt.Circle((0,0), 0.60, fc="white")
    fig.gca().add_artist(centre_circle)

    plt.tight_layout()

    st.pyplot(fig)

    st.divider()

    if st.checkbox("Show raw case data"):
        st.dataframe(df_cases)