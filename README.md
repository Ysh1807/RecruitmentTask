# UAS SOFTWARE Recruitment Task ROUND 2 

# TASK - 1
IMAGE MOSAICING

The task for us was to build a stitched image from a given sequence of provided images
(around 10) into a seamless mosaic.
For testing purposes, we can either take a series of images that are in a sequential order,
or you can extract frames from a video.

STATUS :- COMPLETE :)

# WORKFLOW OF MY PROGRAM
1. Save all the unstitched images in a folder and use glob module to save all the images paths to a list (imgPath)
2. Creating a list for unstitched images.
3. Retrieving the images from imgPath list and appending to the images list.
4. Create a stitcher object and pass the image list to the stitcher for stitching.
5. If no error is faced, write the stitched image and display it else display the error message.

# TASK - 2
IMAGE SEGMENTATION

We need to build a software system which detects a RED arrow in a
video feed captured by the web camera and prints the angle of its heading with respect to
the vertical axis of the image. The system should work in varying backgrounds and varying
lighting conditions.

STATUS :- INCOMPLETE :(

# WHAT CAN MY PROGRAM DO?
It can detect a red arrow quite accurately and won't detect other coloured arrows.

# PROBLEMS WITH MY CODE
1. It will detect other 7 sided closed shapes like heptagon.
2. It can't tell the direction (angle) from the vertical axis as was asked in the task.
