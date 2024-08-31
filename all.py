import pickle
from pathlib import Path
import streamlit_authenticator as stauth

import streamlit as st  # building web apps in python
from PIL import Image  # for opening image files
from datetime import date  # provides date & time functions
from gtts import gTTS, lang  # for text speech
from googletrans import Translator  # provides translation functions
from PyPDF2 import PdfReader
from txtai.pipeline import Summary, Textractor

from cProfile import label
from distutils import extension
import streamlit as st
import pytesseract
from pytesseract import Output
from ocr_utils import *
import os
import warnings

import streamlit.components.v1 as components

# setting app's title, icon & layout
st.set_page_config(page_title="advocate.ai", page_icon="⚖️", layout="wide", initial_sidebar_state="expanded")



# ## AUTH
# names = ["Aritra Ghosh", "hello", "hehe hehe"]
# usernames = ["aritrag1905@gmail.com", "hello@gmail.com", "soclicheobelisk@gmail.com"]

# # load hashed passwords
# file_path = Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rb") as file:
#     hashed_passwords = pickle.load(file)

# authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "advocate-ai", "abcdef", cookie_expiry_days=30)

# name, authentication_status, username = authenticator.login("Login", "main")

# if authentication_status == False:
#     st.error("Username/password is incorrect")

# if authentication_status == None:
#     st.warning("Please enter your username and password")

# if authentication_status:


