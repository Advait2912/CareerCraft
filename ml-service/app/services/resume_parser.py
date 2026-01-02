import pdfplumber
from docx import Document
import io 

def extract_textpdf(file_bytes):
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        #this will extract all the pages and join them

        return "\n".join(page.extract_text() or "" for page in pdf.pages)

def extract_textdocs(file_bytes):
    doc = Document(io.BytesIO(file_bytes))
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)
