import os
import PyPDF2
import streamlit as st

def count_pdf_pages(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            return len(reader.pages)
    except Exception as e:
        st.error(f"Error reading {pdf_path}: {e}")
        return 0

def count_pages_in_folder(folder_path):
    total_pages = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                total_pages += count_pdf_pages(pdf_path)
    return total_pages

st.title("PDF Page Counter")

# Input box to enter the folder path
folder_path = st.text_input("Enter the path to the folder containing PDFs:", "")

if st.button("Count Pages"):
    if folder_path:
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            total_pages = count_pages_in_folder(folder_path)
            st.success(f"Total number of pages in all PDFs: {total_pages}")
        else:
            st.error("The provided path is not a valid directory.")
    else:
        st.warning("Please enter a folder path.")
    
