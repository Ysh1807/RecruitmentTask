import cv2
import numpy as np
import glob

# Save all the unstitched images in a folder and use glob module to save all the images paths to a list
imgPath = glob.glob('Test1/*.jpg')

# Creating a list for unstitched images
images = []

# Retrieving the images from imgPath list and appending to the images list
n = 0
for img in imgPath:
    image = cv2.imread(img)
    imgResize = cv2.resize(image, (600, 400))
    images.append(imgResize)
    n += 1
    cv2.imshow(f'Image {n}', imgResize)     # Showing images to be stitched one by one
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Creating a stitcher object
imageStitcher = cv2.Stitcher_create()

# Passing the image list to the stitcher for stitching
error, stitchedImage = imageStitcher.stitch(images)

# If no error faced, write the stitched image and display it.
if not error:
    finalImage = cv2.resize(stitchedImage, (1000,500))
    cv2.imwrite("Output.png", finalImage)
    cv2.imshow('Output', finalImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Printing an error message, if error faced
else:
    print("No matching descriptors found")