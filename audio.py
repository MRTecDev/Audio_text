from gtts import gTTS
import os

# Texto que você deseja transformar em fala
texto = "Olá, apenas testando se vai dar certo."

# Cria um objeto gTTS
tts = gTTS(text=texto, lang='pt-br')  

# Salva o arquivo de áudio
tts.save("output.mp3")

# Reproduz o arquivo de áudio
os.system("mpg321 output.mp3")  
