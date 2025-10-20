# checker.py
import cv2
import numpy as np

# Load the image from the folder
# The script will look for an image named 'sugarcane.jpg' in the same folder
image_path = 'sugarcane-3.jpg'
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Could not load image at {image_path}")
    exit()

# Convert the original image from BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the color range for UNRIPE (green)
# These values might need tuning for your specific images
unripe_lower = np.array([35, 40, 40])
unripe_upper = np.array([85, 255, 255])

# Define the color range for RIPE (yellow/brown)
ripe_lower = np.array([10, 100, 20])
ripe_upper = np.array([30, 255, 255])

# Create a mask for each color range
unripe_mask = cv2.inRange(hsv_image, unripe_lower, unripe_upper)
ripe_mask = cv2.inRange(hsv_image, ripe_lower, ripe_upper)

# Count the number of non-zero (white) pixels in each mask
unripe_pixels = cv2.countNonZero(unripe_mask)
ripe_pixels = cv2.countNonZero(ripe_mask)

# Calculate the total relevant pixels
total_pixels = unripe_pixels + ripe_pixels

# Avoid division by zero if no relevant colors are found
if total_pixels > 0:
    ripeness_percentage = (ripe_pixels / total_pixels) * 100
else:
    ripeness_percentage = 0

# --- Displaying the Final Output ---
print("--- Sugarcane Ripeness Analysis ---")
print(f"Unripe (Green) Pixel Count: {unripe_pixels}")
print(f"Ripe (Yellow/Brown) Pixel Count: {ripe_pixels}")
print(f"Estimated Ripeness: {ripeness_percentage:.2f}%")

# Display the images to see what the script is doing (optional but helpful)
cv2.imshow('Original Image', image)
cv2.imshow('Ripe Mask (White areas)', ripe_mask)
cv2.imshow('Unripe Mask (White areas)', unripe_mask)

# Wait for the user to press a key to close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()