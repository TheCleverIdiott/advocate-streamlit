import streamlit as st  # building web apps in python
import streamlit.components.v1 as components

st.set_page_config(page_title="advocate.ai", layout="wide", initial_sidebar_state="expanded")

st.sidebar.markdown('''**Features**
- Trained extensively on IPC, CRPC & Indian Constitution
                    
- Provides step-by-step legal advice and assistance.

- Support 22 Indian Languages.

- Breaks down underlying nuances and intricacies of legal statutes of IPC & CRPC to provide a more simplified understanding for the common man.
                    
- Location-based lawyer contacts.
                    
- ADVO continually refines its knowledge base by utilizing user queries to update its understanding to provide up-to-date responses.
                    
''')
def run():
    iframe_src = "https://streamlit-advo.pages.dev/"
    components.iframe(iframe_src, height=800, scrolling=False)

run()