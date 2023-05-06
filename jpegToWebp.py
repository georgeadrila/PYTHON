import os
import subprocess

# Set the directory path containing the image files
directory = "C:/Users/George Adrian/Desktop/image-out"
#directory_new = "C:/Users/George Adrian/Desktop/image-out"

# Iterate over the files in the directory
for filename in os.listdir(directory):
    # Check if the file has a .jpg or .png extension
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Construct the input and output file paths
        input_file = os.path.join(directory, filename)
        output_file = os.path.join(directory, os.path.splitext(filename)[0] + ".webp")

        # Run the cwebp command to convert the image to WebP format
        subprocess.run(["cwebp", "-q", "80", input_file, "-o", output_file])
