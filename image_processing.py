"""
    This module contains functions for processing images.
    It can be used to check if an image contains hidden data
    and remove it if necessary.

    Uses the technique of least significant bit (LSB) steganography.
"""

from pathlib import Path
from PIL import Image
import numpy as np


def has_hidden_data(image_path: Path) -> bool:
    """
    #1
    """
    image = Image.open(image_path)
    pixels = np.array(image)

    # Check the LSB of each color channel
    lsb_changes = (pixels & 1).sum()
    total_bits = pixels.size * 8  # 8 bits per color channel

    threshold = total_bits * 0.01  # .1% change threshold
    if lsb_changes > threshold:
        return True
    return False


def clean_image(image_path: Path, output_path: Path) -> None:
    """
    #2
    """
    image = Image.open(image_path)
    pixels = np.array(image)

    # Zero out the LSB of each color channel
    clean_pixels = pixels & ~1

    # Ensure the numpy array is of type 'uint8' (unsigned 8-bit integer)
    clean_pixels = clean_pixels.astype(np.uint8)

    # Create and save the cleaned image
    clean_img = Image.fromarray(clean_pixels)
    clean_img.save(output_path)
