# Blog Project: Text to Speech and Speech to Text

This project demonstrates a simple web application that performs Text to Speech (TTS) and Speech to Text (STT) conversions using a Flask backend and a JavaScript frontend.

## Features

- **Text to Speech**: Converts text input into speech.
- **Speech to Text**: Records audio from the user's microphone, sends it to the backend, and converts it into text.

## Requirements

- Python 3.6+
- Flask
- SpeechRecognition
- pydub
- gtts
- Web browser with JavaScript enabled

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/rohith-sreedharan/blog-project.git
    cd blog-project
    ```

2. **Set up a virtual environment (optional but recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**

    ```bash
    pip install Flask SpeechRecognition pydub gtts
    ```

## Usage

1. **Run the Flask application**

    ```bash
    python app.py
    ```

2. **Open `index.html` in a web browser**

    ```bash
    open index.html  # or just double-click the file
    ```

3. **Text to Speech**
    - Enter text into the textarea.
    - Click the "Text to Speech" button.
    - The text will be converted to speech and played back.

4. **Speech to Text**
    - Click the "Speech to Text" button to start recording.
    - Click the button again to stop recording.
    - The recorded speech will be sent to the backend, transcribed to text, and displayed on the page.

## Project Structure

- `app.py`: Flask backend to handle TTS and STT requests.
- `index.html`: Frontend HTML with JavaScript to interact with the backend.

## Backend Endpoints

- `POST /text_to_speech`: Converts provided text to speech and returns the audio file.
- `POST /transcribe`: Accepts an audio file, converts it to text, and returns the transcription.

## Example Request and Response

### Text to Speech

- **Request**:

    ```json
    POST /text_to_speech
    Content-Type: application/json

    {
        "text": "Hello, world!"
    }
    ```

- **Response**: An audio file containing the spoken text.

### Speech to Text

- **Request**: An audio file uploaded as form data.

- **Response**:

    ```json
    {
        "transcription": "Hello, world!"
    }
    ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pydub](https://pydub.com/)
- [gTTS](https://pypi.org/project/gTTS/)

## Contact

For any inquiries, please contact [rohith@springreen.in ](mailto:rohith@springreen.in).
