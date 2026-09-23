import fitz
from docx import Document


def extract_pdf_text(file):
    """
    Extract text from a PDF resume.
    """

    text = ""

    pdf = fitz.open(
        stream=file.read(),
        filetype="pdf"
    )

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text


def extract_docx_text(file):
    """
    Extract text from a DOCX resume.
    """

    document = Document(file)

    paragraphs = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            paragraphs.append(paragraph.text)

    return "\n".join(paragraphs)


def extract_txt_text(file):
    """
    Extract text from a TXT file.
    """

    return file.read().decode("utf-8")


def extract_resume_text(file):
    """
    Determine the file type and extract its text.
    """

    filename = file.name.lower()

    if filename.endswith(".pdf"):
        return extract_pdf_text(file)

    if filename.endswith(".docx"):
        return extract_docx_text(file)

    if filename.endswith(".txt"):
        return extract_txt_text(file)

    raise ValueError(
        "Unsupported file format. "
        "Please upload a PDF, DOCX, or TXT file."
    )