from segmentation import segment_person
from background_blur import apply_background_blur
from color_grading import color_grade

INPUT = "input/input.jpeg"
SEGMENTED = "output/foreground.png"
BLURRED = "output/blurred_bg.jpg"
FINAL = "output/final_studio_output.jpg"

print("▶ Step 1: Person segmentation")
segment_person(INPUT, SEGMENTED)

print("▶ Step 2: Background blur")
apply_background_blur(SEGMENTED, INPUT, BLURRED)

print("▶ Step 3: Color grading")
color_grade(BLURRED, FINAL)

print("✅ Studio portrait pipeline completed")
