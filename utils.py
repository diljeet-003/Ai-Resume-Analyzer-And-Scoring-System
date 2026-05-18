import PyPDF2
import docx2txt

def extract_text(file):
    text = ""

    if file.name.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()

    elif file.name.endswith('.docx'):
        text = docx2txt.process(file)

    return text.lower()