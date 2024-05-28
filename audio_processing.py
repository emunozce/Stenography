"""
    b)
"""

import numpy as np
from scipy.io import wavfile


def clean_audio(audio_path, output_path):
    """
    #5
    """
    rate, data = wavfile.read(audio_path)

    if data.dtype == np.int16:
        clean_data = data & ~1
        clean_data = clean_data.astype(np.int16)
        wavfile.write(output_path, rate, clean_data)
        print(f"Audio cleaned and saved to {output_path}.")
