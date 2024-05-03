import os
import imageio.v2 as imageio
from imgaug import augmenters as iaa
import random
from tqdm import tqdm  

# Define the input and output directories and the number of augmented images you want
input_dir = './image_test'  # Update this to your input directory path
output_base_dir = './augemmted_images'  # Update this to your desired base output directory path
number_of_augmented_images = 100 # Update this to the number of augmented images you want

# Basic augmentations applied to all sequences
basic_augmentations = [
    iaa.Fliplr(0.5),  # Horizontal flips
    iaa.Multiply((0.8, 1.2), per_channel=0.2),
    iaa.GaussianBlur(sigma=(0, 1.0)),
    iaa.LinearContrast((0.75, 1.5)),
    iaa.Affine(
        scale={"x": (0.8, 1.0), "y": (0.8, 1.0)},
        translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)},
        rotate=(-15, 15),
        shear=(-8, 8)
    )
]

# Define separate augmentation sequences for different effects
augmentations = [
    iaa.Sequential(basic_augmentations + [
        iaa.AdditiveGaussianNoise(loc=0, scale=(0.02*255, 0.1*255), per_channel=0.5)
    ]),
    iaa.Sequential(basic_augmentations + [
        iaa.SaltAndPepper(0.02)
    ]),
    iaa.Sequential(basic_augmentations + [
        iaa.Salt(0.02)
    ]),
    iaa.Sequential(basic_augmentations + [
        iaa.Pepper(0.02)
    ]),
    iaa.Sequential(basic_augmentations + [
        iaa.AdditivePoissonNoise(lam=(0, 2))
    ]),
    iaa.Sequential(basic_augmentations + [
        iaa.AdditiveLaplaceNoise(scale=(0, 0.15*255))
    ]),
    iaa.Sequential(basic_augmentations + [
        iaa.AddToHueAndSaturation((-30, 30)),  # Adjust hue and saturation
        iaa.Grayscale(alpha=(0.0, 1.0))  # Convert to grayscale with a certain probability
    ]),
    iaa.Sequential(basic_augmentations + [
        iaa.PerspectiveTransform(scale=(0.01, 0.1))
    ])
]

# Process each image in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(input_dir, filename)
        image = imageio.imread(image_path)
        
        # Convert RGBA to RGB if necessary
        if image.shape[-1] == 4:
            image = image[..., :3]

        output_dir = os.path.join(output_base_dir, os.path.splitext(filename)[0])
        os.makedirs(output_dir, exist_ok=True)
        
        # Randomly select an augmentation sequence for each image
        seq = random.choice(augmentations)
        
        # Generate augmented images with progress bar
        for i in tqdm(range(number_of_augmented_images), desc=f"Processing {filename}"): 
            img_aug = seq.augment_image(image)
            output_path = os.path.join(output_dir, f'augmented_{i}.jpg')
            imageio.imwrite(output_path, img_aug)

print("Augmentation complete. Images saved to:", output_base_dir)
