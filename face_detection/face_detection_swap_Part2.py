# -*- coding: utf-8 -*-
# Eric Malavenda
# [P3] Project 3: HaarCascade Classifiers & Face Detection with Python 2.7 + OpenCV 3.1
# A "face-swapping" application
# [CS-4475-A] Professor: Dr. Maria Hybinette

import cv2
import numpy as np
import math

from face_detection_swap_Part1 import box_faces, new_faces, face_2_replace, swap_faces


def box_faces2(image, img):
    face_cascade = cv2.CascadeClassifier('C:/Users/Admin/CS-ComputationalPhoto/'
                                         'image_manipulation-face_detection/venv/Lib/site-packages/'
                                         'cv2/data/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    index = 0
    roi_color_array = []
    roi_color_array1 = []
    roi_color_array2 = []
    roi_color_array3 = []
    for (x, y, w, h) in face:
        # (a, b) is the center of your mask:
        # Resource: http://stackoverflow.com/questions/8647024/how-to-apply-a-disc-shaped-mask-to-a-numpy-array
        # stackoverflow poster source: Bi Rico, answered Dec 28 '11 at 0:41
        rectangular_face = cv2.rectangle(img, (x, y), (x+w, y+h), (1, 0, 0), 2, -1)
        # cv2.rectangle(image,(top-left corner),(bottom-right corner)
        '''        
        a = x+(w/2)
        b = y+(h/2)
        r = w/2
        
        From the following resource: http://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html: 
        "To draw the ellipse, we need to pass several arguments. One argument is the center location (x,y). 
        Next argument is axes lengths (major axis length, minor axis length). angle is the angle of rotation 
        of ellipse in anti-clockwise direction. startAngle and endAngle denotes the starting and ending of 
        ellipse arc measured in clockwise direction from major axis. i.e. giving values 0 and 360 gives the 
        full ellipse. For more details, check the documentation of cv2.ellipse(). Below example draws a half 
        ellipse at the center of the image."
        '''
        bg_elliptical_face = cv2.ellipse(image, (math.floor(x+(w/2)), math.floor(y+(h/2))),
                                         (math.floor(h/3), math.floor(w/2)), 0, 0, 360, 1, -1)
        # reference for cv2.ellipse() function params:
        # http://docs.opencv.org/3.2.0/dc/da5/tutorial_py_drawing_functions.html                   
        # (1) image = png image varname
        # (2) (x+(w/2),y+(h/2)) = x,y coordinates of ellipse's center
        # (3) (h/3,w/2) = major axis length, minor axis length
        # (4) 0 = angle of rotation of ellipse in anti-clockwise direction
        # (5) (0,360) = (start,end) of ellipse arc measured clockwise from major axis
        # (6) ...
        no_face = cv2.subtract(rectangular_face, bg_elliptical_face)
        # no_face = cv2.subtract(image.copy(), new_face)
        # cv2.circle(image,(a,b),r,(0,0,255),0)
        roi = no_face[y:y+h, x:x+w]
        roi_color_array.append(no_face)
        roi_color_array1.append(roi)
        roi_color_array2.append(no_face)
        roi_color_array3.append(bg_elliptical_face)
        index += 1
    return roi_color_array, roi_color_array1, roi_color_array2, roi_color_array3


def add_rois(image, array):
    image_copy = image.copy()
    rows, cols, channels = image_copy.shape
    i = 0
    no_face_image = image_copy[0:rows, 0:cols]
    for im in range(len(array)):
        no_face_image = array[i]
        i += 1    
    return no_face_image


def new_faces_image(array):
    index = 0
    h, w = array[index].shape[:2]
    fname = []
    for face in array:
        file_name = cv2.resize(array[index], (w, h), interpolation=cv2.INTER_LANCZOS4)
        fname.append(file_name)
        index += 1
    return fname[len(fname) - 1]


def main():
    image = cv2.imread('C:/Users/Admin/CS-ComputationalPhoto/image_manipulation-face_detection/'
                       'hillary-clinton-donald-trump-mike-bloomberg.png')
    roi_color_array, roi_color_array2, roi_color_array3 = box_faces(image)
    # fname = write2file(roi_color_array)
    new_face_array, new_faces_copy = new_faces(image, roi_color_array2)
    face2replace_array, face_2_replace_copy = face_2_replace(image, new_face_array, roi_color_array3)
    merged_image = swap_faces(image, new_face_array, face2replace_array, face_2_replace_copy)
    cv2.imshow('merged_image', merged_image)
    cv2.imwrite('merged_image.png', merged_image)
    image = cv2.imread('C:/Users/Admin/CS-ComputationalPhoto/image_manipulation-face_detection/'
                       'hillary-clinton-donald-trump-mike-bloomberg.png')
    img = cv2.imread('merged_image.png')
    roi_color_array, roi_color_array1, roi_color_array2, roi_color_array3 = box_faces2(image, img)
    no_face_image = add_rois(image, roi_color_array3)
    cv2.imwrite('no_face_image.png', no_face_image)
    new_face_image = new_faces_image(roi_color_array)
    rows, cols, channels = new_face_image.shape
    fg_img = no_face_image[0:rows, 0:cols]
    subject_region_roi_0 = cv2.subtract(new_face_image, fg_img)
    for x in range(0, 10):  # to soften the edges of each face and reduce contrast with remaining image
        subject_region_roi_0 = cv2.subtract(subject_region_roi_0, fg_img)
        x += 1
    subject_region_roi = subject_region_roi_0
    cv2.imwrite('new_face_image.png', subject_region_roi)
    merged_image = cv2.addWeighted(no_face_image, 0.5, subject_region_roi, 0.5, 0)
    merged_image_final = cv2.add(merged_image, merged_image.copy())
    cv2.namedWindow('merged_image_final', cv2.WINDOW_NORMAL)
    cv2.imshow('merged_image_final', merged_image_final)
    cv2.imwrite('merged_image_final.png', merged_image_final)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
