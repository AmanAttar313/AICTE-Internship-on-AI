import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:  # Check for None values
            text += page_text
    return text

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    # Combine job description with resumes
    documents = [job_description] + resumes
    
    # Convert text to TF-IDF vectors
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    # Calculate cosine similarity
    job_description_vector = vectors[0]  # First vector (job description)
    resume_vectors = vectors[1:]  # Remaining vectors (resumes)

    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()
    
    return cosine_similarities

# Streamlit app
st.title("AI Resume Screening & Candidate Ranking System")

# Job description input
st.header("Job Description")
job_description = st.text_area("Enter the job description")

# File uploader
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.header("Ranking Resumes")
    
    resumes = []
    file_names = []

    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        if text.strip():  # Ensure the extracted text is not empty
            resumes.append(text)
            file_names.append(file.name)
        else:
            st.warning(f"No text extracted from {file.name}. Please check the file.")

    if resumes:
        # Rank resumes
        scores = rank_resumes(job_description, resumes)

        # Display scores
        results = pd.DataFrame({"Resume": file_names, "Score": scores})
        results = results.sort_values(by="Score", ascending=False)

        st.write(results)
    else:
        st.warning("No valid resumes to process. Please upload valid PDF files.")
else:
    st.info("Please enter a job description and upload resumes to begin.")
