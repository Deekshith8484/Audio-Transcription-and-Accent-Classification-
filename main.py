import streamlit as st
import os
import tempfile
from transformers import pipeline
from download_audio import download_youtube_audio_wav
from preprocess_audio import preprocess_audio
from accent_classifier import SimulatedAccentClassifier

def main():
    st.title("Audio Transcription and Accent Classification")
    st.write("Upload an audio file (WAV/MP3) or provide a YouTube URL to transcribe and classify the accent.")

    # Input options
    input_option = st.radio("Choose input method:", ("Upload Audio File", "Enter YouTube URL"))
    processed_audio_path = os.path.join(tempfile.gettempdir(), "processed_audio.wav")

    if input_option == "Upload Audio File":
        uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])
        if uploaded_file is not None:
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(uploaded_file.read())
                tmp_audio_path = tmp.name
            if st.button("Process Audio"):
                with st.spinner("Processing audio..."):
                    if preprocess_audio(tmp_audio_path, processed_audio_path):
                        st.session_state['ready'] = True
                        st.session_state['audio_path'] = processed_audio_path
                    else:
                        st.session_state['ready'] = False
                    os.remove(tmp_audio_path)  # Clean up temporary file
    else:
        youtube_url = st.text_input("Enter YouTube URL:")
        if youtube_url and st.button("Process Audio"):
            with st.spinner("Downloading and processing audio..."):
                if youtube_url.startswith("http"):
                    if download_youtube_audio_wav(youtube_url, processed_audio_path):
                        st.session_state['ready'] = True
                        st.session_state['audio_path'] = processed_audio_path
                    else:
                        st.session_state['ready'] = False
                else:
                    st.error("Invalid YouTube URL.")
                    st.session_state['ready'] = False

    # Process transcription and accent classification
    if 'ready' in st.session_state and st.session_state['ready']:
        with st.spinner("Loading Whisper model..."):
            try:
                pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base", return_timestamps=True)
                st.write("Whisper model loaded.")
                st.write(f"Transcribing audio from {st.session_state['audio_path']}...")
                result = pipe(st.session_state['audio_path'])
                transcribed_text = result['text']
                st.subheader("Transcription")
                st.write(transcribed_text)

                # Accent classification
                accent_classifier = SimulatedAccentClassifier()
                accent_results = accent_classifier.classify_accent(st.session_state['audio_path'], transcribed_text)
                st.subheader("Accent Analysis Results")
                st.write(f"**Classified Accent:** {accent_results['accent_type']}")
                st.write(f"**Confidence in Classified Accent:** {accent_results['accent_confidence_score']:.2f}%")
                st.write(f"**Overall English Accent Confidence:** {accent_results['english_accent_confidence']:.2f}%")
                st.write(f"**Summary:** {accent_results['summary']}")
                if accent_results['probabilities']:
                    st.write("**Accent Probabilities:**")
                    for accent, prob in accent_results['probabilities'].items():
                        st.write(f"- {accent}: {prob:.2f}%")

                # Clean up processed audio file
                if os.path.exists(processed_audio_path):
                    os.remove(processed_audio_path)
            except Exception as e:
                st.error(f"Error during transcription or accent analysis: {e}")
    elif 'ready' in st.session_state and not st.session_state['ready']:
        st.error("Failed to process audio. Please try again.")

if __name__ == "__main__":
    main()