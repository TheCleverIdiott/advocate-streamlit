import streamlit as st
from txtai.pipeline import Summary, Textractor
from PyPDF2 import PdfReader

st.set_page_config(page_title="advocate.ai", layout="wide", initial_sidebar_state="expanded")

def text_summary(text, maxlength=None):
    #create summary instance
    summary = Summary()
    text = (text)
    result = summary(text)
    return result

def extract_text_from_pdf(file_path):
    # Open the PDF file using PyPDF2
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text

choice = st.sidebar.selectbox("Select your choice", ["Simplify Text", "Simplify Document"])
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.write("____")
st.sidebar.markdown('''
Simplify Complex legal terms and documents.
We can summarize long texts into shorter ones while preserving the main ideas. 
Use **Advocate AI** to make sense of complex legal texts and summarize them into simpler terms. You can also use it to summarize a document containing multiple pages.                
''')

if choice == "Simplify Text":
    st.subheader("Simplify Text")
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

elif choice == "Simplify Document":
    st.subheader("Simplify Document")
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
                