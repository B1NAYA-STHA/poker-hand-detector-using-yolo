import cv2 as cv

def show_hand(frame, text, font=cv.FONT_HERSHEY_SIMPLEX, font_scale=0.8, font_thickness=2, padding=10):
    # Text size
    text_size, _ = cv.getTextSize(text, font, font_scale, font_thickness)
    text_width, text_height = text_size

    # Coordinates
    x = padding
    y = text_height + padding

    # Background box coordinates
    box_coords = ((x - 5, y - text_height - 5), (x + text_width + 5, y + 5))
    
    # Draw background rectangle (black with transparency)
    overlay = frame.copy()
    cv.rectangle(overlay, box_coords[0], box_coords[1], (0, 0, 0), -1)
    alpha = 0.6  # Transparency
    cv.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    # Draw the text (white)
    cv.putText(frame, text, (x, y), font, font_scale, (255, 255, 255), font_thickness, cv.LINE_AA)
    
    return frame

def draw_label(frame, text, x, y, color=(0, 255, 0)):
    font = cv.FONT_HERSHEY_SIMPLEX
    scale = 0.6
    thickness = 2
    
    # Get text size for background rectangle
    (w, h), _ = cv.getTextSize(text, font, scale, thickness)
    
    # Draw filled rectangle as label background slightly above the point (x, y)
    cv.rectangle(frame, (x, y - h - 10), (x + w + 10, y), color, -1)
    
    # Put text on top of the rectangle with black color for good contrast
    cv.putText(frame, text, (x + 5, y - 5), font, scale, (0, 0, 0), thickness, cv.LINE_AA)

