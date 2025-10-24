import fitz
import docx

def extract_text_from_pdf(path: str) -> str:
    doc = fitz.open(path)
    text = []
    for page in doc:
        text.append(page.get_text())
    return "\n".join(text)

def extract_text_from_docx(path: str) -> str:
    doc = docx.Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

def extract_text(path: str, filename: str) -> str:
    if filename.endswith('.pdf'):
        return extract_text_from_pdf(path)
    elif filename.endswith('.docx'):
        return extract_text_from_docx(path)
    else:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
