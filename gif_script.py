import os
import imageio.v2 as imageio
from PIL import Image
import numpy as np

def make_gif_from_images(folder_path, output_path, duration=0.1):
    # Get a list of all PNG files in the folder
    images = [img for img in os.listdir(folder_path) if img.endswith('.png')]
    # Sort images by filename
    images.sort()
    
    # Determine the largest dimensions
    max_width = 0
    max_height = 0
    for image in images:
        img_path = os.path.join(folder_path, image)
        with Image.open(img_path) as img:
            if img.width > max_width:
                max_width = img.width
            if img.height > max_height:
                max_height = img.height
    
    # Create a list to store the resized image objects
    frames = []
    
    for image in images:
        img_path = os.path.join(folder_path, image)
        with Image.open(img_path) as img:
            # Create a new transparent image with the largest dimensions for each frame
            new_img = Image.new("RGBA", (max_width, max_height), (0, 0, 0, 0))
            # Calculate the position to paste the image to keep it centered
            paste_position = ((max_width - img.width) // 2, (max_height - img.height) // 2)
            # Paste the image onto the center of the transparent image
            new_img.paste(img, paste_position)
            
            # Convert the new image to a numpy array and append to frames
            frames.append(np.array(new_img))

    # Save the frames as a GIF
    imageio.mimsave(output_path, frames, 'GIF', duration=duration)

folder_path = '/Users/michaelalva/Desktop/8630.3/8817/assets/8839-2-gif'
output_path = '/Users/michaelalva/Desktop/8630.3/8817/assets/8839-2-gif'
make_gif_from_images(folder_path, f'{output_path}2.gif')
