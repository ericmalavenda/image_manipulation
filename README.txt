# image_manipulation
# Computer Vision & Image Manipulation with Python 2.7 + OpenCV 3.1
# Eric Malavenda
# [CS-4475-A] Professor: Dr. Maria Hybinette
# Georgia Institute of Technology

Feature Detection and Matching with SIFT algorithm in OpenCV 3.1 Implemented with Python 2.7
# Link to Portfolio and to view project-corresponding images: 
# https://eric-malavenda.myportfolio.com/feature-matching-with-sift

def findMatchesBetweenImages(image_1, image_2): 
# “Return the top 10 list of matches between two input images.” 
# “This function detects and computes SIFT (or ORB) from the input images, and 
# returns the best matches using the normalized Hamming Distance.” 
# Referenced URL: http://opencv-python-
# tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html 

# Reason for needing the pre-ORB execution line of code below [line#106 before ORB 
# execution (as SIFT) on line#107] is provided as a bug workaround, in accordance with the #following issue reported in the OpenCV GitHub repo here: 
# https://github.com/opencv/opencv/issues/6081. 
cv2.ocl.setUseOpenCL(False) 
sift = SIFT() 
# 1. “Compute SIFT keypoints and descriptors for both images.” 
image_1_kp, image_1_desc = sift.detectAndCompute(image_1,None) 
image_2_kp, image_2_desc = sift.detectAndCompute(image_2,None) 
# 2. “Create a Brute Force Matcher, using the hamming distance (and set crossCheck to true).” 
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True) 
# 3. “Compute the matches between both images.” 
matches = bf.match(image_1_desc,image_2_desc) 
# 4. Sort the matches based on distance so you get the best matches. 
matches = sorted(matches, key = lambda x:x.distance) 
# 5. Return the image_1 keypoints, image_2 keypoints, and the top 10 matches in 
# a list. 
matches = matches[:10] 
# “return” statement is given 
return image_1_kp, image_2_kp, matches 
# END OF FUNCTION. 

Assignment Question 3. For each of the four images (sample, lighting, scale, rotation), explain the following:

Sample Image:

(1.Q) How many features does your algorithm get correctly? Why do you think it gets some of the errors it gets?
(1.A) Most features were detected accurately for this instance of running the code. Feature detection algorithm 
     yielded nearly 100% accuracy.

(2.Q) Did you try taking the picture multiple times to try and improve results? What did you do to make this work?
(2.A) I took three pictures prior to using including the output below, generated when using the input image I 
      selected for the template-image/sample-image feature detection trial. Made sure to resize the image prior 
      to running the code so both images were 375 X 375 pixels@72-bit resolution. 

(3.Q) Give output result for the “Sample” image that shows the matches.
(3.A) i. Result when using provided images (“Sample” instance): 
      ii. Result when using my images (“Sample” instance):
      https://eric-malavenda.myportfolio.com/feature-matching-with-sift
      (*Click on URL above and scroll down to corresponding image*)
      
Lighting Image: 

(1.Q) How many features does your algorithm get correctly? Why do you think it gets some of the errors it gets?
(1.A) This instance generated feature detection that was accurately portrayed for some of the facial features of 
      the figurine, but limited for other areas of the figurine. I believe the reason for the limited feature detection 
      capability of my algorithm during this instance of running the code was both the low lighting, and the greater 
      distance away from the figurine and above the figurine that I was positioned relative to Stewie when capturing the image. 

(2.Q) Did you try taking the picture multiple times to try and improve results? What did you do to make this work?:
(2.A) I took two photos prior to selecting the output provided below for this part of the assignment. Made sure to 
      resize the image prior to running the code so both images were 375 X 375 pixels@72-bit resolution. 

(3.Q) Give output result for the “Lighting” image that shows the matches.
(3.A) Result when using provided images (“Lighting” instance): 
      i. Result when using provided images (“Lighting” instance): 
      ii. Result when using my images (“Lighting” instance):
      https://eric-malavenda.myportfolio.com/feature-matching-with-sift
      (*Click on URL above and scroll down to corresponding image*)
      
Scale Image: 

(1.Q) How many features does your algorithm get correctly? Why do you think it gets some of the errors it gets?:
(1.A) I had more of an issue with this feature detection instance than with the other instances used for this assignment. 
      I believe the algorithm was able to pick up on fewer feature matches due to my decision to capture images on a desk
      having a color similar to the Stewie figurine’s clothing, as well as being due to my decision to scale the figurine 
      down in size by stepping back and away from the figurine compared to my original (template) image.
      
(2.Q) Did you try taking the picture multiple times to try and improve results? What did you do to make this work?:
(2.A) I took four pictures prior to running the code for this particular image and settling with the output of running 
      that code. Results would have likely improved if I was closer to the figurine when taking the “Scale” trial photo, 
      and directly in front instead of above and at an angle relative to the figurine. Made sure to resize the image 
      prior to running the code so both images were 375 X 375 pixels@72-bit resolution. 
      
(3.Q) Give output result for the “Scale” image that shows the matches.
(3.A) Result when using provided images (“Scale” instance): 
      i. Result when using provided images (“Scale” instance): 
      ii. Result when using my images (“Scale” instance):
      https://eric-malavenda.myportfolio.com/feature-matching-with-sift
      (*Click on URL above and scroll down to corresponding image*)
      
Rotation Image: 

(1.Q) How many features does your algorithm get correctly? Why do you think it gets some of the errors it gets?:
(1.A) Most features were detected correctly for my images and the rotation instance of running my code. 
      There were a few missed features detected as matching between the template and rotated images, and 
      this was likely due to the figurine being inverted 180 degrees when taking the pictures eventually 
      processed by my algorithm. 

(2.Q) Did you try taking the picture multiple times to try and improve results? What did you do to make this work?:
(2.A) Worked well on the first running of the code. Made sure to resize the image prior to running the code so that 
      the image was equal in size to my template image: 375 X 375 pixels@72-bit resolution. 

(3.Q) Give output result for the “Rotation” image that shows the matches.
(3.A) Result when using provided images (“Rotation” instance): 
      i. Result when using provided images (“Rotation” instance): 
      ii. Result when using my images (“Rotation” instance):
      https://eric-malavenda.myportfolio.com/feature-matching-with-sift
      (*Click on URL above and scroll down to corresponding image*)
