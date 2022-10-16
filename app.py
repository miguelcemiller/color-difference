import cv2
import numpy as np
import colour

IMG_SIZE = (200,200)
img_A_path = 'images/leaf-1.jpg'
img_B_path = 'images/2.jpg'

# Read img_A and img_B and convert to float
img_A = cv2.imread(img_A_path).astype("float32") / 255
img_B = cv2.imread(img_B_path).astype("float32") / 255

# Resize 
img_A = cv2.resize(img_A, IMG_SIZE)
img_B = cv2.resize(img_B, IMG_SIZE)

# Convert image_A and image_B from BGR to LAB
img_A = cv2.cvtColor(img_A,cv2.COLOR_BGR2LAB) 
img_B = cv2.cvtColor(img_B,cv2.COLOR_BGR2LAB)

# Calculate Delta-E
delta_E = np.mean(colour.delta_E(img_A, img_B))
print("Delta-E: ", delta_E)