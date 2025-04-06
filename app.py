import streamlit as st
from PIL import Image
import pytesseract

st.set_page_config(page_title="OCR Image to Text App", layout="centered")

st.title("📝 OCR Image to Text")
st.write("Upload a handwritten or printed image and extract text using OCR.")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Extracting text..."):
        text = pytesseract.image_to_string(image)

    st.subheader("🧾 Extracted Text:")
    st.text_area("Result", text, height=250)

    if st.button("Copy Text"):
        st.toast("Text copied! Use CTRL+C to paste.")
