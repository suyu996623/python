import speech_recognition as sr
r = sr.Recognizer()
WAV = sr.AudioFile('test.wav')
with WAV as source:
    audio = r.record(source)
    print(r.recognize_google(audio, language = "zh-tw"))


# from pydub import AudioSegment
# # convert wav to mp3
# sound = AudioSegment.from_mp3("AI.mp3")
# sound.export("test.wav", format="wav")
# ffmpeg 要放在 c:\

