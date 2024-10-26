# Overlay QR Code Image on Template

## Description

The Overlay Image Generator is a Python program that combines a specified overlay image (e.g., a QR code) with multiple background images to create new images. This is particularly useful for branding, marketing, or creating visual content where you want to overlay a specific graphic onto various backgrounds.

This program was created for [Feedbacker Reviews](https://feedbacker.cx/reviews/).

## Features

- Resizes the overlay image to a specified scale.
- Supports multiple background images in a predefined list.
- Allows customization of the overlay image's position on the background.
- Outputs the combined images with dynamically generated filenames that include both the overlay and background image names.

## Requirements

- Python 3.x
- Pillow library (Python Imaging Library)

### Installation

You can install the Pillow library using pip. Run the following command:

```bash
pip install Pillow
```

## Usage

1. Modify Image Paths:

Ensure to change the paths of the overlay and background images in the script. You will need to replace the file paths in the `background_paths` list and `overlay_path` variable with your local file paths.

2. Set Overlay Position:

Adjust the position variable in the code to determine where the overlay image should appear on the background image.

3. Run the Program:

Execute the script using Python. The program will generate new images with the overlay applied to each background image.
```bash
python overlay_image_generator.py
```

4. Output:

The generated images will be saved in the specified output folder with filenames formatted as `result_<overlay_name>_<background_name>.png`.

## Example:

If your overlay image is named `qr-code_gust.png` and you have background images named `v1-1.png`, `v1-2.png`, etc., the output filenames will be:

- `result_qr-code_gust_v1-1.png`
- `result_qr-code_gust_v1-2.png`
- ...

## Note

Ensure that the image files are accessible in the specified locations. If you receive a `FileNotFoundError`, double-check the paths provided in the code.
You may need to adjust the scaling factor for resizing the overlay image depending on your specific use case.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any inquiries or feedback, please contact:

Felipe Valencia - CEO & Data Scientist at [Dataplicada](https://dataplicada.com/)

- f.valencia-clavijo@uea.ac.uk
- fevacla@byui.edu