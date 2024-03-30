# Setup

Eerste virtual environment maken: 
- Python3.11.8 -m venv .myvenv ( python<version> -m venv <virtual-environment-name> ) => eerste switchen naar **python3.11.8**
- .venv\Scripts\activate
- pip install -r requirements.txt

# Dependencies

1. Pytorch nodig dat compatibel is met CUDA: https://pytorch.org/get-started/locally/ : stable2.2 & CUDA 12.1

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

2. pip install -U xformers diffusers transformers accelerate

🤗 xFormers for both inference and training. In our tests, the optimizations performed in the attention blocks allow for both faster speed and reduced memory consumption.
🤗 Accelerate speeds up model loading for inference and training.
🤗 Transformers is required to run the most popular diffusion models, such as Stable Diffusion.

*handige guide: https://thepythoncode.com/article/control-generated-images-with-controlnet-with-huggingface#introduction*