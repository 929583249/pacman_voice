from flask import Flask, request, jsonify
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get('text')
    lang = data.get('lang', 'en')  # 默认语言设置为英语
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # 将文本转换为语音
    tts = gTTS(text=text, lang=lang)
    # 生成一个唯一的文件名
    filename = f"{uuid.uuid4().hex}.mp3"
    tts.save(filename)
    
    return jsonify({'message': 'Speech synthesis completed successfully', 'file': filename})

if __name__ == '__main__':
    app.run(debug=True)
