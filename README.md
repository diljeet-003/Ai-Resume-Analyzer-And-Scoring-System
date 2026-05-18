AI Resume Analyzer and Scoring System
📌 Project Overview

The AI Resume Analyzer and Scoring System is an intelligent web application that analyzes resumes using Natural Language Processing (NLP) and Machine Learning techniques. The system extracts important information from resumes, compares candidate skills with job requirements, and generates a resume score along with recommendations for improvement.

The application helps:

Students improve resumes for placements
Recruiters shortlist candidates faster
Job seekers identify missing skills
HR teams automate resume screening

The project is developed using Python, Streamlit, Scikit-learn, NLTK, and TF-IDF Vectorization.

🚀 Features
📄 Upload Resume in PDF/DOCX format
🔍 Automatic Resume Parsing
🧠 AI-Based Resume Analysis
📊 Resume Score Generation
🛠 Skill Extraction
📈 Resume Strength & Weakness Detection
🎯 Job Recommendation System
📚 Course Recommendation
📋 Keyword Matching using NLP
📊 Data Visualization Dashboard
💡 Resume Improvement Suggestions
🏆 ATS (Applicant Tracking System) Compatibility Check
🛠 Technologies Used
Technology	Purpose
Python	Backend Programming
Streamlit	Web Application UI
NLTK	Natural Language Processing
Scikit-learn	Machine Learning
TF-IDF Vectorization	Keyword Importance
Cosine Similarity	Resume Matching
PyPDF2	PDF Text Extraction
Docx2txt	DOCX File Reading
Plotly	Data Visualization
Pandas	Data Handling
🧠 Machine Learning Concepts Used
1. TF-IDF Vectorization

TF-IDF (Term Frequency-Inverse Document Frequency) converts text into numerical vectors by measuring the importance of words in resumes.

Used for:

Skill extraction
Resume keyword analysis
Job description matching
2. Cosine Similarity

Cosine Similarity measures similarity between:

Resume content
Job description

Score Range:

0 → No similarity
1 → Perfect match
📂 Project Structure
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils.py
├── courses.py
├── skills.py
│
├── Uploaded_Resumes/
├── Images/
├── Data/
│
└── venv/
⚙️ Installation
Step 1: Clone Repository
git clone https://github.com/your-username/AI-Resume-Analyzer.git
Step 2: Open Project Folder
cd AI-Resume-Analyzer
Step 3: Create Virtual Environment
python -m venv venv
Step 4: Activate Environment
Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
Step 5: Install Dependencies
pip install -r requirements.txt
▶️ Run the Project
streamlit run app.py
📄 Supported Resume Formats
PDF (.pdf)
DOCX (.docx)
📊 Working Flow
User uploads resume
Resume text extraction
NLP preprocessing
TF-IDF vectorization
Skill extraction
Cosine similarity calculation
Resume scoring
Recommendations generation
Dashboard visualization
📈 Resume Score Parameters

The score is calculated based on:

Skills Match
Projects Mentioned
Certifications
Experience
Education
Resume Keywords
ATS Compatibility
Formatting Quality
💡 Example Output
Resume Score: 85/100

Strengths:
✔ Python
✔ Machine Learning
✔ SQL

Weaknesses:
✘ Missing Projects
✘ No Certifications

Suggestions:
- Add Machine Learning projects
- Include certifications
- Improve ATS formatting
📚 Future Enhancements
🤖 Deep Learning-Based Resume Ranking
🌐 LinkedIn Profile Analysis
🎤 AI Mock Interview System
☁ Cloud Deployment
📱 Android Application
🧠 GPT-Based Career Guidance
📹 Video Resume Analysis
🎯 Applications
College Placement Cells
HR Recruitment Systems
Career Guidance Platforms
Online Job Portals
ATS Screening Systems
🔐 Advantages
Saves Recruiter Time
Improves Resume Quality
Automated Candidate Screening
Fast Resume Evaluation
Accurate Skill Matching
User-Friendly Interface
⚠️ Limitations
Accuracy depends on resume quality
Limited to predefined skills database
Requires structured resume formatting
Not fully equivalent to human HR review
📸 Screenshots Section

Add screenshots of:

Home Page
Resume Upload Page
Resume Score Dashboard
Skill Analysis Graph
Recommendations Section
📋 Requirements.txt
streamlit
pandas
numpy
scikit-learn
nltk
plotly
PyPDF2
docx2txt
👨‍💻 Author

Developed by: Diljeet Kaur

Final Year Major Project
