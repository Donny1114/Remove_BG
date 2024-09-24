# Background Remover App

## Overview

The Background Remover App is a simple Python application that allows users to remove backgrounds from images using the `rembg` library. 
The app provides a graphical user interface (GUI) for easy image selection, background removal, and output saving.

## Features

- Select an image file (supports JPG and PNG formats).
- Preview the selected image.
- Remove the background from the selected image.
- Save the processed image to your local storage.
- Automatic reset of the interface after saving an image.

## Requirements

To run this application, you need to have Python installed on your system. Additionally, you need the following Python packages:

- `Pillow`
- `rembg`
- `tkinter` (usually included with Python)

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
