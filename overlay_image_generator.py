from PIL import Image
import os

# List of background image paths
background_paths = [
    'C:/Users/felip/Downloads/v1-1.png',
    'C:/Users/felip/Downloads/v1-2.png',
    'C:/Users/felip/Downloads/v1-3.png',
    'C:/Users/felip/Downloads/v2-1.png',
    'C:/Users/felip/Downloads/v2-2.png',
    'C:/Users/felip/Downloads/v2-3.png',
    'C:/Users/felip/Downloads/v3-1.png',
    'C:/Users/felip/Downloads/v3-2.png',
    'C:/Users/felip/Downloads/v3-3.png'
]

# Overlay image path and position settings
overlay_path = 'C:/Users/felip/Downloads/qr-code_gust.png'
overlay_name = os.path.splitext(os.path.basename(overlay_path))[0]  # Get the overlay filename without extension
position = (235, 685)  # Set overlay position on each background
output_folder = 'C:/Users/felip/Downloads/'

# Open and resize the overlay image
overlay_img = Image.open(overlay_path)
new_size = (int(overlay_img.width * 2.1), int(overlay_img.height * 2.1))
overlay_img = overlay_img.resize(new_size, Image.LANCZOS)

# Loop over background images, apply the overlay, and save each result
for bg_path in background_paths:
    background = Image.open(bg_path)
    background.paste(overlay_img, position, overlay_img)  # 'overlay_img' keeps transparency
    
    # Create a unique name for each output image
    bg_name = os.path.splitext(os.path.basename(bg_path))[0]  # Get background filename without extension
    output_path = os.path.join(output_folder, f'result_{overlay_name}_{bg_name}.png')
    
    # Save the modified image
    background.save(output_path)

print("Images created and saved successfully!")
