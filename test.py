from gtts import gTTS
import os
import json

# 打开并读取JSON文件
with open('package.json', 'r') as file:
    data = json.load(file)
    text = data['text']  # 假设JSON文件中包含一个"text"键

# 将文本转换为语音
tts = gTTS(text=text, lang='en')

# 保存语音文件
tts.save("output.mp3")

# 播放语音文件
os.system("start output.mp3")  # 对于Windows用户
# 对于Mac用户，可以使用 os.system("afplay output.mp3")
# 对于Linux用户，可以使用 os.system("mpg321 output.mp3")
