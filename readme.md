# YouTube Video Transcription Service

This Python application is a Flask web service that takes a YouTube video URL as input and returns a transcript of the audio using OpenAI's Whisper ASR API. It first downloads the audio from the YouTube video, splits it into 10-minute chunks, and then transcribes each chunk using the Whisper ASR API.

## Dependencies

To use this application, make sure you have the following dependencies installed:

- `openai`: The official OpenAI Python library.
- `pytube`: A lightweight, dependency-free Python library for downloading YouTube videos.
- `pydub`: A simple audio processing library for Python.
- `Flask`: A lightweight WSGI web application framework.

You can install these dependencies using pip:

\```bash
pip install openai pytube pydub flask
\```

## Usage

1. Set up an OpenAI API key:

\```bash
export OPEN_AI_KEY=your_openai_api_key_here
\```

2. Run the Flask application:

\```bash
python app.py
\```

3. Make a request to the `/transcribe` endpoint with the YouTube video URL as a parameter:

\```bash
curl "http://localhost:5000/transcribe?url=https://www.youtube.com/watch?v=example"
\```

4. The application will download the audio from the YouTube video, split it into chunks, transcribe each chunk using the Whisper ASR API, and return the transcript as a JSON object:

\```json
{
"transcript": "your_transcription_here"
}
\```

## Notes

- This application is for demonstration purposes only and is not suitable for use in production.
- The transcription accuracy depends on the quality of the audio and the performance of the Whisper ASR API.
- Keep in mind that long videos may take a significant amount of time to transcribe.
- Make sure you have the necessary permissions to download and transcribe the audio from the YouTube video.
