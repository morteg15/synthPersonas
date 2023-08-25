from PIL import Image
import os

def resize_images_in_folder(src_folder, dest_folder, new_size):
    """
    Resize all jpg images in the source folder to the specified size
    and save them in the destination folder.
    
    Parameters:
    - src_folder: Path to the source folder containing jpg images.
    - dest_folder: Path where resized images will be saved.
    - new_size: A tuple (width, height) specifying the desired size.
    """
    # Ensure the destination folder exists
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # Loop through each file in the source folder
    for filename in os.listdir(src_folder):
        if filename.endswith(".jpg"):
            filepath = os.path.join(src_folder, filename)
            with Image.open(filepath) as img:
                # Resize the image
                resized_img = img.resize(new_size)
                
                # Save the resized image to the destination folder
                resized_img_path = os.path.join(dest_folder, filename)
                resized_img.save(resized_img_path, "JPEG")
                print(f"Resized {filename} and saved to {resized_img_path}")

if __name__ == "__main__":
    # Example usage
    source_folder = "data\profilepictures_o"
    destination_folder = "data\profilepictures"
    target_size = (800, 600)  # For example, resize to 800x600
    resize_images_in_folder(source_folder, destination_folder, target_size)
