import sys

from preprocess import preprocess_image
from axisDetection import detect_axes
from displayImages import displayImage

def main(image_path):
    # Step 1: Preprocess the image
    original_image, preprocessed_image = preprocess_image(image_path)
    
    # Step 2: Detect axes
    axes_image = detect_axes(preprocessed_image, original_image.copy())
    
    # Step 3: Display all images side by side
    displayImage(original_image, preprocessed_image, axes_image)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Image number not entered")
        sys.exit()
    
    image_path = f"images/graph{sys.argv[1]}.png"
    main(image_path)
