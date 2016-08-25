# -*- coding: utf-8 -*-
# Eric Malavenda
# [P3] Project 3: HaarCascade Classifiers & Human/Cat Face/Body Feature Detection + Face/Facial Feature Swapping
# [CS-4475-A] Professor: Dr. Maria Hybinette

import cv2

def box_faces(image):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    index = 0
    roi_color_array = []
    roi_color_array2 = []
    roi_color_array3 = []
    for (x,y,w,h) in face:
        #roi_gray = gray[y:y+h, x:x+w]
        # line of code above is necessary if cascading through additional features on face
        roi_color = image[y:y+h, x:x+w]
        roi_color_array.append(roi_color)
        roi_color_array2.append(roi_color)
        #cv2.rectangle(roi_color,(x,y),(x+w,y+h),(255,0,0),2) 
        # line of code above makes (blue) rectangle around each face in image
        roi_color_array3.append(roi_color)# copy of roi_color_array
        index += 1
    return (roi_color_array, roi_color_array2, roi_color_array3)
    
def write2file(array):  
    index = 0
    h, w = array[index].shape[:2]
    fname = []
    for face in array:
        file_name_precursor = cv2.resize(array[index], ((w), (h)), interpolation = cv2.INTER_LANCZOS4)
        fileName = cv2.imwrite('roi_color' + str(index) + '.png', file_name_precursor)
        fname.append(fileName)
        index += 1
    return (fname)

def newFaces(image, roi_color_array2):
    newFaces_copy = image.copy()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(newFaces_copy, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    new_face_array = []
    index = 0
    for img in range(0, len(roi_color_array2)-1):
        for (x,y,w,h) in face:
            h_h, w_w = newFaces_copy[y:y+h, x:x+w].shape[:2]
            roi_color_array2_i = cv2.resize(roi_color_array2[index], ((w_w), (h_h)), interpolation = cv2.INTER_LANCZOS4)
            newFaces_copy[y:y+h, x:x+w] = roi_color_array2_i
            new_face = newFaces_copy[y:y+h, x:x+w]
            new_face_array.append(new_face)
            index += 1
        return new_face_array, newFaces_copy
        
def face_2_replace(image, new_face_array, roi_color_array3):
    face_2_replace_copy = image.copy()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(face_2_replace_copy, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    face2replace_array = []
    i = len(roi_color_array3)-1
    for img in range(0, len(new_face_array)-1):
        j = 0
        for img in range(0, len(roi_color_array3)-1):
            for (x,y,w,h) in face:
                _h_h_, _w_w_ = face_2_replace_copy[y:y+h, x:x+w].shape[:2]
                roi_color_array3_i = cv2.resize(roi_color_array3[i], ((_w_w_), (_h_h_)), interpolation = cv2.INTER_LANCZOS4)
                face_2_replace_copy[y:y+h, x:x+w] = roi_color_array3_i
                _face2replace_ = face_2_replace_copy[y:y+h, x:x+w]
                hh, ww = new_face_array[j].shape[:2]
                face2replace = cv2.resize(_face2replace_, ((ww), (hh)), interpolation = cv2.INTER_LANCZOS4)
                face2replace_array.append(face2replace)
                i -= 1
                j += 1
            return face2replace_array, face_2_replace_copy

def swapFaces(image, new_face_array, face2replace_array, face_2_replace_copy):
    #merged_image = image.copy()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    i = 0
    for img in range(0, len(face2replace_array)-1):
        j = 0
        for img in range(0, len(new_face_array)-1):
            for (x,y,w,h) in face:  
                face_2_replace_copy[y:y+new_face_array[j].shape[0], x:x+new_face_array[j].shape[1]] = face2replace_array[i]
                merged_image = face_2_replace_copy
                i += 1
                j += 1
            return (merged_image)
    
image = cv2.imread('fam2.png')
roi_color_array, roi_color_array2, roi_color_array3 = box_faces(image)
#fname = write2file(roi_color_array)
new_face_array, newFaces_copy = newFaces(image, roi_color_array2)
face2replace_array, face_2_replace_copy = face_2_replace(image, new_face_array, roi_color_array3)
merged_image = swapFaces(image, new_face_array, face2replace_array, face_2_replace_copy)
#cv2.imshow('merged_image', merged_image)
cv2.imwrite('merged_image.png', merged_image)
