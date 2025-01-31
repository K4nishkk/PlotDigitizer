import cv2
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gradient_variation = compute_gradient_variation(gray)
    if (gradient_variation > 200):
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    elif (gradient_variation > 100):
        blurred = cv2.bilateralFilter(gray, 19, 75, 75)
    else:
        blurred = gray

    edges = cv2.Canny(blurred, 100, 150)
    return image, edges

def compute_gradient_variation(gray):
    # Compute Sobel gradients in X and Y directions
    Gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    Gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # Compute gradient magnitude and std
    gradient_magnitude = np.sqrt(Gx**2 + Gy**2)
    gradient_std = np.std(gradient_magnitude)

    return gradient_std