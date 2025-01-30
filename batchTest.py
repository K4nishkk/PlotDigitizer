import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

def batchTest():
    testOption: str = sys.argv[1]

    if testOption == "-m":
        manyImageSameTest(int(sys.argv[2]))
    elif testOption == "-s":
        sameImageManyTest(sys.argv[2:])
    else:
        print("Unidentified flag used")

def manyImageSameTest(nImage: int):
    rows: int = int((nImage - 1) / 3 + 1)
    cols: int = 3
    plt.figure(figsize=(20, 10))

    for i in range(nImage):
        image_path = f"images/graph{i}.png"
        processedImage = process(image_path)

        plt.subplot(rows, cols, i + 1)
        plt.title(f"Image {i + 1}")
        plt.imshow(processedImage, cmap="gray")
        plt.axis("off")

    plt.show()

def sameImageManyTest(options: list):
    imageNum = options[0]
    start = int(options[1])
    end = int(options[2])
    gap = int((end - start) / 8 + 1)
    index = 1

    rows: int = 2
    cols: int = 4
    plt.figure(figsize=(20, 10))
    image_path = f"images/graph{imageNum}.png"

    for i in range(start, end + 1, gap):
        processedImage = process(image_path, i)

        plt.subplot(rows, cols, index)
        plt.title(f"Value: {i}")
        plt.imshow(processedImage, cmap="gray")
        plt.axis("off")

        index = index + 1

    plt.show()

def process(image_path: str, VALUE: int = ...):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # blurred = cv2.GaussianBlur(gray, (VALUE, VALUE), 0)
    # blurred = cv2.medianBlur(gray, 5)
    blurred = cv2.bilateralFilter(gray, VALUE, 75, 75)
    # thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, VALUE, 2)
    edges = cv2.Canny(blurred, 100, 150)
    return edges

if __name__ == "__main__":
    batchTest()