import whisper

model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio(r"C:\Users\Jackb\OneDrive\Documents\Voice recording test files\Lords prayer.mp3")

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions(language= 'en', fp16=False) 
result = whisper.decode(model, mel, options) 
print(result.text)


# print the recognized text
print(result.text)