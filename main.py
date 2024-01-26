import pdfplumber
import easyocr

class PdfOCR:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def extract_text_from_page(self, page_number):
        with pdfplumber.open(self.pdf_path) as pdf:
            page = pdf.pages[page_number]
            text = page.extract_text()
        return text

    def extract_text_from_all_pages(self):
        with pdfplumber.open(self.pdf_path) as pdf:
            all_text = [page.extract_text() for page in pdf.pages]
        return all_text

    def convert_pdf_to_images(self):
        with pdfplumber.open(self.pdf_path) as pdf:
            images = [page.to_image() for page in pdf.pages]
        return images

    def perform_ocr_on_images(self, images):
        reader = easyocr.Reader(['en'])
        extracted_text = []
        for image in images:
            result = reader.readtext(image.to_pil())
            text = ' '.join([entry[1] for entry in result])
            extracted_text.append(text)
        return extracted_text

def process_pdf(pdf_path):
    pdf_ocr = PdfOCR(pdf_path)

    # Extract text from a specific page
    page_number = 0  # Change to the desired page number
    text_from_page = pdf_ocr.extract_text_from_page(page_number)
    print(f"Text from page {page_number + 1}:\n{text_from_page}\n")

    # Extract text from all pages
    all_text = pdf_ocr.extract_text_from_all_pages()
    print(f"Text from all pages:\n{all_text}\n")

    # Convert PDF to images and perform OCR on the images
    pdf_images = pdf_ocr.convert_pdf_to_images()
    ocr_results = pdf_ocr.perform_ocr_on_images(pdf_images)

    for i, result in enumerate(ocr_results):
        print(f"OCR Result for page {i + 1}:\n{result}\n")

if __name__ == "__main__":
    pdf_path = "data/sample.pdf"
    process_pdf(pdf_path)
