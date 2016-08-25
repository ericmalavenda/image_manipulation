# Malavenda, Eric
# [CS-4475-A] Instructor: Dr. Maria Hybinette
# Project 1 [P1]: Computational Photography & Non-Photorealistic Rendering

# "Filtering is the fundamental operation in image and video processing. 
# Edge-preserving smoothing filters are used in many different applications" 

import cv2
import numpy as np

# Beyeler, M. (2O15) OpenCV with Python Blueprints
# Referenced from urls:
# 1. http://docs.opencv.org/master/df/dac/group__photo__render.html#gsc.tab=0
# 2. http://www.learnopencv.com/non-photorealistic-rendering-using-opencv-python-c/
# 3. http://www.askaswiss.com/2016/01/how-to-create-pencil-sketch-opencv-python.html
# 
image1 = 'Original_GT Dad + Me.png'
img1 = cv2.imread(image1)
# Upload image...

(height, width) = img1.shape[:2]

# Height and width of pencilsketch canvas will 
# default to height and width of each corresponding imported image, and set 
# prior to image processing, unless height or width of imported image is larger
# than the pencilsketch canvas. If larger than the pencil sketch canvas,
# imported image will pass through the conditional statement below and be scaled
# down to more workable dimensions. 

image2 = 'pencilsketch_bg_canvas.png' # used for imported-image size standardization
img2 = cv2.imread(image2)
# Upload image...

(h, w) = img2.shape[:2]

if ((height > h) | (width > w)):
    height_threshold = height * 0.10
    width_threshold = width * 0.10  
    img1_rszd = cv2.resize(img1,( int(width_threshold), int(height_threshold)), 
                          interpolation = cv2.INTER_AREA ) 
    img2_rszd = cv2.resize(img2,( int(width_threshold), int(height_threshold)), 
                          interpolation = cv2.INTER_AREA ) 
else:
    img1_rszd = cv2.resize(img1,( int(width), int(height)), interpolation
    = cv2.INTER_AREA ) 
    img2_rszd = cv2.resize(img2,( int(width), int(height)), interpolation
    = cv2.INTER_AREA ) 
              
###############################################################################
#Pencil Sketch Filter (pencilSketch)
# "Out-of-the-box" in OpenCV 3.0                
img_pencilSketch_gray, img_pencilSketch_color = cv2.pencilSketch(img1_rszd,
                                sigma_s=60, sigma_r=0.07, shade_factor=0.05)
# Outputs a non-colorized as well as a colorized image that appears to
# to be a sketch of the original image. Quality appears to be lacking for each 
# image. Even when adjusting the shade factor parameter, the filtered image never
# correctly communicated the facial expressions of the subjects in the original
# images, except for the Mona Lisa image, although this was a non-photorealistic
# image prior to import which affected the outcome.
cv2.imshow('Gray Pencil Sketch', img_pencilSketch_gray)
cv2.imwrite('Gray_Pencil_Sketch.png', img_pencilSketch_gray)
cv2.waitKey(0)

cv2.imshow('color pencil sketch', img_pencilSketch_color)
cv2.imwrite('Color_Pencil_Sketch.png', img_pencilSketch_color)
cv2.waitKey(0)

# An attempt to improve output image quality by implementing use of the 
# edge preserving filter, prior to processing with the pencilSketch() function,
# yielded an unsuccessful result.
_img_copy_ = img1_rszd.copy()
#img_edges_preserved = cv2.edgePreservingFilter(_img_copy_, flags=1, sigma_s=60, 
#                                              sigma_r=0.4)
_img_enhanced_ = cv2.detailEnhance(_img_copy_, sigma_s=10, sigma_r=0.15)
penSk_edgeP, penSk_color_edgeP = cv2.pencilSketch(_img_enhanced_, 
                                                  sigma_s=60, sigma_r=0.07, 
                                                  shade_factor=0.05)
                                
cv2.imshow('Pencil edgePreserved Sketch', penSk_edgeP)
cv2.imwrite('Pencil_Edge_Preserved_Sketch.png', penSk_edgeP)
cv2.waitKey(0)

