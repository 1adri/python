from PIL import Image, ImageEnhance, ImageFilter
import os 


import pytesseract
from gtts import gTTS 

def preprocess_image(image_path):
    # Open the image using Pillow
    image = Image.open(image_path)

    # Convert the image to grayscale
    image = image.convert('L')

    # Apply image enhancement
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2.0)  # Adjust the enhancement factor as needed

    # Apply Gaussian blur to reduce noise
    image = image.filter(ImageFilter.GaussianBlur(radius=1))

    # Thresholding to make text more visible
    threshold_value = 150  # Adjust the threshold value as needed
    image = image.point(lambda p: p > threshold_value and 255)

    # Save the pre-processed image for inspection (optional)
    image.save('preprocessed_image.png')

    return image

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
img = "image6.jpg"
#img.load()
preprocessed_image = preprocess_image(img)

text1 = pytesseract.image_to_string(preprocessed_image, lang="ben")  #Specify language to look after!
print(text1)
'''
language = 'bn'

myobj = gTTS(text=text1, lang=language, slow=False) 

myobj.save("welcome.mp3") 
'''