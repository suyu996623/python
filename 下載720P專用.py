import pytube

v_list = [
"'https://www.youtube.com/live/1edmw_tYboI?si=0VIbltZ2ovuvpKDX'",
"'https://www.youtube.com/live/j2gcFtRMMgA?si=iZTDhSD51khSCqyj'",
"'https://www.youtube.com/live/4P_rLNLarCg?si=u9EgelVkgLCbI-py'",
"'https://www.youtube.com/live/M5qt69HRzJg?si=5xaFmHDij1tg8MPY'",
"'https://www.youtube.com/live/kHl5K0A1Z78?si=-PvgJiX5rPuFjnoz'",
"'https://www.youtube.com/live/pbbo6ZSyUdM?si=pcOJ2MdoMKls5h5l'",
"'https://www.youtube.com/live/vwEABweY8Pc?si=7Aew5QxrQ3AYlxA3'",
"'https://www.youtube.com/live/6tkRSwvM9mw?si=ucS5fWSOv-eSImRf'",
"'https://www.youtube.com/live/DhZ6m_uiQEo?si=KGUflUUAZemYxE7K'",
"'https://www.youtube.com/live/8nXG4vBtvgQ?si=Kp7f45A-89F_49GG'",
"'https://www.youtube.com/live/Z6rxM6kbcVA?si=kALgArtf8lmZ9OXn'",
]

download_location = r'C:\Users\suyu\Desktop\suv'
for video_url in v_list :
    yt = pytube.YouTube(video_url)  # yt 物件
    print('開始下載')
    print(type(yt.streams.filter(res="720p")))
    stream = yt.streams.filter(res="720p").first()
    print(stream)
    stream.download(download_location)
    print('下載完成!!')

# <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">