import cv2
import numpy as np
import os
from google.colab.patches import cv2_imshow

# Input and output directories
input_folder = '/content/Images'  # Folder containing your input images
output_folder = '/content/drive/MyDrive/processed_imgs'  # Folder to save processed images

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# CLAHE settings
n = 1  # Tile grid size
clip_limit = 1.0

# Define CLAHE function
def apply_clahe(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(n, n))
    lab[:, :, 0] = clahe.apply(lab[:, :, 0])
    enhanced_image = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    return enhanced_image

# Define RGB enhancement function
def apply_rgb_method(image):
    b, g, r = cv2.split(image)
    b = cv2.equalizeHist(b)
    g = cv2.equalizeHist(g)
    r = cv2.equalizeHist(r)
    enhanced_image = cv2.merge((b, g, r))
    return enhanced_image

# Process all images in the folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        if image is None:
            print(f" Skipping {filename} (cannot read file).")
            continue

        # Apply CLAHE
        image_clahe = apply_clahe(image)

        # Apply RGB method
        image_enhanced = apply_rgb_method(image_clahe)

        # Save processed image
        output_path = os.path.join(output_folder, f"processed_{filename}")
        cv2.imwrite(output_path, image_enhanced)

        print(f"✅ Processed and saved: {output_path}")

        # Display the result for each image
        print(f"\nOriginal Image: {filename}")
        cv2_imshow(image)
        print(f"Enhanced Image: processed_{filename}")
        cv2_imshow(image_enhanced)

print("\n All images processed successfully!")