def all():
    def text_summary(text, maxlength=None):
        #create summary instance
        summary = Summary()
        text = (text)
        result = summary(text)
        return result
    
    def get_key(val):
        for key, value in lang.tts_langs().items():
            if val == value:
                return key
            
    def get_key2(val):
        for key, value in lang.tts_langs().items():
            if val == value:
                return key
             
    def extract_text_from_pdf(file_path):
        # Open the PDF file using PyPDF2
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            page = reader.pages[0]
            text = page.extract_text()
        return text
    
    def ocr(file_name):
            image = Image.open(file_name)
            image = np.array(image)
            d = pytesseract.image_to_data(image, output_type=Output.DICT)
            n_boxes = len(d["level"])
            boxes = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
            for i in range(n_boxes):
                (x, y, w, h) = (d["left"][i], d["top"][i], d["width"][i], d["height"][i])
                boxes = cv2.rectangle(boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)
            extracted_text = pytesseract.image_to_string(image, lang="eng")
            # pdf = pytesseract.image_to_pdf_or_hocr(image, lang="fas", extension="pdf")
            # hocr = pytesseract.image_to_pdf_or_hocr(image, lang="fas", extension="hocr")
            return boxes, extracted_text
    
    def run():
        iframe_src = "https://streamlit-advo.pages.dev/"
        components.iframe(iframe_src, height=800, scrolling=False)
    
    def news():
        iframe_src = "https://advo-news.pages.dev/"
        components.iframe(iframe_src, height=800, scrolling=False)

    def call():
        iframe_src = "https://advo-news.pages.dev/"
        components.iframe(iframe_src, height=800, scrolling=False)

    def author():
        iframe_src = "https://aritraghosh.xyz/"
        components.iframe(iframe_src, height=750, scrolling=True)
    
    def doc_gen():
        iframe_src = "https://advo-docgen.pages.dev/"
        components.iframe(iframe_src, height=750, scrolling=True)
    
        

    
    choice = st.sidebar.selectbox("Select your choice", ["Overview", "ChatBot", "OCR", "Translate Text", "Translate Document", "Generate Document", "Summarize Text", "Summarize Document", "Latest Updates", "Schedule a Call", "Author"])
    
    
    def main():
        # instance of Translator()
        trans = Translator()
    
        # gets gtts supported languages as dict
        langs = lang.tts_langs()
        langs2 = lang.tts_langs()
    
    
        if choice == "ChatBot":
            run()
    
    
    
        elif choice == "Image Scanner":
            st.title("Advo Scanner")
    
            input_col, output_col = st.columns(2)
            with input_col:
                with st.form("form2", clear_on_submit=True):
                    content_file = st.file_uploader("Upload your image here")
                    # content_file = file_selector()
                    submit = st.form_submit_button("Submit")
                    if submit:
                        if content_file is not None:
                            result_image, extracted_text = ocr(content_file)
                            with output_col:
                                st.image(
                                    result_image,
                                    caption="OCR",
                                    use_column_width="always",
                                    output_format="PNG",
                                )
                                with input_col:
                                    st.markdown(
                                        f'<div dir="ltr" style="text-align: justify;">{extracted_text}</div>',
                                        unsafe_allow_html=True,
                                    )
            
                                    download_txt = st.download_button(label="Download Text", data=extracted_text, file_name=f"OCR_{content_file.name.split('.')[0]}.txt",   mime="text/plain")
    
            
    
    
        elif choice == "Overview":
            st.title("Advocate.ai - Your Gateway to Empowered Justice!")
            iframe_code = """
                <div style="display: flex; justify-content: center;">
                    <iframe width="600" height="340" src="https://www.youtube.com/embed/j869V86b8xw?mute=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen><iframe>
                </div>
            """
            st.markdown(iframe_code, unsafe_allow_html=True)

            st.text("")
            st.text("")

            st.markdown('''

                🌐 Tired of legal complexities hindering justice? Say goodbye to expensive lawyer visits and uncertainty. Meet Advo, your AI legal companion!

                🤖 **Unlock the Power of Legal Clarity:**
                Advo, our AI chatbot, is your personalized legal guide. Trained on the Indian Constitution, IPC, and CRPC, it simplifies legal jargon, providing short advice and step-by-step solutions tailored to your situation.

                🔗 **Seamless Integration, Unlimited Access:**
                Advo seamlessly integrates into any website, bridging the gap between government resources and the public. No more endless searches; get the legal information you need instantly!

                🌐 **Break the Language Barrier:**
                With support for 22 Indian languages, Advo ensures everyone, irrespective of language, understands their rights. Justice is for everyone, and language should never be a barrier!

                📞 **Personalized Support for Complex Cases:**
                Facing a challenging situation? Advo doesn't just stop at information; we offer one-on-one on-call support for complicated cases. Your justice journey is our priority!

                💡 **Advocate.ai - Empowering You with Legal Clarity, One Click at a Time!**

                🔍 Don't just navigate the legal system; let Advo guide you. Your rights, your justice, simplified! #AdvocateForJustice #LegalEmpowerment #AdvoAI

            ''')
    
        elif choice == "Translate Text":
            # display current date & header
            st.header("Advo Translator")
            st.write(f"Date : {date.today()}")
    
            input_text = st.text_input("Enter the text")  # gets text to translate
            lang_choice = st.selectbox(
                "Language to translate: ", list(langs.values())
            )  # shows the supported languages list as selectbox options
    
            if st.button("Translate"):
                if input_text == "":
                    # if the user input is empty
                    st.write("Please Enter text to translate")
    
                else:
                    detect_expander = st.expander("Detected Language")
                    with detect_expander:
                        detect = trans.detect([input_text])[
                            0
                        ]  # detect the user given text language
                        detect_text = f"Detected Language : {langs[detect.lang]}"
                        st.success(detect_text)  # displays the detected language
    
                        # # convert the detected text to audio file
                        # detect_audio = gTTS(text=input_text, lang=detect.lang, slow=False)
                        # detect_audio.save("user_detect.mp3")
                        # audio_file = open("user_detect.mp3", "rb")
                        # audio_bytes = audio_file.read()
                        # st.audio(audio_bytes, format="audio/ogg", start_time=0)
    
                    trans_expander = st.expander("Translated Text")
                    with trans_expander:
                        translation = trans.translate(
                            input_text, dest=get_key(lang_choice)
                        )  # translates user given text to target language
                        translation_text = f"Translated Text : {translation.text}"
                        st.success(translation_text)  # displays the translated text
    
                        # convert the translated text to audio file
                        translated_audio = gTTS(
                            text=translation.text, lang=get_key(lang_choice), slow=False
                        )
                        translated_audio.save("user_trans.mp3")
                        audio_file = open("user_trans.mp3", "rb")
                        audio_bytes = audio_file.read()
                        st.audio(audio_bytes, format="audio/ogg", start_time=0)
    
                        # download button to download translated audio file
                        with open("user_trans.mp3", "rb") as file:
                            st.download_button(
                                label="Download",
                                data=file,
                                file_name="trans.mp3",
                                mime="audio/ogg",
                            )
    
        elif choice == "Translate Document":
            st.subheader("Translate Document")
            input_file = st.file_uploader("Upload your document here", type=['pdf'])
            doc_lang_choice = st.selectbox(
                "Language to translate: ", list(langs2.values())
            )
            if input_file is not None:
                st.success("File uploaded successfully")
                
                if st.button("Translate Document"):
                    with open("doc_file.pdf", "wb") as f:
                        f.write(input_file.getbuffer())
                    
                    doc_detect_expander = st.expander("Detected Language")
                    with doc_detect_expander:
                        extracted_text = extract_text_from_pdf("doc_file.pdf")
                        doc_detect = trans.detect(extracted_text)
                        st.markdown("**Original Document Text:**")
                        detect_text = f"Detected Language : {langs2[doc_detect.lang]}"
                        st.info(extracted_text)
    
                        # convert the detected text to audio file
                        # text_detect_audio = gTTS(text=extracted_text, lang=doc_detect.lang, slow=False)
                        # text_detect_audio.save("text_user_detect.mp3")
                        # text_audio_file = open("text_user_detect.mp3", "rb")
                        # text_audio_bytes = text_audio_file.read()
                        # st.audio(text_audio_bytes, format="audio/ogg", start_time=0)
    
                    doc_trans_expander = st.expander("Translated Document Text")
                    with doc_trans_expander:
                        doc_translation = trans.translate(extracted_text, dest=get_key2(doc_lang_choice))
                        st.markdown("**Translated Document:**")
                        st.info(doc_translation.text)
    
                         # convert the translated text to audio file
                        doc_translated_audio = gTTS(
                            text=doc_translation.text, lang=get_key2(doc_lang_choice), slow=False
                        )
                        doc_translated_audio.save("doc_user_trans1.mp3")
                        doc_audio_file = open("doc_user_trans1.mp3", "rb")
                        doc_audio_bytes = doc_audio_file.read()
                        st.audio(doc_audio_bytes, format="audio/ogg", start_time=0)
    
                        # download button to download translated audio file
                        with open("doc_user_trans1.mp3", "rb") as file:
                            st.download_button(
                                label="Download",
                                data=file,
                                file_name="doc_trans.mp3",
                                mime="audio/ogg",
                            )
    
    
            else:
                st.write("Please Enter document to translate")
    
        elif choice == "Summarize Text":
            st.subheader("Summarize Text")
            input_text = st.text_area("Enter your text here")
            if input_text is not None:
                if st.button("Summarize Text"):
                    col1, col2 = st.columns([1,1])
                    with col1:
                        st.markdown("**Your Input Text**")
                        st.info(input_text)
                    with col2:
                        st.markdown("**Summary Result**")
                        result = text_summary(input_text)
                        st.success(result)
    
        elif choice == "Summarize Document":
            st.subheader("Summarize Document")
            input_file = st.file_uploader("Upload your document here", type=['pdf'])
            if input_file is not None:
                if st.button("Summarize Document"):
                    with open("doc_file.pdf", "wb") as f:
                        f.write(input_file.getbuffer())
                    col1, col2 = st.columns([1,1])
                    with col1:
                        st.info("File uploaded successfully")
                        extracted_text = extract_text_from_pdf("doc_file.pdf")
                        st.markdown("**Extracted Text is Below:**")
                        st.info(extracted_text)
                    with col2:
                        st.markdown("**Summary Result**")
                        text = extract_text_from_pdf("doc_file.pdf")
                        doc_summary = text_summary(text)
                        st.success(doc_summary)

        elif choice == "Latest Updates":
            news()

        elif choice == "Schedule a Call":
            calendly_link = "https://calendly.com/advocateai/case-discussion"
            st.markdown(f'<iframe src="{calendly_link}" width="100%" height="800px" style="border:0"></iframe>', unsafe_allow_html=True)
    
        elif choice == "Author":
            author()

        elif choice == "Generate Document":
            doc_gen()


    # if __name__ == "__main__":
    #     main() 
