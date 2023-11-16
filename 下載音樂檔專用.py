import pytube   
import os
import subprocess

v_list = [
"'https://youtu.be/EM9fA0uJn6w?si=K0anX1ze3Zx8dPD_'",
]

def onP(stream, chunk, bytes_remaining):
    pass

def onC(stream, file_path):
    pass
    fileobj = {}
    fileobj['name'] = os.path.basename(file_path).split('.')[0]+'.mp3'
    os.rename(os.path.basename(file_path),'video.mp4')
    str1 = 'ffmpeg -i video.mp4 -c:a libmp3lame -q:a 4 music.mp3'
    subprocess.run(str1, capture_output=True) # capture_output 设为 true，stdout 和 stderr 将会被捕获。
    os.rename('music.mp3',fileobj['name'])
    os.remove('video.mp4')
    print("mp3 download compelete !!")
    
download_location = r'C:\Users\suyu\Desktop\suv'
for video_url in v_list :    
    yt = pytube.YouTube(video_url, on_progress_callback=onP,on_complete_callback=onC)
    yt.streams.filter(abr="128kbps").first().download(download_location)

        