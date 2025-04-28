import scipy
from transformers import AutoProcessor, BarkModel
import os

processor = AutoProcessor.from_pretrained("./local-bark-model", local_files_only=True)
model = BarkModel.from_pretrained("./local-bark-model", local_files_only=True)

supported_languages = ["en", "fr", "de", "es", "it", "ja", "zh", "pt", "pl", "ru", "ko", "tr", "hi"]

prompt = os.environ.get("PROMPT", os.environ.get("DEFAULT_PROMPT", "Hello there nice to meet you!"))
voice = os.environ.get("VOICE", os.environ.get("DEFAULT_VOICE", "john"))
language = os.environ.get("LANGUAGE", os.environ.get("DEFAULT_LANGUAGE", "en"))

# If the language is not supported, use English
if language not in supported_languages:
    language = "en"

if voice == "john":
    voice_preset = f"v2/{language}_speaker_6"
elif voice == "jane":
    voice_preset = f"v2/{language}_speaker_9"
else:
    # If the voice is not supported, use John
    voice_preset = "v2/en_speaker_6"

inputs = processor(
    text=[prompt],
    voice_preset=voice_preset,
    return_tensors="pt",
)

audio_array = model.generate(**inputs)
audio_array = audio_array.cpu().numpy().squeeze()
sampling_rate = model.generation_config.sample_rate

# Save the audio in the outputs directory
output_dir = "/outputs"
os.makedirs(output_dir, exist_ok=True)

# Save as wav format
wav_output_path = os.path.join(output_dir, "output.wav")

scipy.io.wavfile.write(wav_output_path, rate=sampling_rate, data=audio_array)