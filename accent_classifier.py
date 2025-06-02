import numpy as np

class SimulatedAccentClassifier:
    """A class to simulate accent classification based on transcribed text."""
    def __init__(self):
        # Define the list of possible accents to classify
        self.accents = ["American", "British (RP)", "Australian", "Indian", "Scottish"]
        # Default probability distribution for accents (used when no specific keywords are found)
        self.default_accent_distribution = {
            "American": 0.2, "British (RP)": 0.2, "Australian": 0.2, "Indian": 0.3, "Scottish": 0.1
        }

    def classify_accent(self, audio_filepath: str, transcribed_text: str):
        """Simulates accent classification based on lexical patterns in the transcribed text.

        Args:
            audio_filepath (str): Path to the audio file (not used in this simulation).
            transcribed_text (str): The transcribed text from the audio.

        Returns:
            dict: A dictionary containing the classified accent, confidence scores, summary, and probabilities.
        """
        print("Simulating accent classification with focus on Indian accent...")
        # Convert transcribed text to lowercase for consistent keyword matching
        transcribed_text = transcribed_text.lower()

        # Check for specific keywords to determine the dominant accent
        if any(word in transcribed_text for word in ["lakh", "crore", "bhai", "didi", "ji"]):
            dominant_accent = "Indian"
            confidence_in_dominant = 0.90
        elif "color" in transcribed_text or "flavor" in transcribed_text:
            dominant_accent = "American"
            confidence_in_dominant = 0.85
        elif "colour" in transcribed_text or "flavour" in transcribed_text:
            dominant_accent = "British (RP)"
            confidence_in_dominant = 0.85
        elif "mate" in transcribed_text or "g'day" in transcribed_text:
            dominant_accent = "Australian"
            confidence_in_dominant = 0.80
        elif "aye" in transcribed_text or "loch" in transcribed_text:
            dominant_accent = "Scottish"
            confidence_in_dominant = 0.80
        else:
            # If no specific keywords are found, use a random distribution based on default probabilities
            probabilities = np.random.dirichlet(
                [self.default_accent_distribution[accent] * 10 for accent in self.accents]
            )
            dominant_accent_index = np.argmax(probabilities)
            dominant_accent = self.accents[dominant_accent_index]
            confidence_in_dominant = probabilities[dominant_accent_index]

        # Generate a random confidence score for overall English accent detection
        english_accent_confidence = np.random.uniform(90, 99)
        # Create a summary of the classification results
        summary = (
            f"The audio primarily exhibits characteristics of a '{dominant_accent}' accent. "
            f"This is based on a simulated analysis of lexical patterns, with a focus on detecting Indian English."
        )

        # Return a dictionary with classification results
        return {
            "accent_type": dominant_accent,
            "accent_confidence_score": round(confidence_in_dominant * 100, 2),
            "english_accent_confidence": round(english_accent_confidence, 2),
            "summary": summary,
            # Include probabilities only if they were generated (i.e., no specific keywords found)
            "probabilities": {self.accents[i]: round(prob * 100, 2) for i, prob in enumerate(probabilities)} if 'probabilities' in locals() else {}
        }