# Image to Text using Python

import pytesseract
from PIL import Image

# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Open image
img = Image.open("image-and-text/www.png")

# Extract text
txt = pytesseract.image_to_string(img)

# Print extracted text
print("Extracted Text:")
print(txt)