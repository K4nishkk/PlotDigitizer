import cv2
import numpy as np

def detect_axes(edges, original_image):
    lines = cv2.HoughLinesP(image=edges, rho=1, theta=np.pi / 180, threshold=100, minLineLength=150, maxLineGap=10)
    
    if lines is not None:
        x_axis, y_axis = None, None
        horizontal_lines = []
        vertical_lines = []
        
        # Filter lines using slope
        for line in lines:
            x1, y1, x2, y2 = line[0]
            slope = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')
            
            if abs(slope) < 0.1:
                horizontal_lines.append(line[0])
            elif abs(slope) > 10:
                vertical_lines.append(line[0])
        
        # Assign largest lines as axes
        if horizontal_lines:
            x_axis = max(horizontal_lines, key=lambda line: line[2] - line[0])
        if vertical_lines:
            y_axis = max(vertical_lines, key=lambda line: line[3] - line[1])
        
        # Draw the detected axes on the image (if found)
        if x_axis is not None:
            cv2.line(original_image, (x_axis[0], x_axis[1]), (x_axis[2], x_axis[3]), (0, 255, 0), 2)
        if y_axis is not None:
            cv2.line(original_image, (y_axis[0], y_axis[1]), (y_axis[2], y_axis[3]), (0, 255, 0), 2)
    
    return original_image