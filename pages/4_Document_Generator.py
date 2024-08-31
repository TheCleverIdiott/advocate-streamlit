import streamlit as st  # building web apps in python
import streamlit.components.v1 as components

st.set_page_config(page_title="advocate.ai", layout="wide", initial_sidebar_state="expanded")

st.sidebar.text("")
st.sidebar.text("")
st.sidebar.markdown('''
Automating the long and tedious taskk of document generation.
Generate Documents Just by Filling a Form.
Save and Edit it according to your use.
Download it in PDF format.
                    
''')
def doc_gen():
    iframe_src = "https://advo-docgen.pages.dev/"
    components.iframe(iframe_src, height=750, scrolling=True)

doc_gen()