from pydub import AudioSegment
import speech_recognition as sr

# 定义音频文件路径和目标WAV文件路径
input_audio_file = "output.mp3"
output_wav_file = "output.wav"

# 将音频文件转换为 WAV 格式
audio = AudioSegment.from_mp3(input_audio_file)
audio.export(output_wav_file, format="wav")

# 创建一个识别器对象
recognizer = sr.Recognizer()

# 读取转换后的 WAV 音频文件
with sr.AudioFile(output_wav_file) as source:
    audio_data = recognizer.record(source)

# 进行语音识别
try:
    text = recognizer.recognize_google(audio_data, language="en-US")
    print("Transcribed Text: ", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

