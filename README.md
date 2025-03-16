# AICTE-Internship-on-AI
AICTE Internship on AI: Transformative Learning  with  TechSaksham – A joint CSR initiative of Microsoft &amp; SAP

📄 AI-Powered Resume Screening and Ranking System
An AI-driven application that automates the process of screening and ranking resumes based on their relevance to a given job description. Built using Python, Streamlit, and Machine Learning techniques, this system enhances the recruitment process by minimizing manual effort and bias.

🚀 Features
📄 Upload Multiple Resumes (PDF format)
📝 Input Job Description to define candidate criteria
⚙️ Text Extraction from PDFs using PyPDF2
🧠 TF-IDF Vectorization to process textual data
🔍 Cosine Similarity for calculating resume relevance
📊 Ranking System to sort resumes by similarity score
⚠️ Error Handling for invalid files or empty inputs
📈 Real-Time Results Display using Streamlit
📚 Tech Stack
Frontend: Streamlit
Backend: Python
Libraries:
PyPDF2 – for PDF text extraction
scikit-learn – for TF-IDF vectorization and cosine similarity
pandas – for data manipulation and result visualization
⚙️ Installation and Setup
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/ai-resume-ranking.git
cd ai-resume-ranking
2. Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate         # For Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Streamlit App
bash
Copy
Edit
streamlit run aman_resume_ranking.py
5. Access the App
The app will open in your default web browser at:

arduino
Copy
Edit
http://localhost:8501
🧩 How the System Works
Enter Job Description:

Provide a detailed job description specifying skills and qualifications.
Upload Resumes:

Upload multiple PDF resumes for evaluation.
AI Processing:

The system extracts text from each resume.
Converts text into numerical vectors using TF-IDF.
Calculates similarity using Cosine Similarity.
View Results:

Displays a table ranking resumes based on their relevance to the job description.
💡 Sample Usage
python
Copy
Edit
# Run this in the terminal
streamlit run aman_resume_ranking.py
Input the job description in the text box.
Upload multiple resumes (PDF format).
Click "Rank Resumes" to view the ranked results.
🔄 Project Workflow
Input Job Description ➡️
Upload PDF Resumes ➡️
Text Extraction using PyPDF2 ➡️
TF-IDF Vectorization ➡️
Cosine Similarity Calculation ➡️
Ranking and Displaying Results
🛠️ Key Functions
extract_text_from_pdf(file)

Extracts text from a given PDF file.
rank_resumes(job_description, resumes)

Processes the job description and resumes using TF-IDF and calculates similarity using cosine similarity.
st.file_uploader()

Allows uploading multiple resumes.
st.write()

Displays the results in a tabular format.
⚠️ Error Handling
Alerts users if:
The uploaded file is not a PDF.
No valid text is extracted from the PDF.
The job description is missing.
🔄 Future Enhancements
✅ Integrate with OCR tools for scanning image-based PDFs.
✅ Add support for other file formats like DOCX.
✅ Enhance UI for better user interaction.
✅ Export results to CSV or Excel.
