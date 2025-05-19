# SPEECH-RECOGNITION-SYSTEM

This project converts audio files (WAV or MP3) into text using the Google Speech Recognition API. It handles both WAV and MP3 files, converting MP3 to WAV using the `pydub` library.

## Overview

The script `speech_to_text.py` takes an audio file path as input and outputs the transcribed text. It uses the `speech_recognition` library to interact with the Google Speech Recognition API.

## Setup

1.  **Prerequisites:**
    * Python 3.6 or higher
    * pip

2.  **Installation:**
    * Clone this repository (if applicable) or save the code as `speech_to_text.py`.

3.  **Install Dependencies:**
    * You need to install the following Python libraries. Open your terminal or command prompt and run:

        ```bash
        pip install SpeechRecognition pydub
        ```

    * `SpeechRecognition`: For accessing the Google Speech Recognition API.
    * `pydub`: For handling MP3 to WAV conversion.

## Important Notes

* **Internet Connection:** This script requires an active internet connection to communicate with the Google Speech Recognition API.
* **API Key (Optional):** The Google Speech Recognition API can be used without an API key for basic usage. However, Google may impose usage limits. For production or high-volume usage, consider obtaining a Google Cloud Speech-to-Text API key and configuring `speech_recognition` to use it.  See the `speech_recognition` documentation for details.

## How to Use

1.  Save the Python code as `speech_to_text.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script:

    ```bash
    python speech_to_text.py
    ```

5.  The script will prompt you to enter the path to the audio file you want to transcribe. Enter the full path to your WAV or MP3 file.
6.  The script will then attempt to transcribe the audio and print the resulting text. If the transcription is unsuccessful, it will print an error message.

## Code Description

* `speech_to_text.py`: Contains the Python script with the following functions:
    * `transcribe_audio(audio_file_path)`:
        * Takes the path to an audio file (WAV or MP3) as input.
        * Converts MP3 files to WAV using `pydub`.
        * Reads the audio data using `speech_recognition`.
        * Transcribes the audio using the Google Speech Recognition API.
        * Handles potential errors, including:
            * Invalid file path (not a string).
            * File not found.
            * Errors reading the audio file.
            * Errors during communication with the Google Speech Recognition API.
            * Google Speech Recognition could not understand the audio.
        * Returns the transcribed text, or `None` if an error occurs.
    * `main()`:
        * The main function of the script.
        * Prompts the user to enter the audio file path.
        * Calls `transcribe_audio()` to transcribe the audio.
        * Prints the transcribed text or an error message.

## Example Output

Here's an example of the interaction:


Speech-to-Text System
Enter the path to the audio file (WAV or MP3): /path/to/your/audiofile.wav
[... (Transcription process) ...]
Transcribed Text:
This is the transcribed text from your audio file. The Google Speech Recognition API has converted the spoken words into written text.


If there's an error, you might see:


Speech-to-Text System
Enter the path to the audio file (WAV or MP3): /path/to/nonexistent_file.wav
Error: File not found at /path/to/nonexistent_file.wav
Transcription failed.

