from pytubefix import YouTube
import moviepy.editor as mp
import whisper
import os
import re
import ffmpeg

"""
# Baixa o áudio do arquivo
import sys
url = input('Digite o link do video: ')
path = "D:\GitHub_Repository\Programas-em-Python\Projetos-Extras\Analisador_Youtube"
filename = "audio.wav"
yt = YouTube(url)
stream = yt.streams.filter(only_audio=True).first().download(path)
#Converter o video(mp4) para mp3
for file in os.listdir(path):                  #For para percorrer dentro da pasta passada anteriormente
    if re.search('mp4', file):                 #If verificando se o arquivo e .MP4                    
        mp4_path = os.path.join(path , file)   #Cria uma variavel para armazenar o arquivo .MP4
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3') #Variavel que cria o nome do arquivo e adiciona .MP3 ao final
        new_file = mp.AudioFileClip(mp4_path)  #Cria o arquivo de áudio (.MP3)
        new_file.write_audiofile(mp3_path)     #Renomeia o arquivo, setando o nome criado anteriormente
        os.remove(mp4_path)                    #Remove o arquivo .MP4
print("Download Completo")
"""
# Transcrição dos vídeos
model = whisper.load_model("base")
result = model.transcribe("Meme Quero cafe.mp3")

#Salva como TXT com quebra de linhas
with open("transcription.txt", "w") as f:
    f.write(result["text"])