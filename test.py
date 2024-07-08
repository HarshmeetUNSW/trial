import os
import gdown
import streamlit as st

def download_model(url, output_path):
    # Check if the file already exists
    if not os.path.exists(output_path):
        # File doesn't exist, download it
        st.write("Downloading model...")
        gdown.download(url, output_path, quiet=False)
    else:
        # File exists, no need to download
        st.write("Model already downloaded.")

# URL of the model file on Google Drive
# url = 'https://drive.google.com/uc?id=1eb5CZJgcqKthwMl2TgKZF2HFrwsGDJ3d/view?usp=sharing'

url ="https://drive.google.com/file/d/1eb5CZJgcqKthwMl2TgKZF2HFrwsGDJ3d/view?usp=sharing"

# Desired path to save the downloaded file
output_path = 'model/model.safetensors'

download_model(url, output_path)

# Proceed with your model loading and other operations
