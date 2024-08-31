import streamlit as st

st.set_page_config(page_title="advocate.ai", layout="wide", initial_sidebar_state="expanded")


calendly_link = "https://calendly.com/advocateai/case-discussion"

st.markdown(f'<iframe src="{calendly_link}" width="100%" height="800px" style="border:0"></iframe>', unsafe_allow_html=True)

st.sidebar.text("")
st.sidebar.text("")
st.sidebar.info('''Got a case to discuss? Schedule a call with us!''')