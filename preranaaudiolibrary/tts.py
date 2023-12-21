from gtts import gTTS 
from webscraping import copied_text
language = 'bn'

myobj = gTTS(text=copied_text, lang=language, slow=False) 

myobj.save("welcome.mp3") 