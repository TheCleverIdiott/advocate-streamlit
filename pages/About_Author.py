import streamlit as st  # building web apps in python
import streamlit.components.v1 as components


st.set_page_config(page_title="advocate.ai", layout="wide", initial_sidebar_state="expanded")
def author():
    iframe_src = "https://aritraghosh.xyz/"
    components.iframe(iframe_src, height=750, scrolling=True)

st.sidebar.info("Join me in creating a society where everyone is informed, aware, and empowered! Together, let's pave the way for justice and equality. Don't let lack of knowledge be a hurdle – choose advocate.ai and let justice prevail!")

st.write("This site was developed by:")
author()
