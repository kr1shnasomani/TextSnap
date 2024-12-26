<h1 align="center">TextSnap</h1>
The project extracts text from images using PyTesseract and EasyOCR. It enhances images through grayscale conversion, denoising, thresholding and morphological operations. The extracted text is then displayed from the processed image for improved accuracy and clarity.

## Execution Guide:
1. Run the following command line in the terminal:
   ```
   pip install opencv-python pytesseract easyocr matplotlib numpy
   ```

2. Download Tesseract:
   - For Windows use the link - `https://github.com/UB-Mannheim/tesseract/releases/download/v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe`
   - For MacOS run the commands - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` and `brew install tesseract` in the terminal

3. Once the installation of Tesseract is done, open the folder > copy the path of the `tesseract.exe` file > paste it in the code.

4. Download the image > copy the path of the image > paste it in the code

5. The code will convert the image to grayscale and extract the text from that. After this is done, the grayscale image and the text extracted will be shown in the output section.

## Model Prediction:

   Image:
   ![image](https://github.com/user-attachments/assets/f5dea247-5914-4eb7-98df-70c1a54fd5b5)

   Output:
   ![image](https://github.com/user-attachments/assets/394e0419-0234-4969-83b4-0f3710f03335)

## Overview:
This project focuses on **text extraction from images** using Optical Character Recognition (OCR) techniques. It leverages two OCR libraries, **Tesseract** and **EasyOCR**, for extracting text from images, while also applying image enhancement techniques to improve the accuracy of text recognition.

1. **Libraries Used**:
   - **OpenCV**: Used for image processing tasks like converting the image to grayscale, noise reduction, and applying thresholding.
   - **PyTesseract**: An OCR engine that converts the text in the image to a string format.
   - **EasyOCR**: Another OCR tool that supports multiple languages and is initialized to recognize English text.
   - **Matplotlib**: Used for visualizing the image after enhancement.

2. **Image Enhancement**:
   - The image is first converted to **grayscale** to simplify the processing.
   - A **bilateral filter** is applied to reduce noise while preserving edges.
   - **Adaptive thresholding** is used to convert the image into a binary format, where the text is more distinguishable from the background.
   - **Morphological operations** (opening and closing) are applied to remove small noise and fill gaps, enhancing text visibility for OCR.

3. **Text Extraction**:
   - The image is enhanced using the `enhance_image()` function, which processes it step-by-step to improve text clarity.
   - **PyTesseract** is used to extract text from the processed image. The extracted text is then printed and optionally visualized using **Matplotlib**.
   - The enhanced image is also saved for debugging purposes.

4. **Output**:
   The text extracted from the image is printed to the console. This can be any text visible within the image.

5. **Why this Approach**:
   - The use of **image enhancement** techniques ensures better accuracy in text extraction, especially in images with noisy backgrounds or low contrast.
   - Using both **Tesseract** and **EasyOCR** provides redundancy, allowing the comparison of results from two different OCR engines to ensure the best possible output.

This project demonstrates how to extract text from images in a practical way by preprocessing the image and using robust OCR libraries, which can be useful in applications like document scanning, text recognition in photos, and digitizing printed text.
