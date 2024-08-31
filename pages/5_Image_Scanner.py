import streamlit as st  # building web apps in python
from cProfile import label
from distutils import extension
import streamlit as st
import pytesseract
from pytesseract import Output
from ocr_utils import *
import os
import warnings

st.set_page_config(page_title="advocate.ai", layout="wide", initial_sidebar_state="expanded")

st.sidebar.text("")
st.sidebar.text("")
st.sidebar.markdown('''
Extract text from images and documents.
Use **Advo Scanner** to extract text from images and documents. You can also use it to extract text from a document containing multiple pages.
**Advocate AI** is a powerful tool that uses OCR (Optical Character Recognition) to extract text from images and documents.
You can upload your own image or document file, select an available template (if you want), customize the settings, and then extract the text from the image or document file.
''')

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
                        download_txt = st.download_button(label="Download Text", data=extracted_text, file_name=f"OCR_{content_file.name.split('.')[0]}.txt", mime="text/plain")