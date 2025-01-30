import matplotlib.pyplot as plt
import cv2

def displayImage(original_image, preprocessed_image, axes_image):
    plt.figure(figsize=(20, 10))
    
    plt.subplot(2, 2, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    
    plt.subplot(2, 2, 2)
    plt.title("Preprocessed Image")
    plt.imshow(preprocessed_image, cmap="gray")
    plt.axis("off")
    
    plt.subplot(2, 2, 3)
    plt.title("Detected Axes")
    plt.imshow(cv2.cvtColor(axes_image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    
    plt.show()