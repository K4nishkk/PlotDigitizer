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

### Understandings
* Blurring -
    * Gaussian blur - to remove random noise of gaussian distribution.
    * Median blur - to remove salt and pepper noise
    * Bilateral filter - preserves edges (best working)

    >def bilateralFilter(
        src: MatLike,
        d: int, ------> most effect, works better on increasing
        sigmaColor: float, -------> 2nd most effective
        sigmaSpace: float,
        dst: MatLike | None = ...,
        borderType: int = ...
    ) -> MatLike

    * d
    Diameter of the filter kernel (the neighborhood size)
    Higher d → More pixels considered → More blurring
    * sigmaColor
    How much colors are mixed in the filtering process
    Higher sigmaColor → More colors blended → More smoothing
    * sigmaSpace
    How much nearby pixels influence each other
    Higher sigmaSpace → Larger spatial smoothing → More blurring

* Canny edge detection

    >def Canny(
        image: MatLike,
        threshold1: float,
        threshold2: float,
        edges: MatLike | None = ...,
        apertureSize: int = ...,
        L2gradient: bool = ...
    ) -> MatLike

    * threshold1 determines the minimum gradient strength needed to start considering a pixel as an edge.
    * Any pixel above threshold2 is a strong edge.
    * Pixels between threshold1 and threshold2 are considered weak edges and will be included only if they are connected to strong edges.
    * apperatureSize - Size of the Sobel kernel used for gradient calculation (default = 3, must be odd: 3, 5, 7)
    * L2gradient - If True, uses more accurate L2 norm for gradient calculation but takes more time