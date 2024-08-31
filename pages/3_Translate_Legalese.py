import streamlit as st  # building web apps in python
from PIL import Image  # for opening image files
from datetime import date  # provides date & time functions
from gtts import gTTS, lang  # for text speech
from googletrans import Translator  # provides translation functions
from PyPDF2 import PdfReader  # for reading pdf files

st.set_page_config(page_title="advocate.ai", layout="wide", initial_sidebar_state="expanded")

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

choice = st.sidebar.selectbox("Select your choice", ["Translate Text", "Translate Document"])
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.write("____")
st.sidebar.markdown('''
Translate Legal Documents and Texts.
Keeping in mind the diversity of our Nation we have integrated a feature to translate legal documents and texts into your local language.
Use **Advocate AI** to translate legal documents and texts into your local language. You can also use it to translate a document containing multiple pages.               
''')

# instance of Translator()
trans = Translator()

# gets gtts supported languages as dict
langs = lang.tts_langs()
langs2 = lang.tts_langs()

if choice == "Translate Text":
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