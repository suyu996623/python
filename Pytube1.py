import pytube   
import os
import subprocess

v_list = [
"'https://www.youtube.com/watch?v=CZuX7381kPA&list=PLV5FrAUYlO_2uPcnumAn3ZPaf7FDFhWSs&index=277'",
]


# https://stackoverflow.com/posts/67617878/edit pytube的載點
'''
Error:Unterminated string starting at: line 1 column 39 (char 38) 这个bug令人发指，
通过输出字符串才发现，是通过命令行参数传递的串，但空格导致被识别为多个命令行参数了。
在整个参数外加双引号即可。

v_list = ["https://www.youtube.com/watch?v=uX7cTXgC96o",
]
'''
def onP(stream, chunk, bytes_remaining):
    pass

def onC(stream, file_path):
    fileobj = {}
    fileobj['name'] = os.path.basename(file_path)
    fileobj['dir'] = os.path.dirname(file_path)
    
    if stream.resolution == '720p' and stream.audio_codec != None:
        print("720P with audio download !!")
    else :
        if stream.resolution == '1080p':
            os.rename(fileobj['name'],'video1080.mp4')
        else :
            os.rename(fileobj['name'],'video.mp4')
            str1 = 'ffmpeg -i video.mp4 -c:a libmp3lame -q:a 4 music.mp3'
            subprocess.run(str1, capture_output=True)
            str1 = 'ffmpeg -i video1080.mp4 -i music.mp3 -acodec copy -vcodec copy mix01.mp4'
            subprocess.run(str1, capture_output=True)
            os.rename('mix01.mp4',fileobj['name'])
            os.remove('music.mp3')
            os.remove('video.mp4')
            os.remove('video1080.mp4')
            print("1080P mix audio compelete !!")
    
for video_url in v_list :    
    
    download_location = 'd:/suv/'
    
    yt = pytube.YouTube(video_url, on_progress_callback=onP,on_complete_callback=onC)
    video_list = yt.streams.filter(type="video").all()
    video_list_length = len(video_list)
    
    stream720_index = 0
    for v in video_list:
        if v.resolution == '720p':
            break
        stream720_index += 1
    
    if stream720_index != video_list_length :  # 有720P
        if video_list[stream720_index].audio_codec != None : # 720P有聲音
            video_list[stream720_index].download(download_location) # 下載720P with audio的檔案
            continue
        else :
            pass
    else :
        pass
        
    stream1080_index = 0
    for v in video_list:
        if v.resolution == '1080p':
            break
        stream1080_index += 1
        
    if stream1080_index != video_list_length : # 有1080P
        
        stream_audio_index = 0
        for v in video_list:
            if v.audio_codec != None:
                break
        if stream_audio_index != video_list_length : # 找到有聲音的影音檔 
            video_list[stream1080_index].download(download_location) # 下載1080P
            video_list[stream_audio_index].download(download_location) # 下載聲音
        else :
            pass
    
    else :
        pass
        
    # print(type(video_list[0].audio_codec)) # <class 'str'> mp4a.40.2
    # print(video_list[1].audio_codec) # <class 'NoneType'> None

    # print(yt.streams.filter(res="1080p").all())
    # print(yt.streams.filter(res="1080p")[0])
    # print(yt.streams.filter(res="1080p").first())

    # yt.streams.filter(res="360p").first().download(download_location)
    # yt.streams.filter(res="1080p").first().download(download_location)  # 沒有聲音
    # yt.streams.filter(abr="128kbps").first().download(download_location)  # 沒有影像

    # ffmpeg -i TAEYEON01.mp4 -i TAEYEON01.mp3 -acodec copy -vcodec copy mix01.mp4
    # ffmpeg -i video360.mp4 -c:a libmp3lame -q:a 4 music360.mp3

