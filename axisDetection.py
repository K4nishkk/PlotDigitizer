import cv2
import numpy as np

def detect_axes(edges, original_image):
    lines = cv2.HoughLinesP(image=edges, rho=1, theta=np.pi / 180, threshold=100, minLineLength=150, maxLineGap=10)
    
    if lines is not None:
        lines = remove_full_image_lines(lines, original_image.shape)
        horizontal_lines, vertical_lines = filter_lines_using_slope(lines)
        horizontal_lines, vertical_lines = filter_border_lines(horizontal_lines, vertical_lines, original_image.shape)
        x_axis, y_axis = get_axes(horizontal_lines, vertical_lines)
        origin = find_intersection(x_axis, y_axis)
        draw_axes_and_origin(original_image, x_axis, y_axis, origin)
    
    return original_image

def remove_full_image_lines(lines, image_shape):
    height, width = image_shape[:2]
    filtered_lines = []

    for line in lines:
        x1, y1, x2, y2 = line[0]

        # Ignore horizontal lines spanning the full width
        if not (x1 == 0 and x2 == width - 1):
            # Ignore vertical lines spanning the full height
            if not (y1 == 0 and y2 == height - 1):
                filtered_lines.append(line)

    return filtered_lines

def filter_lines_using_slope(lines):
    horizontal_lines = []
    vertical_lines = []
    
    for line in lines:
        x1, y1, x2, y2 = line[0]
        slope = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')
        
        if abs(slope) < 0.1:
            horizontal_lines.append(line[0])
        elif abs(slope) > 10:
            vertical_lines.append(line[0])

    return horizontal_lines, vertical_lines

def filter_border_lines(horizontal_lines, vertical_lines, image_shape, border_threshold=10):
    height, width = image_shape[:2]
    filtered_horizontal_lines = []
    filtered_vertical_lines = []

    for line in horizontal_lines:
        x1, y1, x2, y2 = line
        if (
            y1 > border_threshold and y2 > border_threshold and  # Not near top
            y1 < height - border_threshold and y2 < height - border_threshold  # Not near bottom
        ):
            filtered_horizontal_lines.append(line)

    for line in vertical_lines:
        x1, y1, x2, y2 = line
        if (
            x1 > border_threshold and x2 > border_threshold and  # Not near left
            x1 < width - border_threshold and x2 < width - border_threshold  # Not near right
        ):
            filtered_vertical_lines.append(line)

    return filtered_horizontal_lines, filtered_vertical_lines

def get_axes(horizontal_lines, vertical_lines):
    x_axis, y_axis = None, None
    if horizontal_lines:
        x_axis = max(horizontal_lines, key=lambda line: line[2] - line[0])
    if vertical_lines:
        y_axis = max(vertical_lines, key=lambda line: line[3] - line[1])

    return x_axis, y_axis

def find_intersection(x_axis, y_axis):
    if x_axis is None or y_axis is None:
        return None

    x1, y1, x2, y2 = x_axis
    x3, y3, x4, y4 = y_axis

    # Solve system of equations for line intersection
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    # Calculate intersection point
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator

    return int(px), int(py)

def draw_axes_and_origin(original_image, x_axis, y_axis, origin):
    if x_axis is not None:
        cv2.line(original_image, (x_axis[0], x_axis[1]), (x_axis[2], x_axis[3]), (0, 255, 0), 2)
    if y_axis is not None:
        cv2.line(original_image, (y_axis[0], y_axis[1]), (y_axis[2], y_axis[3]), (0, 255, 0), 2)
    if origin is not None:
        cv2.circle(original_image, origin, 5, (0, 0, 255), -1)
        cv2.putText(original_image, "Origin", (origin[0] + 5, origin[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)