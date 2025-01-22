import cv2
import numpy as np

subject_img = cv2.imread("prop_images/cropped.png")  # Image to be aligned.
ref_img = cv2.imread("prop_images/ref.png")    # Reference image.

# Greyscale images
subject_gray = cv2.cvtColor(subject_img, cv2.COLOR_BGR2GRAY)
ref_gray = cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY)
height, width = ref_gray.shape

# Orbs are used for point detection
orb_detector = cv2.ORB_create(5000)

# get key points and descriptors from both images
key_points_subject, descriptors_subject = orb_detector.detectAndCompute(subject_gray, None)
key_points_ref, descriptors_ref = orb_detector.detectAndCompute(ref_gray, None)

# matcher object used by opencv to find minimum distance orientation between the two sets of descriptors
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

# perform matching
matches = matcher.match(descriptors_subject, descriptors_ref)

# Distance here is the avg distance between desciptors in the match
# get the lowest distance (best match)
matches = sorted(matches, key = lambda x: x.distance)

# Take the top 90 % matches
matches = matches[:int(len(matches)*0.9)]
no_of_matches = len(matches)




# Define empty matrices of shape no_of_matches * 2.
p1 = np.zeros((no_of_matches, 2))
p2 = np.zeros((no_of_matches, 2))

for i in range(len(matches)):
  p1[i, :] = key_points_subject[matches[i].queryIdx].pt
  p2[i, :] = key_points_ref[matches[i].trainIdx].pt

# Find the homography matrix.
homography, mask = cv2.findHomography(p1, p2, cv2.RANSAC)

# Use this matrix to transform the
# colored image wrt the reference image.
transformed_img = cv2.warpPerspective(subject_img,
                    homography, (width, height))

# Save the output.
cv2.imwrite('output.jpg', transformed_img)
