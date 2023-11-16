import pytube   
import os
import subprocess

v_list = [
"'https://www.youtube.com/watch?v=rJNBGqiBI7s'",
]


def onP(stream, chunk, bytes_remaining):
    pass

def onC(stream, file_path):
    fileobj = {}
    fileobj['name'] = os.path.basename(file_path)
    fileobj['dir'] = os.path.dirname(file_path)
    
    if stream.resolution == '2160p':
        os.rename(fileobj['name'],'video2160.mp4')
    if stream.abr == "128kbps" :
        os.rename(fileobj['name'],'video.mp4')
        str1 = 'ffmpeg -i video.mp4 -c:a libmp3lame -q:a 4 music.mp3'
        subprocess.run(str1, capture_output=True) # capture_output 设为 true，stdout 和 stderr 将会被捕获。
        str1 = 'ffmpeg -i video2160.mp4 -i music.mp3 -acodec copy -vcodec copy mix01.mp4'
        subprocess.run(str1, capture_output=True)
        os.rename('mix01.mp4',fileobj['name'])
        os.remove('music.mp3')
        os.remove('video.mp4')
        os.remove('video2160.mp4')
        print("2160P mix audio compelete !!")
    
for video_url in v_list :    
    
    download_location = 'd:/suv/'
    yt = pytube.YouTube(video_url, on_progress_callback=onP,on_complete_callback=onC)
    yt.streams.filter(res="2160p").first().download(download_location)
    print('1')
    yt.streams.filter(abr="128kbps").first().download(download_location)

        