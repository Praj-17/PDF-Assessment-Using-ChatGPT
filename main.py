import easyocr
from PIL import Image
from pdf2image import convert_from_path
import pytesseract

class HandwrittenPDFExtractor:
    def __init__(self, tesseract_cmd_path, easyocr_lang='en'):
        self.tesseract_cmd_path = tesseract_cmd_path
        self.easyocr_lang = easyocr_lang
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd_path
        self.reader = easyocr.Reader([easyocr_lang])

    def pdf_to_images(self, pdf_path):
        images = convert_from_path(pdf_path)
        print(type(images[0]))
        final_images = []
        pdf_name = pdf_path.split("/")[-1][:3]
        for i, image in enumerate(images):
            image = image.save(f'{pdf_name}_page_{i + 1}.jpg')
            final_images.append(f"{pdf_name}_page_{i + 1}.jpg")
            print(f'Saved page_{i + 1}.png')

        return final_images


    def extract_text_tesseract(self, image):
        print("Running Tesseract")
        text_tesseract = pytesseract.image_to_string(image, lang='eng')
        print(text_tesseract)
        return text_tesseract

    def extract_text_easyocr(self, image):
        result = self.reader.readtext(image)
        text_easyocr = '\n'.join([entry[1] for entry in result])
        return text_easyocr

    def extract_text_from_handwritten_pdf(self, pdf_path):
        images = self.pdf_to_images(pdf_path)
        extracted_text = []

        for i, image in enumerate(images):
            # text_tesseract = self.extract_text_tesseract(image)
            text_easyocr = self.extract_text_easyocr(image)

            extracted_text.append({
                # 'tesseract': text_tesseract
                'easyocr': text_easyocr
            })

        return extracted_text

if __name__ == "__main__":
    tesseract_cmd_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pdf_extractor = HandwrittenPDFExtractor(tesseract_cmd_path)

    pdf_path = "data/sample2.pdf"
    extracted_text = pdf_extractor.extract_text_from_handwritten_pdf(pdf_path)

    for i, text_dict in enumerate(extracted_text):
        print(f"Page {i+1}:\nTesseract OCR:\n\nEasyOCR:\n{text_dict['easyocr']}\n")
