import yt_dlp
import os
import uuid
import time

def download_youtube_audio_wav(url, save_path="processed_audio.wav"):
    """Downloads audio from a YouTube URL and converts it to 16kHz mono WAV format.

    Args:
        url (str): The YouTube URL to download audio from.
        save_path (str): The path where the processed audio file will be saved.

    Returns:
        bool: True if the download and conversion are successful, False otherwise.
    """
    print(f"Attempting to download audio from {url}...")
    temp_id = uuid.uuid4().hex  # Unique ID to avoid filename conflicts
    temp_filename = f"temp_audio_{temp_id}"

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{temp_filename}.%(ext)s',
            'quiet': True,
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                    'preferredquality': '192',
                }
            ],
            'postprocessor_args': ['-ar', '16000', '-ac', '1']
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        expected_output = f"{temp_filename}.wav"

        # Wait briefly to ensure file is fully written/unlocked
        time.sleep(0.5)

        if os.path.exists(expected_output):
            os.rename(expected_output, save_path)
            print(f"Audio downloaded and saved as {save_path}")
            return True
        else:
            raise FileNotFoundError("Expected WAV file not found.")

    except Exception as e:
        print(f"Error downloading audio: {e}")
        return False

    finally:
        # Cleanup leftover .part files if any
        for f in os.listdir():
            if f.startswith(temp_filename) and f.endswith(".part"):
                try:
                    os.remove(f)
                except Exception:
                    pass
