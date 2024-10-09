# Setup

First you create a virtual environment: 
- Python3.11.8 -m venv .myvenv
- .venv\Scripts\activate (windows)
- pip install -r requirements.txt

# Dependencies
1. Install Pytorch + CUDA: https://pytorch.org/get-started/locally/ : stable2.2 & CUDA 12.1
2. pip install -U xformers diffusers transformers accelerate

🤗 xFormers for both inference and training. In our tests, the optimizations performed in the attention blocks allow for both faster speed and reduced memory consumption.\
🤗 Accelerate speeds up model loading for inference and training.\
🤗 Transformers is required to run the most popular diffusion models, such as Stable Diffusion.

*usefull guide*: https://thepythoncode.com/article/control-generated-images-with-controlnet-with-huggingface#introduction

# Models
1. runwayml/stable-diffusion-v1-5 => SD 1.5 doesn't generate realistic images
2. stablediffusionapi/realistic-vision-v20-2047 -> works really well

# Inference
Just run the jupyter notebook **model.ipynb**. 
