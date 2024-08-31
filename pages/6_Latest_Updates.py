import streamlit as st  # building web apps in python
import streamlit.components.v1 as components

st.set_page_config(page_title="advocate.ai", layout="wide", initial_sidebar_state="expanded")

st.sidebar.text("")
st.sidebar.text("")

st.sidebar.markdown('''
With Laws being chnages everyday and new cases being filed every minute, it is important to keep up with the legal landscape of India.
Use **Advo News** to stay updated with the latest news and updates.
''')

def news():
    iframe_src = "https://advo-news.pages.dev/"
    components.iframe(iframe_src, height=750, scrolling=True)

news()