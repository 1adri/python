from PIL import Image

import requests

import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
img = Image.open("image3.png")
img.load()
text = pytesseract.image_to_string(img, lang="eng")  #Specify language to look after!
print(text)
text = text.replace(" ", "%20")
base = 'https://translate.google.com/translate_tts?ie=UTF-&&client=tw-ob&tl=en&q='

base += text

print(f'\n{base}')
def download_audio(url, destination_path):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(destination_path, 'wb') as audio_file:
            audio_file.write(response.content)
        print(f"Audio downloaded successfully to {destination_path}")
    else:
        print(f"Failed to download audio. Status code: {response.status_code}")

# Example usage
audio_url = "https://example.com/path/to/your/audiofile.mp3"
download_destination = "audiofile.mp3"

download_audio(base, download_destination)

'''
i = 'Сред. Скорость'
print(i)
if (text == i):
    print("Match")
else :
    print("Not Match")
# Simple image to string
print(pytesseract.image_to_string(Image.open('image.jpg')))
'''