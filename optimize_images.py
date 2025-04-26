import os
from PIL import Image
from pathlib import Path

def optimize_image(input_path, output_path, max_width=1200, quality=85):
    """Optimize a single image by resizing and compressing."""
    try:
        with Image.open(input_path) as img:
            # Calculate new dimensions while maintaining aspect ratio
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Save optimized image
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
            print(f"Optimized: {input_path} -> {output_path}")
            
    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")

def process_directory(input_dir, output_dir):
    """Process all images in a directory and its subdirectories."""
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    
    # Supported image extensions
    image_extensions = {'.jpg', '.jpeg', '.png'}
    
    # Walk through all files in the directory
    for root, _, files in os.walk(input_dir):
        for file in files:
            if Path(file).suffix.lower() in image_extensions:
                input_path = Path(root) / file
                # Create corresponding output path
                relative_path = input_path.relative_to(input_dir)
                output_path = output_dir / relative_path
                
                optimize_image(str(input_path), str(output_path))

if __name__ == "__main__":
    input_dir = "croatiamontenegro"
    output_dir = "croatiamontenegro_optimized"
    
    print("Starting image optimization...")
    process_directory(input_dir, output_dir)
    print("Image optimization complete!") 