from rembg import remove
from PIL import Image

def segment_person(input_path, output_path):
    img = Image.open(input_path).convert("RGB")
    fg = remove(img)   # RGBA output
    fg.save(output_path)
