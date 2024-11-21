import os
from typing import Optional
import whisper
from elevenlabs import generate, save, set_api_key
from google.cloud import texttospeech

class VoiceUtils:
    def __init__(self, elevenlabs_api_key: Optional[str] = None, google_credentials_path: Optional[str] = None):
        """Initialize voice utilities with optional API keys"""
        if elevenlabs_api_key:
            set_api_key(elevenlabs_api_key)
        if google_credentials_path:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_credentials_path
        
        self.whisper_model = whisper.load_model("base")
        self.google_client = texttospeech.TextToSpeechClient()

    def transcribe_audio(self, audio_file_path: str) -> str:
        """Transcribe audio file using Whisper"""
        try:
            result = self.whisper_model.transcribe(audio_file_path)
            return result["text"]
        except Exception as e:
            print(f"Error transcribing audio: {str(e)}")
            return ""

    def generate_elevenlabs_speech(self, text: str, voice_id: str, output_path: str) -> bool:
        """Generate speech using ElevenLabs"""
        try:
            audio = generate(text=text, voice=voice_id)
            save(audio, output_path)
            return True
        except Exception as e:
            print(f"Error generating ElevenLabs speech: {str(e)}")
            return False

    def generate_google_speech(self, text: str, language_code: str, output_path: str) -> bool:
        """Generate speech using Google Text-to-Speech"""
        try:
            synthesis_input = texttospeech.SynthesisInput(text=text)
            voice = texttospeech.VoiceSelectionParams(
                language_code=language_code,
                ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )

            response = self.google_client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config
            )

            with open(output_path, "wb") as out:
                out.write(response.audio_content)
            return True
        except Exception as e:
            print(f"Error generating Google speech: {str(e)}")
            return False
