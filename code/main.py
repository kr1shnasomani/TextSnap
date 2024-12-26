# Import the required libraries
import cv2
import pytesseract
import easyocr
import numpy as np
import matplotlib.pyplot as plt

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\krish\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Initialize the EasyOCR reader with English as the language
reader = easyocr.Reader(['en'])

# Image processing and text extracting
def enhance_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    denoised = cv2.bilateralFilter(gray, 5, 75, 75)
    
    thresh = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    kernel = np.ones((3,3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=1)
    
    return closing

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    
    enhanced_image = enhance_image(image)

    extracted_text = pytesseract.image_to_string(enhanced_image)
    
    return extracted_text

if __name__ == "__main__":
    image_path = r"C:\Users\krish\OneDrive\Desktop\Projects\TextSnap - Text Extractor\dataset\image.png"
    extracted_text = extract_text_from_image(image_path)

    print(extracted_text)