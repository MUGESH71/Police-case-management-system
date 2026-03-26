import streamlit as st
import pandas as pd
from models.case import Case
from models.officer import Officer
from utils import load_data, save_data
import seaborn as sns
import matplotlib.pyplot as plt

# ---------- CONFIG ----------
st.set_page_config(page_title="Police CMS", layout="wide")

# ---------- STYLING ----------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: #e2e8f0;
}
section[data-testid="stSidebar"] {
    background: #020617;
}
h1, h2, h3 {
    color: #38bdf8;
    font-weight: 700;
}
.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
    margin-bottom: 20px;
}
.stButton>button {
    background: linear-gradient(90deg, #3b82f6, #06b6d4);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
    font-weight: bold;
}
.stButton>button:hover {
    transform: scale(1.05);
    transition: 0.2s;
}
.stTextInput>div>div>input,
.stSelectbox>div>div,
textarea {
    background-color: #020617 !important;
    color: white !important;
    border-radius: 8px;
}
[data-testid="metric-container"] {
    background: #1e293b;
    border-radius: 12px;
    padding: 10px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1 style='text-align:center;'>🚔 Police Case Management System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Smart • Clean • Actually Usable</p>", unsafe_allow_html=True)

# ---------- MENU ----------
menu = st.sidebar.selectbox("Menu", [
    "Register Officer",
    "Search Officers",
    "Register Case",
    "Assign Officer",
    "Update Case Status",
    "Search Case",
    "Dashboard"
])

# ---------- HELPERS ----------
def is_valid_number(val):
    return val.isdigit()

# ---------- REGISTER OFFICER ----------
if menu == "Register Officer":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("👮 Register Officer")

    col1, col2 = st.columns(2)

    with col1:
        officer_id = st.text_input("Officer ID")
        name = st.text_input("Name")
        rank = st.text_input("Rank")
        station = st.text_input("Station")

    with col2:
        assigned = st.text_input("Cases Assigned", "0")
        pending = st.text_input("Cases Pending", "0")
        solved = st.text_input("Cases Solved", "0")
        contact = st.text_input("Contact Number")

    if st.button("➕ Add Officer"):
        if not officer_id.isdigit():
            st.error("Officer ID must be numeric")
        else:
            new_officer = Officer(
                int(officer_id), name, rank, station,
                assigned, pending, solved, contact
            )
            save_data("officers", new_officer.to_dict())
            st.success("Officer registered successfully")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- SEARCH OFFICER ----------
elif menu == "Search Officers":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔍 Search Officers")

    officers = load_data("officers")
    search = st.text_input("Enter Officer ID")

    if st.button("Search"):
        if not search.isdigit():
            st.warning("Enter valid ID")
        else:
            found = False
            for o in officers:
                if o["officer_id"] == int(search):
                    st.success("Officer Found")
                    st.json(o)
                    found = True
            if not found:
                st.error("Officer not found")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- REGISTER CASE ----------
elif menu == "Register Case":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📁 Register Case")

    col1, col2 = st.columns(2)

    with col1:
        case_id = st.text_input("Case ID")
        title = st.text_input("Title")
        desc = st.text_area("Description")

    with col2:
        officer = st.text_input("Assigned Officer")
        status = st.selectbox("Status", ["Open", "Under Investigation", "Closed"])
        date = st.date_input("Date")

    if st.button("📌 Register"):
        if not case_id.isdigit() or title == "":
            st.error("Invalid input")
        else:
            case = Case(int(case_id), title, desc, status, officer, str(date))
            save_data("cases", case.to_dict())
            st.success("Case registered")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- ASSIGN OFFICER ----------
elif menu == "Assign Officer":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔗 Assign Officer to Case")

    cases = load_data("cases")
    cid = st.text_input("Case ID")
    officer = st.text_input("Officer Name")

    if st.button("Assign"):
        updated = False
        for c in cases:
            if str(c["Case_id"]) == cid:
                c["Assigned officer"] = officer
                updated = True
        if updated:
            save_data("cases", cases)
            st.success("Assigned successfully")
        else:
            st.error("Case not found")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- UPDATE STATUS ----------
elif menu == "Update Case Status":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔄 Update Case Status")

    cases = load_data("cases")
    cid = st.text_input("Case ID")
    status = st.selectbox("New Status", ["Open", "Under Investigation", "Closed"])

    if st.button("Update"):
        updated = False
        for c in cases:
            if str(c["Case_id"]) == cid:
                c["Case status"] = status
                updated = True
        if updated:
            save_data("cases", cases)
            st.success("Status updated")
        else:
            st.error("Case not found")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- SEARCH CASE ----------
elif menu == "Search Case":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔍 Search Case")

    cases = load_data("cases")
    cid = st.text_input("Case ID")

    if st.button("Search"):
        found = False
        for c in cases:
            if str(c["Case_id"]) == cid:
                st.success("Case Found")
                st.json(c)
                found = True
        if not found:
            st.error("Not found")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- DASHBOARD ----------
elif menu == "Dashboard":
    st.subheader("📊 Analytics Dashboard")

    cases = load_data("cases")
    df = pd.DataFrame(cases)

    if df.empty:
        st.warning("No data yet")
    else:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        c1.metric("🚨 Total", len(df))
        c2.metric("🟡 Open", (df["Case status"]=="Open").sum())
        c3.metric("✅ Closed", (df["Case status"]=="Closed").sum())

        st.markdown('</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            fig, ax = plt.subplots()
            sns.countplot(x="Case status", data=df, ax=ax)
            ax.set_title("Case Status")
            st.pyplot(fig)

        with col2:
            fig, ax = plt.subplots()
            sns.countplot(
                y="Assigned officer",
                data=df,
                order=df["Assigned officer"].value_counts().index,
                ax=ax
            )
            ax.set_title("Cases per Officer")
            st.pyplot(fig)

        st.divider()

        fig, ax = plt.subplots()
        df["Case status"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)

        if st.checkbox("Show Data"):
            st.dataframe(df)