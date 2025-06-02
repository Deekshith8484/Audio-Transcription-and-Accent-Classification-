---
##  Audio Transcription and Accent Classification Streamlit App

Here's a cool app for you! It's like having a personal assistant that not only transcribes what you say but also identifies your English accent—whether it's American, British (proper RP!), Australian, Indian, or even Scottish! This app is built with **Streamlit**, making it super easy to use in your web browser.

---
###  What This App Does (Features!)

* **Input Options:** You can either **upload your own audio file** (WAV or MP3 formats are supported!) or simply **paste a YouTube link**. It's straightforward!
* **Audio Processing:** The app handles downloading and converting YouTube audio, or it processes your local files, ensuring everything is converted to a crisp 16kHz mono WAV format. No need to worry about the technical details!
* **Accurate Transcription:** It uses the advanced **Whisper model** from OpenAI to accurately transcribe everything spoken in the audio.
* **Accent Identification:** With its specialized "simulated accent classifier," the app analyzes the transcribed text to identify the likely accent—be it **American, British (RP), Australian, Indian, or Scottish**. It uses lexical patterns and common linguistic traits to make its best guess.
* **User-Friendly Interface:** The Streamlit user interface is very intuitive and easy to navigate. Just provide your input, initiate the process, and view your results!

---
###  Project Structure

* `download_audio.py`: Manages downloading and converting YouTube audio.
* `preprocess_audio.py`: Handles resampling local audio files to the required 16kHz mono WAV format.
* `accent_classifier.py`: Contains the "Simulated Accent Classifier" logic for identifying accents from text.
* `main.py`: This is the core Streamlit application file, orchestrating all the audio processing, transcription, and accent classification.

---
### 🛠 What You'll Need (Requirements!)

Before you get started, ensure you have these essentials in place:

#### Python Packages:

You can install these using `pip`. It's a good idea to create a `requirements.txt` file listing these packages:

```
streamlit
yt_dlp
librosa
soundfile
numpy
transformers
```

Then, simply run `pip install -r requirements.txt`.

#### System Dependencies:

* **FFmpeg:** This is a crucial dependency for audio handling.
    * **For Ubuntu/Linux:**
        ```bash
        sudo apt-get update
        sudo apt-get install ffmpeg
        ```
    * **For macOS (using Homebrew):**
        ```bash
        brew install ffmpeg
        ```
    * **For Windows:** You'll need to either **download it from ffmpeg.org** or use Chocolatey (`choco install ffmpeg`). Crucially, remember to **add FFmpeg's `bin` directory to your system's PATH**. You can verify the installation by typing `ffmpeg -version` in your command prompt.
* **Python Version:** You'll need **Python 3.8 or newer**. You can check your version by typing `python --version` in your terminal.
* **Hardware:** A minimum of **4GB RAM** is recommended, especially for the Whisper model. More RAM will definitely improve performance!
* **Disk Space:** Ensure you have sufficient disk space for temporary audio files created during processing.

---
###  Getting Started (Installation!)

Follow these straightforward steps to get the app running:

1.  Confirm that Python 3.8+ and FFmpeg are installed and properly configured in your system's PATH.
2.  **Clone or download this project** to your computer. Then, navigate to the project's directory in your terminal.
3.  Install all the required Python packages as mentioned above:
    ```bash
    pip install streamlit yt_dlp librosa soundfile numpy transformers
    ```
4.  Ensure all the primary files (`download_audio.py`, `preprocess_audio.py`, `accent_classifier.py`, and `main.py`) are located in the **same directory**.

---
###  How to Run the Application!

Running this app is very simple:

1.  In your project directory, execute this command in your terminal:
    ```bash
    streamlit run main.py
    ```
2.  A new browser window will automatically open, displaying the Streamlit interface for the app.
3.  Choose your preferred input method: you can either **upload a WAV or MP3 file** directly, or **paste a YouTube URL**.
4.  Click the "**Process Audio**" button. The app will then handle the audio processing, transcription, and accent classification.
5.  Finally, you'll see the **transcribed text** and the **classified accent** (along with confidence scores!) displayed on the screen. A summary of the accent analysis will also be provided. In some cases, if specific keywords aren't detected, it might show a probability distribution across different accents.

---
###  Important Notes!

* Temporary files are created during the processing, but the app automatically deletes them once done.
* The Whisper model might take some time to load, especially during the first run or with larger audio files. Please be patient.
* Ensure you have a stable internet connection, particularly for YouTube downloads and model initialization.
* If you encounter any errors, check the Streamlit interface for error messages, and verify your FFmpeg installation.

---
###  Troubleshooting!

Facing a small issue? Don't worry, here are some common solutions:

* **FFmpeg not found:** Double-check that FFmpeg is installed and its path is correctly added to your system's environment variables. Run `ffmpeg -version` to confirm.
* **Module not found:** Ensure all necessary Python packages are installed. You can verify this by running `pip list`.
* **Large audio files:** Processing can be slow for large files; consider using shorter audio clips or running the app on a more powerful machine.
* **YouTube download issues:** Confirm that the YouTube URL is valid and accessible. For more advanced options or troubleshooting, refer to the `yt_dlp` documentation.

---
###  License

This project is intended for educational purposes and utilizes open-source libraries under their respective licenses. Please ensure compliance with YouTube's terms of service when downloading audio.

---
