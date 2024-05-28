"""
    a)
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

    lsb_changes = (pixels & 1).sum()
    total_bits = pixels.size * 8

    threshold = total_bits * 0.01
    if lsb_changes > threshold:
        return True
    return False


def clean_image(image_path: Path, output_path: Path) -> None:
    """
    #2
    """
    image = Image.open(image_path)
    pixels = np.array(image)

    clean_pixels = pixels & ~1

    clean_pixels = clean_pixels.astype(np.uint8)

    clean_img = Image.fromarray(clean_pixels)
    clean_img.save(output_path)
