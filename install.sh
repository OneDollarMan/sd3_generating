#!/bin/bash

if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

source venv/bin/activate

# Installing torchvision for cuda 12.4
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# Installing diffusers 0.31.0.dev0 for original sd3
#if [ ! -d "diffusers" ]; then
#  git clone https://github.com/huggingface/diffusers
#fi
#cd diffusers
#git pull
#pip install -e .
#cd ..

# Installing diffusers for flash_sd3
pip install git+https://github.com/initml/diffusers.git@clement/feature/flash_sd3

# Installing diffusers for flux
#pip install -U diffusers

if [ -f "requirements.txt" ]; then
  pip3 install -r requirements.txt
else
  echo "requirements.txt not found"
fi