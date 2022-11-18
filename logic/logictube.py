from __future__ import unicode_literals
import youtube_dl
import ffmpeg

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'output.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
}
def lunk(pew):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = pew
#        url=input("Вставте ссылку на ютуб видео ")
        ydl.download([url])
        stream = ffmpeg.input('output.m4a')
        stream = ffmpeg.output(stream, 'output.wav')
        
        

