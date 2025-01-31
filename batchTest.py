import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt
from preprocess import preprocess_image, compute_gradient_variation
from axisDetection import detect_axes

def batchTest():
    testOption: str = sys.argv[1]

    if testOption == "-m":
        manyImagesSameTest(nImage=5)
    elif testOption == "-s":
        sameImageManyTests(sys.argv[2:])
    elif testOption == "-a":
        allImagesTestOutput(nImage=5)
    else:
        print("Unidentified flag used")

def manyImagesSameTest(nImage: int):
    rows: int = int((nImage - 1) / 3 + 1)
    cols: int = 3
    plt.figure(figsize=(20, 10))

    for i in range(nImage):
        image_path = f"images/graph{i}.png"
        originalImage = cv2.imread(image_path)
        processedImage = test(originalImage)

        plt.subplot(rows, cols, i + 1)
        plt.title(f"Image {i + 1}")
        plt.imshow(processedImage, cmap="gray")
        plt.axis("off")

    plt.show()

def sameImageManyTests(options: list):
    rows: int = 2
    cols: int = 3

    imageNum = options[0]
    start = int(options[1])
    end = int(options[2])
    gap = int((end - start) / (rows * cols) + 1)
    index = 1

    plt.figure(figsize=(20, 10))
    image_path = f"images/graph{imageNum}.png"
    original_image = cv2.imread(image_path)

    for i in range(start, end + 1, gap):
        processedImage = test(original_image, i)

        plt.subplot(rows, cols, index)
        plt.title(f"Value: {i}")
        plt.imshow(processedImage, cmap="gray")
        plt.axis("off")

        index = index + 1

    plt.show()

def test(image, VALUE: int = ...):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # blurred = cv2.GaussianBlur(gray, (VALUE, VALUE), 0)
    # blurred = cv2.medianBlur(gray, 5)
    blurred = cv2.bilateralFilter(gray, 1, 25, 75)
    # thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, VALUE, 2)
    edges = cv2.Canny(blurred, 100, 150, L2gradient=True)
    axes = detect_axes(edges, image)
    return axes

def allImagesTestOutput(nImage: int):
    rows: int = int((nImage - 1) / 3 + 1)
    cols: int = 3
    plt.figure(figsize=(20, 10))

    for i in range(nImage):
        image_path = f"images/graph{i}.png"
        originalImage, processedImage = preprocess_image(image_path)
        axesImage = detect_axes(processedImage, originalImage.copy())

        plt.subplot(rows, cols, i + 1)
        plt.title(f"Image {i + 1}")
        plt.imshow(axesImage, cmap="gray")
        plt.axis("off")

    plt.show()

if __name__ == "__main__":
    batchTest()