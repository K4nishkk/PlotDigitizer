import matplotlib.pyplot as plt
import cv2

def displayImage(original_image, preprocessed_image, axes_image):
    plt.figure(figsize=(15, 5))
    
    # Original Image
    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    
    # Preprocessed Image (Edges)
    plt.subplot(1, 3, 2)
    plt.title("Preprocessed Image (Edges)")
    plt.imshow(preprocessed_image, cmap="gray")
    plt.axis("off")
    
    # Image with Detected Axes
    plt.subplot(1, 3, 3)
    plt.title("Detected Axes")
    plt.imshow(cv2.cvtColor(axes_image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    
    plt.show()