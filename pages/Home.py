import streamlit as st

st.set_page_config(
    page_title="advocate.ai",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.title("Advocate.ai - Your Gateway to Empowered Justice!")

import streamlit as st

def Home():
    iframe_code = """
    <div style="display: flex; justify-content: center;">
        <iframe width="600" height="340" src="https://www.youtube.com/embed/j869V86b8xw?mute=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;    clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    """
    
    st.markdown(iframe_code, unsafe_allow_html=True)
    
    st.text("")
    st.text("")
    
    st.markdown('''
    
    🌐 Tired of legal complexities hindering justice? Say goodbye to expensive lawyer visits and uncertainty. Meet Advo, your AI legal companion!
    
    🤖 **Unlock the Power of Legal Clarity:**
    Advo, our AI chatbot, is your personalized legal guide. Trained on the Indian Constitution, IPC, and CRPC, it simplifies legal jargon, providing short advice and step-by-step  solutions tailored to your situation.
    
    🔗 **Seamless Integration, Unlimited Access:**
    Advo seamlessly integrates into any website, bridging the gap between government resources and the public. No more endless searches; get the legal information you need     instantly!
    
    🌐 **Break the Language Barrier:**
    With support for 22 Indian languages, Advo ensures everyone, irrespective of language, understands their rights. Justice is for everyone, and language should never be a    barrier!
    
    📞 **Personalized Support for Complex Cases:**
    Facing a challenging situation? Advo doesn't just stop at information; we offer one-on-one on-call support for complicated cases. Your justice journey is our priority!
    
    💡 **Advocate.ai - Empowering You with Legal Clarity, One Click at a Time!**
    
    
    🔍 Don't just navigate the legal system; let Advo guide you. Your rights, your justice, simplified! #AdvocateForJustice #LegalEmpowerment #AdvoAI
    
    ''')