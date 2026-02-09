Studio Portrait Pipeline
A Python-based studio-quality portrait enhancement pipeline that converts ordinary portrait images into professional-looking studio-style outputs 
using semantic segmentation, background blur, and color grading. The pipeline is designed to be simple, modular, and easy to extend for research or application-level use.

Features
Portrait segmentation to separate the subject from the background
Selective background blur to simulate shallow depth of field
Color grading for improved contrast, tone, and visual appeal
Modular pipeline where each processing stage can be modified independently

Supports common image formats such as JPG and PNG

Project Structure
studio_portrait_pipeline/
├── segmentation.py – Subject/person segmentation logic
├── background_blur.py – Applies background blur using segmentation mask
├── color_grading.py – Color enhancement and tonal adjustments
├── main.py – Entry point for running the full pipeline
├── .gitignore

Pipeline Workflow
The pipeline processes an input image in three main stages. First, semantic segmentation is performed to identify the portrait subject and generate a foreground mask. 
Next, the background blur stage applies a selective blur only to the background region while preserving subject sharpness. 
Finally, color grading is applied to enhance brightness, contrast, and color balance, resulting in a studio-style portrait.

Usage
The complete pipeline can be executed by running the main script using Python. Input and output image paths, along with processing parameters such as 
blur strength and color adjustments, can be modified directly inside the main.py file.

Customization
Each module in the pipeline is independent and can be replaced or extended. The segmentation stage can be swapped with another model, 
the background blur strength can be tuned for different depth effects, and the color grading logic can be adjusted to match specific visual styles or presets. 
The pipeline can also be integrated into other Python applications or services.

Use Cases
This project is suitable for studio-style profile photos, resume or portfolio portraits, social media image enhancement, and automated photography post-processing workflows.

Future Scope
Potential enhancements include adding command-line arguments, batch image processing support, GPU acceleration, multiple color grading presets, and integration with web or API-based applications.

