import os
from PIL import Image
import pillow_heif
from pathlib import Path

def convert_heic_to_jpg(folder_path):
    """
    Convert all HEIC files in the specified folder to JPG format.
    
    Args:
        folder_path (str): Path to the folder containing HEIC files
    """
    # Register HEIF opener to handle HEIC files
    pillow_heif.register_heif_opener()
    
    # Create folder for converted images if it doesn't exist
    output_folder = os.path.join(folder_path, "converted_jpg")
    os.makedirs(output_folder, exist_ok=True)
    
    # Get all HEIC files in the folder
    heic_files = list(Path(folder_path).glob("*.HEIC")) + list(Path(folder_path).glob("*.heic"))
    
    if not heic_files:
        print("No HEIC files found in the specified folder.")
        return
    
    # Convert each HEIC file to JPG
    for heic_file in heic_files:
        try:
            # Construct output filename
            jpg_filename = os.path.join(output_folder, f"{heic_file.stem}.jpg")
            
            # Open and convert HEIC to JPG
            with Image.open(heic_file) as img:
                # Convert to RGB mode if necessary
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Save as JPG
                img.save(jpg_filename, 'JPEG', quality=95)
            
            print(f"Successfully converted: {heic_file.name} -> {os.path.basename(jpg_filename)}")
            
        except Exception as e:
            print(f"Error converting {heic_file.name}: {str(e)}")

if __name__ == "__main__":
    # Example usage
    folder_path = input("Enter the folder path containing HEIC files: ")
    convert_heic_to_jpg(folder_path)