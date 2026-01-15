import fitz
import pytesseract
from PIL import Image
from docx import Document

# Explicit Tesseract path (Windows-safe)
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def clean_text(text: str) -> str:
    lines = [l.strip() for l in text.splitlines()]
    lines = [l for l in lines if len(l) > 3]
    return "\n".join(lines)


def load_pdf(data: bytes) -> str:
    doc = fitz.open(stream=data, filetype="pdf")
    extracted = []

    for page in doc:
        text = page.get_text().strip()
        if text:
            extracted.append(text)
        else:
            pix = page.get_pixmap(dpi=300)
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            extracted.append(
                pytesseract.image_to_string(img, config="--oem 3 --psm 6")
            )

    doc.close()
    final = clean_text("\n".join(extracted))

    if not final:
        raise ValueError("Unable to extract text from PDF")

    return final


def load_txt(data: bytes) -> str:
    return data.decode("utf-8", errors="ignore").strip()


def load_docx(data: bytes) -> str:
    doc = Document(data)
    return "\n".join(p.text for p in doc.paragraphs).strip()


def extract_text(uploaded_file) -> str:
    name = uploaded_file.name.lower()
    data = uploaded_file.read()

    if name.endswith(".pdf"):
        return load_pdf(data)
    elif name.endswith(".txt"):
        return load_txt(data)
    elif name.endswith(".docx"):
        return load_docx(data)
    else:
        raise ValueError("Unsupported file type")
