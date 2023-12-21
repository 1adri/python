from PIL import Image
import os 


import pytesseract
from gtts import gTTS 
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
img = Image.open("image3.png")
img.load()
text1 = pytesseract.image_to_string(img, lang="eng")  #Specify language to look after!
print(text1)

language = 'en'

myobj = gTTS(text=text1, lang=language, slow=False) 

myobj.save("welcome.mp3") 
