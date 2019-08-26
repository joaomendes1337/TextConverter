from gtts import gTTS
import os
## PRECISA SER INSTALADO O gTTS ( PIP INSTALL gTTS)

list_files_directory = os.listdir()
i=0
while i < list_files_directory.__len__():
    print( str(i)+ " - " + str(list_files_directory[i]))
    i+=1
op = int(input("Digite qual ficheiro usar: "))

name_file = list_files_directory[op]

try:
    file = open(name_file, "r", encoding="utf-8")
    file_text = file.readlines()
except:
    print("Could not parse the file.")
file_text = [i for i in file_text if i is not "\n"]
file_text = " ".join(file_text)

tts = gTTS(text=file_text, lang='en')
tts.save("sv1.mp3")
print("Done")
