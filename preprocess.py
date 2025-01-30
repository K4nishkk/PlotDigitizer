import cv2

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # blurred = cv2.medianBlur(gray, 5)
    blurred = cv2.bilateralFilter(gray, 19, 75, 75)
    edges = cv2.Canny(blurred, 100, 150)
    return image, edges