cv2.imshow('color edgePreserved pencil sketch', penSk_color_edgeP)
cv2.imwrite('Color_Pencil_Edge_Preserved_Sketch.png', penSk_color_edgeP)
cv2.waitKey(0)
###############################################################################
img_copy = img1_rszd.copy()
img_stylized = cv2.stylization(img_copy, sigma_s=60, sigma_r=0.07)
cv2.imshow('Watercolor Sketch_Stylization', img_stylized)
cv2.imwrite('Watercolor_Sketch_Stylization.png', img_stylized)
cv2.waitKey(0)

img_copy = img1_rszd.copy()
img_stylized = cv2.stylization(img_copy, sigma_s=60, sigma_r=0.07)
img_hsv = cv2.cvtColor(img_stylized, cv2.COLOR_BGR2HSV)
cv2.imshow('Watercolor Sketch_Stylization_HSV', img_hsv)
cv2.imwrite('Watercolor_Sketch_Stylization_HSV.png', img_hsv)
cv2.waitKey(0)

img_copy_ = img1_rszd.copy()
# img_enhanced_ = cv2.detailEnhance(img_copy_, sigma_s=10, sigma_r=0.15)
# img_edgesPreserved = cv2.edgePreservingFilter(img_copy_, flags=1, sigma_s=60, 
#                                              sigma_r=0.4)
# Better result achieved with bilateral filter followed by stylization.
# Both the detail enhance and edge preservation filters were attemtpted prior
# to stylization function implementation, but result was better when using 
# bilateral filter function with the stylization function. Smoother resulting image
# when compared to use of stylization function alone.
img_bilateral = cv2.bilateralFilter(img_copy_, 9, 75, 75)
img_stylized_bilateral = cv2.stylization(img_bilateral, sigma_s=60, sigma_r=0.07)

cv2.imshow('Watercolor Sketch_Bilateral Filter+Stylized', img_stylized_bilateral)
cv2.imwrite('Watercolor_Sketch_Bilateral Filter+Stylized.png', img_stylized_bilateral)
cv2.waitKey(0) 
###############################################################################
#Detail Enhancing Filter ( detailEnhance )
img_copy2 = img1_rszd.copy()
img_enhanced = cv2.detailEnhance(img_copy2, sigma_s=10, sigma_r=0.15)

cv2.imshow('Enhanced Image', img_enhanced)
cv2.imwrite('Enhanced_Image.png', img_enhanced)
cv2.waitKey(0)
###############################################################################
#Edge Preserving Filter ( edgePreservingFilter )
img_copy3 = img1_rszd.copy()
img_edgesPreserved = cv2.edgePreservingFilter(img_copy3, flags=1, sigma_s=60, 
                                              sigma_r=0.4)

cv2.imshow('Edge Preserved Image', img_edgesPreserved)
cv2.imwrite('Edge_Preserved_Image.png', img_edgesPreserved)
cv2.waitKey(0)
###############################################################################
# http://www.askaswiss.com/2016/01/how-to-create-pencil-sketch-opencv-python.html
# Enhanced Pencil Sketch Technique (not built-in cv2.pencilSketch function)
img_copy4 = img1_rszd.copy()

img_gray = cv2.cvtColor(img_copy4, cv2.COLOR_BGR2GRAY)
img_gray_inv = 255 - img_gray
img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(21, 21), sigmaX=0, sigmaY=0)

def dodgeV2(image, mask):
  return cv2.divide(image, 255-mask, scale=256)
def burnV2(image, mask):
  return 255-cv2.divide(255-image, 255-mask, scale=256)
  
img_blend_dodge = dodgeV2(img_gray, img_blur)
cv2.imshow('Pencil Sketch Image with Dodge', img_blend_dodge) # with dodgeV2 
# function applied
cv2.imwrite('Pencil_Sketch_Image_Dodge.png', img_blend_dodge)
cv2.waitKey(0)

img_blend_dodge_burn = burnV2(img_blend_dodge, img_blur)
cv2.imshow('Pencil Sketch Image with Dodge + Burn', img_blend_dodge_burn) 
# with both dodgeV2 & burnV2 functions applied
cv2.imwrite('Pencil_Sketch_Image_Dodge + Burn.png', img_blend_dodge_burn)
cv2.waitKey(0)
#img_blend = cv2.multiply(img_blend, img2, scale=1/256)
# Was not able to implement the function above to obtain a compiled result
# Pencil sketch background image was effectively never used as a canvas 
# for this portion of the demo, due to complications with the function above's
# implementation.

