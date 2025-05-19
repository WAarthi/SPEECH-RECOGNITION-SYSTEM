import speech_recognition as sr
import os
from pydub import AudioSegment
import tempfile

def transcribe_audio(audio_file_path):
    """
    Transcribes an audio file into text using the Google Speech Recognition API.
    Handles both WAV and MP3 files.  MP3 files are converted to WAV using pydub.

    Args:
        audio_file_path (str): The path to the audio file.

    Returns:
        str: The transcribed text, or None if an error occurs.
    """
    # Check if the file path is valid
    if not isinstance(audio_file_path, str):
        print("Error: audio_file_path must be a string.")
        return None

    # Create a recognizer object
    r = sr.Recognizer()

    # Get the absolute path of the audio file
    audio_file_path = os.path.abspath(audio_file_path)

    # Check the file extension
    if audio_file_path.lower().endswith(".mp3"):
        # Convert MP3 to WAV using pydub
        try:
            audio = AudioSegment.from_mp3(audio_file_path)
            # Create a temporary WAV file
            temp_wav_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=True)
            audio.export(temp_wav_file.name, format="wav")
            audio_file_path = temp_wav_file.name  # Update path to the WAV file
        except Exception as e:
            print(f"Error converting MP3 to WAV: {e}")
            return None

    # Open the audio file using a context manager
    try:
        with sr.AudioFile(audio_file_path) as source:
            # Read the audio data from the file
            audio_data = r.record(source)
    except FileNotFoundError:
        print(f"Error: File not found at {audio_file_path}")
        return None
    except Exception as e:
        print(f"Error reading audio file: {e}")
        return None

    # Use the Google Speech Recognition API to transcribe the audio
    try:
        text = r.recognize_google(audio_data)
        if audio_file_path.endswith(".wav") and "temp_wav_file" in locals():
             temp_wav_file.close() #explicitly close
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during transcription: {e}")
        return None



def main():
    """
    Main function to run the speech-to-text system.
    Prompts the user for an audio file path, transcribes it, and prints the output.
    """
    print("Speech-to-Text System")
    print("---------------------")

    # Get the audio file path from the user
    audio_file_path = input("Enter the path to the audio file (WAV or MP3): ")

    # Transcribe the audio file
    transcribed_text = transcribe_audio(audio_file_path)

    # Print the transcribed text
    if transcribed_text:
        print("\nTranscribed Text:")
        print(transcribed_text)
    else:
        print("\nTranscription failed.")

if __name__ == "__main__":
    main()
