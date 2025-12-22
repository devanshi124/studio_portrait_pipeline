import cv2
import numpy as np
from PIL import Image

def apply_background_blur(fg_path, bg_path, output_path):
    # Load foreground (RGBA, RGB order)
    fg = Image.open(fg_path).convert("RGBA")
    fg_np = np.array(fg)

    # Convert foreground RGB -> BGR
    fg_rgb = fg_np[:, :, :3]
    fg_bgr = cv2.cvtColor(fg_rgb, cv2.COLOR_RGB2BGR)

    alpha = fg_np[:, :, 3] / 255.0
    alpha = alpha[:, :, None]

    # Load background (BGR)
    bg = cv2.imread(bg_path)
    bg_blur = cv2.GaussianBlur(bg, (61, 61), 0)

    # Composite (ALL BGR now)
    result = fg_bgr * alpha + bg_blur * (1 - alpha)
    result = result.astype(np.uint8)

    cv2.imwrite(output_path, result)