imgPencilSketchDodge_copy = img_blend_dodge.copy() 
### dodge.copy() used for this implementation
imgPencilSketchDodge_copy_BGR = cv2.cvtColor(imgPencilSketchDodge_copy, 
                                 cv2.COLOR_GRAY2BGR)
imgPencilSketch_stylized = cv2.stylization(imgPencilSketchDodge_copy_BGR, 
                                           sigma_s=60, sigma_r=0.07)
### cv2.stylization() function used after conversion to grayscale of dodge.copy()

cv2.imshow('Stylized Pencil Sketch', imgPencilSketch_stylized)
cv2.imwrite('Stylized_Pencil_Sketch.png', imgPencilSketch_stylized)
cv2.waitKey(0)

###############################################################################
# Detail enhancing filter used prior to processing image with alternative 
# pencil sketch (non-built-in) algorithm from above demo.
img_copy5 = img1_rszd.copy()
img_enhanced_ = cv2.detailEnhance(img_copy5, sigma_s=10, sigma_r=0.15)

img_gray_enhanced = cv2.cvtColor(img_enhanced_, cv2.COLOR_BGR2GRAY)
img_gray_inv_enhanced = 255 - img_gray_enhanced
img_blur_enhanced = cv2.GaussianBlur(img_gray_inv_enhanced, ksize=(21, 21), 
                                     sigmaX=0, sigmaY=0)

img_blend_dodge_enhanced = dodgeV2(img_gray_enhanced, img_blur_enhanced)

cv2.imshow('Enhanced Pencil Sketch Image with Dodge', img_blend_dodge_enhanced) 
# with dodgeV2 function applied
cv2.imwrite('Enhanced_Pencil_Sketch_Image_Dodge.png', img_blend_dodge_enhanced)
cv2.waitKey(0)

img_blend_dodge_burn_enhanced = burnV2(img_blend_dodge_enhanced, img_blur_enhanced)
cv2.imshow('Enhanced Pencil Sketch Image with Dodge + Burn', 
           img_blend_dodge_burn_enhanced) # with dodgeV2 & burnV2 methods applied
cv2.imwrite('Enhanced_Pencil_Sketch_Image_Dodge + Burn.png', 
            img_blend_dodge_burn_enhanced)
cv2.waitKey(0)
###############################################################################
# Stylization (cartoonization) filter used prior to processing image with alternative 
# pencil sketch (non-built-in) algorithm from above demo.
# Better result from implementing detail enhance and stylization functions
# separately, when using one prior to processing image with alt-pencil sketch
# algorithm.
img_copy6 = img1_rszd.copy()

img_stylized_ = cv2.stylization(img_copy6, 
                                           sigma_s=60, sigma_r=0.07)
### cv2.stylization() function used prior to conversion to grayscale of 
### original_image.copy()

img_gray_stylized_ = cv2.cvtColor(img_stylized_, cv2.COLOR_BGR2GRAY)
img_gray_inv_stylized = 255 - img_gray_stylized_
img_blur_stylized = cv2.GaussianBlur(img_gray_inv_stylized, ksize=(21, 21), 
                                     sigmaX=0, sigmaY=0)

img_blend_dodge_stylized = dodgeV2(img_gray_stylized_, img_blur_stylized)

cv2.imshow('Stylized Pencil Sketch Image with Dodge', img_blend_dodge_stylized) 
# with dodgeV2 function applied
cv2.imwrite('Stylized_Pencil_Sketch_Image_Dodge.png', img_blend_dodge_stylized)
cv2.waitKey(0)

img_blend_dodge_burn_stylized = burnV2(img_blend_dodge_stylized, img_blur_stylized)
cv2.imshow('Stylized Pencil Sketch Image with Dodge + Burn', 
           img_blend_dodge_burn_stylized) # with dodgeV2 & burnV2 methods applied
cv2.imwrite('Stylized_Pencil_Sketch_Image_Dodge + Burn.png', 
            img_blend_dodge_burn_stylized)
cv2.waitKey(0)
###############################################################################
