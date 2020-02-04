# -*- coding: utf-8 -*-

"""
Created on Wed Jun 08 00:59:39 2016

@author: Eric Malavenda

[CS-4475-A] Homework 2
"""

# Acknowledgements:
# CS-4475-A, CS-6475-A / Summer 2016 
# [Professor] Dr. Marie Hybinette@Georgia Institute of Technology & @University of Georgia
# Assignment and assignment code framework creators:
# Dr. Jay Summet & Dr. Irfan Essa@Georgia Institute of Technology
# Original assignment URL:
# http://cobweb.cs.uga.edu/~maria/classes/2016-CompPhoto/H2-Blend.html

import cv2 
import numpy as np

"""
1. Read in all images you need into an array []. 
1a. Use the 0 index as the 'background image'. 
1b. Consider scaling (the provided) images by cv2.resize() by a factor of 0.12
    of their height and width so they fit on the screen when displayed.
""" 

## 1.

def getimagesarray(array,factor):
    index=0
    images_d = []
    for image in array:
        cv2img = cv2.imread(fname[index])
        height, width = cv2img.shape[:2]
        cv2img_sz = cv2.resize(cv2img,( int(factor*width), int(factor*height)), interpolation = cv2.INTER_AREA ) 
        images_d.append(cv2img_sz)           
        index +=1
    return images_d

"""
2. Iterate over the array of images. For each image:
2a. Create two 'masks' fgmask, and bgmask (bgmask is the inverse of fgmask).
2b. fgmask masks out the 'difference' of the fgmask (hopefully the subject). 
2c. fgmask: highlights subject in foreground image. (normal mask)
2d. bgmask: black out area in background image to exclude the subject. (inverse mask).
"""
     
# 2c.    
def image_operations(array,arraynames):
    index=1
    canvas_array = []
    for image in range(index, len(array)):
        bg_img = array[0]
        fg_img = array[index]
        rows,cols,channels = fg_img.shape
        cv2.imshow('background image', bg_img)
        cv2.waitKey(0)
        roi = bg_img[0:rows, 0:cols]
        #cv2.imshow('roi', roi)
        #cv2.waitKey(0)
        # Create a mask of component and also create its inverse mask
        bg_img2gray = cv2.cvtColor(bg_img,cv2.COLOR_BGR2GRAY)
        fg_img2gray = cv2.cvtColor(fg_img,cv2.COLOR_BGR2GRAY)
        new = cv2.subtract( fg_img2gray, bg_img2gray )
        ret, fgmask = cv2.threshold(new, 0, 255, cv2.THRESH_BINARY)
        #cv2.imshow('fgmask',fgmask)
        #cv2.waitKey(0)
        fgmask_inv = cv2.bitwise_not(fgmask)
        bgmask = fgmask_inv
        #cv2.imshow('bgmask',bgmask)
        #cv2.waitKey(0)
        # Black-out area of component in roi
        subject_region_black_roi = cv2.bitwise_and(roi,roi,mask = fgmask)
        cv2.imshow('bg', subject_region_black_roi)  
        cv2.waitKey(0)
        # Take only region of component from component image.
        subject_region_visible_fg = cv2.bitwise_and(fg_img,fg_img,mask = bgmask)
        cv2.imshow('fg', subject_region_visible_fg)
        cv2.waitKey(0)        
        # Place component in roi and update main image
        canvas_img = cv2.add(subject_region_black_roi, subject_region_visible_fg)
        bg_img[0:rows, 0:cols ] = canvas_img
        #cv2.imshow('res',bg_img)
        #cv2.waitKey(0) 
        canvas_array.append(bg_img)
        index += 1
    return canvas_array
    
## 1a. Background image is used as array[0] image:

fname = [
    'background.png',
    'component01.png', 
    'component02.png',
    'component03.png'] 

INDEX = 0

## 1.
## 1a.
## 1b. Scaling images by cv2.resize() by a factor of 0.25: 
images_d2 = np.array(getimagesarray(fname,0.25))

