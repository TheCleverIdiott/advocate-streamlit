import streamlit as st
from pathlib import Path
import streamlit_authenticator as stauth
import pickle
from streamlit.source_util import get_pages

from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import json

from pages.Home import *

# st.set_page_config(page_title="advocate.ai", page_icon="⚖️", layout="wide", initial_sidebar_state="expanded")


DEFAULT_PAGE = "1_login.py"
SECOND_PAGE_NAME = "app"


def get_all_pages():
    default_pages = get_pages(DEFAULT_PAGE)

    pages_path = Path("pages.json")

    if pages_path.exists():
        saved_default_pages = json.loads(pages_path.read_text())
    else:
        saved_default_pages = default_pages.copy()
        pages_path.write_text(json.dumps(default_pages, indent=4))

    return saved_default_pages


def clear_all_but_first_page():
    current_pages = get_pages(DEFAULT_PAGE)

    if len(current_pages.keys()) == 1:
        return

    get_all_pages()

    # Remove all but the first page
    key, val = list(current_pages.items())[0]
    current_pages.clear()
    current_pages[key] = val

    _on_pages_changed.send()


def show_all_pages():
    current_pages = get_pages(DEFAULT_PAGE)

    saved_pages = get_all_pages()

    # Replace all the missing pages
    for key in saved_pages:
        if key not in current_pages:
            current_pages[key] = saved_pages[key]

    _on_pages_changed.send()


def hide_page(name: str):
    current_pages = get_pages(DEFAULT_PAGE)

    for key, val in current_pages.items():
        if val["page_name"] == name:
            del current_pages[key]
            _on_pages_changed.send()
            break





## AUTH
names = ["Aritra Ghosh", "hello", "hehe hehe"]
usernames = ["aritrag1905@gmail.com", "hello@gmail.com", "soclicheobelisk@gmail.com"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "advocate-ai", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    show_all_pages()
    # clear_all_but_first_page()
    st.title("Advocate.ai - Your Gateway to Empowered Justice!")
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
    
else:
    clear_all_but_first_page()

    
    