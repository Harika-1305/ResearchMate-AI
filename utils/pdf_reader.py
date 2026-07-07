import fitz
import pytesseract
from pdf2image import convert_from_bytes

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text(pdf_file):

    try:

        pdf_bytes = pdf_file.read()

        # =====================================
        # Normal PDF Text Extraction
        # =====================================

        pdf = fitz.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        text = ""

        for page in pdf:

            text += page.get_text()

        # Return if text exists

        if text.strip():

            return text

        # =====================================
        # OCR Fallback
        # =====================================

        images = convert_from_bytes(
            pdf_bytes,
            poppler_path=r"C:\Program Files\poppler-26.02.0\Library\bin"
        )

        ocr_text = ""

        for image in images:

            ocr_text += pytesseract.image_to_string(
                image
            )

        return ocr_text

    except Exception as e:

        return (
            f"Error extracting text: {str(e)}"
        )