# 2.
# 2a.
# 2b.
result = np.array(image_operations(images_d2,fname))
##final_composite_img = add_for_composite(result)

# 2c.

cv2.imshow('composite0', result[INDEX])
cv2.imwrite('composite0.png', result[INDEX])
cv2.waitKey(0)

cv2.destroyAllWindows()

###########################################################################################################################################################
###########################################################################################################################################################

def instructor_getimagesarray(array,factor):
    I_D = 0
    instructor_images_d = []
    for image in array:
        cv2img = cv2.imread(fname_instructor[I_D])
        height, width = cv2img.shape[:2]
        cv2img_sz = cv2.resize(cv2img,( int(factor*width), int(factor*height)), interpolation = cv2.INTER_AREA ) 
        instructor_images_d.append(cv2img_sz)           
        I_D += 1
    return instructor_images_d

"""
2. Iterate over the array of images. For each image:
2a. Create two 'masks' fgmask, and bgmask (bgmask is the inverse of fgmask).
2b. fgmask masks out the 'difference' of the fgmask (hopefully the subject). 
2c. fgmask: highlights subject in foreground image. (normal mask)
2d. bgmask: black out area in background image to exclude the subject. (inverse mask).
"""
     
## 2c.    
def instructor_image_operations(array,arraynames):
    index=1
    canvas_arr = []
    for image in range(index, len(array)):
        bg_img = array[0]
        fg_img = array[index]
        rows,cols,channels = fg_img.shape
        cv2.imshow('background image', bg_img)
        cv2.waitKey(0)
        roi = bg_img[0:rows, 0:cols]
        #cv2.imshow('roi', roi)
        #cv2.waitKey(0)
        # Create a mask of component and also create its inverse mask
        bg_img2gray = cv2.cvtColor(bg_img,cv2.COLOR_BGR2GRAY)
        fg_img2gray = cv2.cvtColor(fg_img,cv2.COLOR_BGR2GRAY)
        new = cv2.subtract( fg_img2gray, bg_img2gray )
        ret, fgmask = cv2.threshold(new, 0, 255, cv2.THRESH_BINARY)
        #cv2.imshow('fgmask',fgmask)
        #cv2.waitKey(0)
        fgmask_inv = cv2.bitwise_not(fgmask)
        bgmask = fgmask_inv
        #cv2.imshow('bgmask',bgmask)
        #cv2.waitKey(0)
        # Black-out area of component in roi
        subject_region_black_roi = cv2.bitwise_and(roi,roi,mask = bgmask)
        cv2.imshow('bg', subject_region_black_roi)  
        cv2.waitKey(0)
        # Take only region of component from component image.
        subject_region_visible_fg = cv2.bitwise_and(fg_img,fg_img,mask = fgmask)
        cv2.imshow('fg', subject_region_visible_fg)
        cv2.waitKey(0)        
        # Place component in roi and update main image
        canvas_img2 = cv2.bitwise_or(subject_region_black_roi, subject_region_visible_fg)
        bg_img[0:rows, 0:cols ] = canvas_img2
        #cv2.imshow('res',bg_img)
        #cv2.waitKey(0) 
        canvas_arr.append(bg_img)
        index += 1
    return canvas_arr
    
## 1a. Background image is used as array[0] image:

fname_instructor = [
    '00.jpg',
    '01.jpg', 
    '02.jpg',
    '03.jpg',
    '04.jpg',
    '05.jpg',
    '06.jpg',
    '07.jpg',
    '08.jpg',
    '09.jpg'] 

IND = 0

## 1.
## 1a.
## 1b. Scaling images by cv2.resize() by a factor of 0.12: 
instructor_images_d2 = np.array(instructor_getimagesarray(fname_instructor,0.12))

# 2.
# 2a.
# 2b.
result2 = np.array(instructor_image_operations(instructor_images_d2,fname_instructor))

# 2c.

cv2.imshow('composite1', result2[IND])
cv2.imwrite('composite1.jpg', result2[IND])
cv2.waitKey(0)

cv2.destroyAllWindows()
