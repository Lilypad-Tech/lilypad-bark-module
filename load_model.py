from huggingface_hub import snapshot_download

# Download the model from the Hugging Face Hub
snapshot_download(repo_id="suno/bark", local_dir="./local-bark-model")
