import glob
import os

import torchvision
from PIL import Image
from tqdm import tqdm
from torch.utils.data.dataloader import DataLoader
from torch.utils.data.dataset import Dataset


def get_square_crop(image, size):
    # Get dimensions
    w, h = image.size

    # Determine the size of the square (the smaller dimension of the image)
    min_dim = size

    # Calculate cropping coordinates
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    right = (w + min_dim) // 2
    bottom = (h + min_dim) // 2

    # Crop the image to a square
    image = image.crop((left, top, right, bottom))
    return image

def img_resize(image, size):
    # Ensure size is a tuple for the resize method
    if isinstance(size, int):
        size = (size, size)
    resized_image = image.resize(size)  # Resize using the size parameter
    return resized_image


class MnistDataset(Dataset):
    r"""
    Nothing special here. Just a simple dataset class for mnist images.
    Created a dataset class rather using torchvision to allow
    replacement with any other image dataset
    """
    def __init__(self, split, im_path, im_ext='png'):
        r"""
        Init method for initializing the dataset properties
        :param split: train/test to locate the image files
        :param im_path: root folder of images
        :param im_ext: image extension. assumes all
        images would be this type.
        """
        self.im_size = 28 ################################# for textures, size fixing
        self.split = split
        self.im_ext = im_ext
        self.images, self.labels = self.load_images(im_path)
    
    def load_images(self, im_path):
        r"""
        Gets all images from the path specified
        and stacks them all up
        :param im_path:
        :return:
        """
        assert os.path.exists(im_path), "images path {} does not exist".format(im_path)
        ims = []
        labels = []
        for d_name in tqdm(os.listdir(im_path)):
            for fname in glob.glob(os.path.join(im_path, d_name, '*.{}'.format(self.im_ext))):
                ims.append(fname)
                labels.append(int(d_name))
        print('Found {} images for split {}'.format(len(ims), self.split))
        return ims, labels
    
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, index):
        im = Image.open(self.images[index])
        im = img_resize(im, self.im_size)        #################################textures
        im_tensor = torchvision.transforms.ToTensor()(im)
        
        # Convert input to -1 to 1 range.
        im_tensor = (2 * im_tensor) - 1
        return im_tensor
