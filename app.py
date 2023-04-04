import os
import openai
from pytube import YouTube
from pydub import AudioSegment
from flask import Flask, request, jsonify

app = Flask(__name__)
openai.api_key = os.environ['OPEN_AI_KEY']

def transcribe_audio_chunks(chunks):
    transcript_text = ""
    for idx, chunk in enumerate(chunks):
        chunk.export("temp_chunk.mp3", format="mp3")
        with open("temp_chunk.mp3", "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
        transcript_text += transcript["text"]
        print(f"Chunk {idx + 1} of {len(chunks)} transcribed.")
    os.remove("temp_chunk.mp3")
    return transcript_text

@app.get('/')
def index():
    return "API working"

@app.route('/transcribe', methods=['GET'])
def transcribe_youtube_video():
    url = request.args.get('url')

    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()

    output_path = "Youtubeaudios"
    filename = "audio.mp3"
    print("Downloading...")
    audio_stream.download(output_path=output_path, filename=filename)

    print(f"Audio downloaded to {output_path}/{filename}")
    audio = AudioSegment.from_file(os.path.join(output_path, filename))

    chunk_duration = 10 * 60 * 1000
    num_chunks = len(audio) // chunk_duration + (1 if len(audio) % chunk_duration != 0 else 0)
    audio_chunks = [audio[i * chunk_duration:(i + 1) * chunk_duration] for i in range(num_chunks)]

    print(f"Number of chunks: {len(audio_chunks)}")
    print("Start the transcription - Chunk 1")
    transcript_text = transcribe_audio_chunks(audio_chunks)

    return jsonify({'transcript': transcript_text})

if __name__ == '__main__':
    app.run()
