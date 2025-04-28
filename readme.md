# Lilypad-bark-module

This repo represents the [suno/bark model](https://github.com/suno-ai/bark) as a module to be run on the Lilypad Network to produce text-to-audio inference

# Inputs

The module allows you to pass in a piece of text and generate an audio sample using the following parameters

- PROMPT -> The text to generate the audio sample from
- VOiCE -> The voice to be used to read the text (i.e `john` or `jane`)
- LANGUAGE -> The accent type to use for the voice ("en", "fr", "de", "es", "it", "ja", "zh", "pt", "pl", "ru", "ko", "tr", "hi")

# How to run

Run this on the lilypad network via:

```bash
lilypad run gihub.com/Lilypad-Tech/lilypad-bark-module:<add-commit-hash-here> -i prompt="hello world" -i voice="john" -i language="en"
```

or through the Anura API

# Notes

- This model does not suppot creating custom voices or creating a copy of your own voice

# Acknowledgments

- [suno/bark model](https://github.com/suno-ai/bark)