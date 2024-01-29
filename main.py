import easyocr
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import speech_recognition as sr
import os

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self, attempt_count=0):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.pause_threshold = 1.2
            self.recognizer.non_speaking_duration = 0.3
            self.recognizer.energy_threshold = 340
            audio = self.recognizer.listen(source, phrase_time_limit=6)

        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            if attempt_count >= 3:
                query = " "
                return query.lower()
            print("Couldn't understand, say that again please!")
            return self.listen(attempt_count + 1)
        except sr.RequestError as e:
            print(f"Error connecting to Google's speech recognition service; {e}")
            query = " "
            return query.lower()






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
            image_path = f'{pdf_name}_page_{i + 1}.jpg'
            if not os.path.exists(image_path):
                image = image.save()
            final_images.append(image_path)
            print(image_path)

        return final_images


    def extract_text_tesseract(self, image):
        print("Running Tesseract")
        text_tesseract = pytesseract.image_to_string(image, lang='eng')
        print(text_tesseract)
        return text_tesseract

    def extract_text_easyocr(self, image):
        print("Running EasyOCR")
        result = self.reader.readtext(image)
        text_easyocr = '\n'.join([entry[1] for entry in result])
        return text_easyocr

    def extract_text_from_handwritten_pdf(self, pdf_path):
        images = self.pdf_to_images(pdf_path)
        extracted_text = []

        for i, image in enumerate(images):
            text_tesseract = self.extract_text_tesseract(image)
            text_easyocr = self.extract_text_easyocr(image)

            extracted_text.append({
                'tesseract': text_tesseract,
                'easyocr': text_easyocr
            })

        return extracted_text

if __name__ == "__main__":
    print("________________Text Extraction__________________")
    tesseract_cmd_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pdf_extractor = HandwrittenPDFExtractor(tesseract_cmd_path)

    pdf_path = "data/sample2.pdf"
    extracted_text = pdf_extractor.extract_text_from_handwritten_pdf(pdf_path)
    print(extracted_text)

    print("________________Speech Recognition__________________")
    speech_recognizer = SpeechRecognizer()
    result = speech_recognizer.listen()
    print("Final Result:", result)
