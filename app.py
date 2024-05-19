from flask import Flask, request, jsonify, send_file
from gtts import gTTS
import speech_recognition as sr
from pydub import AudioSegment
import io

app = Flask(__name__)

@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    tts = gTTS(text=text, lang='en')
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)

    return send_file(audio_buffer, mimetype='audio/mpeg')

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    audio = AudioSegment.from_file(io.BytesIO(audio_file.read()), format='wav')

    recognizer = sr.Recognizer()
    audio_data = sr.AudioData(audio.raw_data, audio.frame_rate, audio.sample_width)

    try:
        text = recognizer.recognize_google(audio_data)
        return jsonify({'transcription': text})
    except sr.UnknownValueError:
        return jsonify({'error': 'Could not understand audio'}), 400
    except sr.RequestError:
        return jsonify({'error': 'Could not request results from Google Speech Recognition service'}), 500

if __name__ == '__main__':
    app.run(debug=True)