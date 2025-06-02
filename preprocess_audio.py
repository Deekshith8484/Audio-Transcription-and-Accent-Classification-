import librosa
import soundfile as sf

def preprocess_audio(audio_path, output_path="processed_audio.wav"):
    """Resamples an input audio file to 16kHz mono WAV format.

    Args:
        audio_path (str): Path to the input audio file (WAV or MP3).
        output_path (str): Path where the processed audio file will be saved (default: 'processed_audio.wav').

    Returns:
        bool: True if preprocessing is successful, False otherwise.
    """
    print(f"Preprocessing audio from {audio_path}...")
    try:
        # Load the audio file with librosa, resampling to 16kHz and converting to mono
        y, sr = librosa.load(audio_path, sr=16000, mono=True)
        # Save the processed audio as a WAV file using soundfile
        sf.write(output_path, y, 16000)
        print(f"Audio resampled and saved as {output_path}")
        return True
    except Exception as e:
        # Handle any errors during audio preprocessing
        print(f"Error preprocessing audio: {e}")
        return False