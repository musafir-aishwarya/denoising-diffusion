Denoising Diffusion Probabilistic Models Implementation in Pytorch
========
## Trained Checkpoint Folder

* The size of the checkpoints trained is very large, so I have put them in the Drive. Accessible using the below link:

* https://drive.google.com/drive/folders/1s7EwOxeqjoiDhYDOdHGABC0x5sYlH7wx?usp=sharing    

* Download this folder and put it in the code repo for the trained checkpoints and generated samples.


## Data preparation
For setting up the mnist dataset:

Follow - https://github.com/explainingai-code/Pytorch-VAE#data-preparation

## Training on our own images
For this one would need to make the following changes
* Put the image files in a folder created within the repo root (example: data/images/*.png ). The data folder should only have one directory 'images'
* Comment https://github.com/explainingai-code/DDPM-Pytorch/blob/main/dataset/mnist_dataset.py#L42 as this is only valid for mnist
* Update the expected number of channels here and image dimensions(assumed square images) here - https://github.com/explainingai-code/DDPM-Pytorch/blob/main/config/default.yaml#L10
* Change the config path here to point to 'data' directory('data' and not 'data/images') - https://github.com/explainingai-code/DDPM-Pytorch/blob/main/config/default.yaml#L2
* Right now the code has been written for picking up png files in mnist data directory format, so I assume there are subdirectories inside the directory mentioned in config and these sub-directories have .png files. 
This would work if you have .png files. If the images are of other formats or combination of different formats then one would have to change the load_images function correspondingly here - https://github.com/explainingai-code/DDPM-Pytorch/blob/main/dataset/mnist_dataset.py#L29C9-L29C9
* As of now code is written assuming square images, if thats not the case then just changing the dimensions to desired one during sampling should work - https://github.com/explainingai-code/DDPM-Pytorch/blob/main/tools/sample_ddpm.py#L20


# Quickstart
* Create a new conda environment with python 3.8 then run below commands
* ```git clone https://github.com/explainingai-code/DDPM-Pytorch.git```
* ```cd DDPM-Pytorch```
* ```pip install -r requirements.txt```
* For training/sampling use the below commands passing the desired configuration file as the config argument in case you want to play with it. 
* ```python -m tools.train_ddpm``` for training ddpm
* ```python -m tools.sample_ddpm``` for generating images

## Configuration
* ```config/default.yaml``` - Allows you to play with different components of ddpm  


## Output 
Outputs will be saved according to the configuration present in yaml files.

For every run a folder of ```task_name``` key in config will be created

During training of DDPM the following output will be saved 
* Latest Model checkpoint in ```task_name``` directory

During sampling the following output will be saved
* Sampled image grid for all timesteps in ```task_name/samples/*.png``` 
