#!/bin/bash

## download AE model
cd ..
mkdir -p first_stage_models/vq-f4 && cd first_stage_models/vq-f4 || exit
wget -O model.zip https://ommer-lab.com/files/latent-diffusion/vq-f4.zip
unzip -o model.zip
rm model.zip
