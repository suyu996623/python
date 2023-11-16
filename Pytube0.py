import pytube   

video_url = r"https://www.youtube.com/live/_oYkzzGTj9Q?si=uVvsnGB16ruJ2e5T"
yt = pytube.YouTube(video_url)
video_list = yt.streams
#video_list_length = len(video_list)
print(video_list)

# yt.streams.filter(res="720p").first().download(download_location)

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
