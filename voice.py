from gtts import gTTS

def text_to_speech(text: str, filename="response.mp3"):
    try:
        tts = gTTS(text=text, lang="en")
        tts.save(filename)
        return filename
    except Exception as e:
        return None