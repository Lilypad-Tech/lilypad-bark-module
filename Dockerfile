# Base stage with common dependencies
FROM python:3.9-slim-buster AS base

# Set the working directory in the container
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    wget \
    ffmpeg \
    libsm6 \
    libxext6 \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Update pip and install base Python packages with specific numpy version
RUN pip install --no-cache-dir --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir \
    transformers \
    huggingface_hub==0.30.1 \
    scipy \
    torch

# Create directories for model cache
RUN mkdir -p /root/.cache/huggingface

# Copy the model files into the container
COPY local-bark-model /workspace/local-bark-model

# Create output directory
RUN mkdir -p /outputs && chmod 777 /outputs

# Production stage
FROM base AS production

# Copy the Python script into the container
COPY run_bark.py /workspace/run_bark.py
RUN chmod +x /workspace/run_bark.py

# Set default environment variables
ENV DEFAULT_PROMPT="Hey everyone,[clears throat] today I want to talk about something that’s been on my mind a lot lately—how AI is reshaping the way we work, create and live our lives."
ENV DEFAULT_VOICE="john"
ENV DEFAULT_LANGUAGE="en"

VOLUME /workspace/outputs

# Set the entrypoint to run the Python script
ENTRYPOINT ["python", "/workspace/run_bark.py"]