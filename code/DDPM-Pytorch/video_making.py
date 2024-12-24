import cv2
import os
import re

# Path to the directory containing images
image_folder = './default/good_alotsamples'
output_video_file  = './alot_video.mp4'
fps = 30  # Frames per second

# Function to sort filenames numerically by extracting the number after 'x0_'
def numerical_sort(file):
    # Extracts numeric parts and pads them for accurate numeric sorting
    parts = re.findall(r'\d+', file)
    return tuple(int(part) for part in parts)

# Get the list of all files in the image directory with the PNG extension and sort them
all_files = os.listdir(image_folder)
image_files = [f for f in all_files if f.startswith('x0_') and f.endswith('.png')]
sorted_filenames = sorted(image_files, key=numerical_sort, reverse=True)

# Check if we have any images to process
if not sorted_filenames:
    raise ValueError("No images found in the folder.")

# Read the first image to determine the size
first_image_path = os.path.join(image_folder, sorted_filenames[0])
first_image = cv2.imread(first_image_path)
if first_image is None:
    raise ValueError("Error reading the first image.")

height, width, channels = first_image.shape
video_size = (width, height)

# Create a VideoWriter object
video_writer = cv2.VideoWriter(output_video_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, video_size)

# Add images to the video writer in reverse order
for filename in sorted_filenames:
    image_path = os.path.join(image_folder, filename)
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Error reading image {filename}.")
    video_writer.write(image)

# Release the VideoWriter object
video_writer.release()

output_video_file  # Return the path of the created video
