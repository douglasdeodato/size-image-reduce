import os
from PIL import Image

def reduce_image_size(image_path, output_path, quality=85):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Convert to RGB (to ensure compatibility with JPEG format)
            img = img.convert('RGB')
            
            # Create directories in the output folder if they don't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Save the optimized image
            img.save(output_path, format='JPEG', quality=quality, optimize=True)
            
            print(f"Processed: {image_path} -> {output_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_images_in_folder(input_folder, output_folder, quality=85):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png')):
                # Construct the full input path
                input_path = os.path.join(root, file)
                
                # Determine the relative path to maintain subfolder structure
                relative_path = os.path.relpath(input_path, input_folder)
                
                # Construct the full output path, ensuring it mirrors the input structure
                output_path = os.path.join(output_folder, relative_path)
                
                # Replace PNG extension with JPG if needed
                if file.lower().endswith('png'):
                    output_path = output_path.rsplit('.', 1)[0] + '.jpg'
                
                # Optimize and save the image
                reduce_image_size(input_path, output_path, quality)

    print("Image processing completed.")

# Example usage
if __name__ == "__main__":
    input_folder = 'images'  # Ensure this folder exists
    output_folder = 'images-reduced'

    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist. Please check the path.")
    else:
        process_images_in_folder(input_folder, output_folder)
