### Preprocessing
* Read image
* convert to grayscale
* apply gaussian blur (remove random noise)
* Canny edge detection

Suggested operations -
* Adaptive thresholding (to enhance light lines)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
* Enhance contrast (using historam equalization)
    equalized = cv2.equalizeHist(gray)
* Apply binary threshold (creates a binary image)
    _, thresh = cv2.threshold(equalized, 100, 255, cv2.THRESH_BINARY)
* morphological operations (to close gaps in faint lines)
    kernel = np.ones((5, 5), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

### Axis Detection
* Hough transform
* filter lines using slope
* assing longest line as axes
* draw them on original image