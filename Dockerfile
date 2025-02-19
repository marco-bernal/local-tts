# This file is specific to HuggingFace spaces, since it relies on having a root-less user.
# Using requirements.txt and standard python image since UV doesn't support root-less users up until now.
FROM python:3.11-slim-bookworm

# Create a user to copy and download files.
RUN useradd -m -u 1000 user
# Switch to the "user" user
USER user
# Set home to the user's home directory
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH
# Set up '/app' as working directory.
WORKDIR $HOME/app

# Install project dependencies with pip from the requirements.txt file
COPY --chown=user requirements.txt $HOME/app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the application from the builder.
COPY --chown=user datasets/english_models.csv $HOME/app/datasets/english_models.csv
COPY --chown=user main.py $HOME/app

# Set up server and port 7860, required by hugging face and gradio.
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Command to run the app with UV.
ENTRYPOINT ["python", "main.py"]