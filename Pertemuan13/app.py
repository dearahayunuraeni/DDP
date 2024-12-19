import streamlit as st

home = st.Page("./pages/dashboard.py", title="Home")
nabung = st.Page("./pages/nabung.py", title="Nabung")

pg = st.navigation({
    "Dashboard" : [home],
    "Nabung" : [nabung],
})

if "Nabung" not in st.session_state:
    st.session_state['Nabung'] = []

pg.run()