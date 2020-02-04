# image_manipulation
# Computer Vision & Image Manipulation with Python 2.7 + OpenCV 3.1
# CS-4475-A, CS-6475-A / Summer 2016
# Georgia Institute of Technology
# [Professor] Dr. Maria Hybinette
# Original assignment URL:
# http://cobweb.cs.uga.edu/~maria/classes/2016-CompPhoto/H2-Blend.html

Link to Portfolio and to view project-corresponding images:
https://eric-malavenda.myportfolio.com/multiplicity

The images I used as foreground and background images that would later comprise my algorithmically modified composite image, 
were photos taken of me by my fiancé at our home in  Tucker, GA last week on June 6. I felt that the lighting available in 
our home would be sufficient at the time the photos were taken. They were taken in the evening and we turned on as many lights
as possible, and we also used a flash attachment on our camera. All component images included myself in three different 
positions on the couch, and my cat in a single and mostly static conformation. I was using my phone in one component 
(left portion of composite) image, my laptop in another (central portion of composite) image, and tablet in my third 
(right portion of component) image. I chose this theme based on my observations that people are no longer as motivated
to converse when that are together, with preference more typically given to the use of electronics to serve as life’s
distractions. I chose to name my composite image “A Conversation,” which seems appropriate as a contradiction in images.
The image’s main static props were a large leather couch and one of our cats, a Hemingway named Morgan (who was mostly
still except for slight tail and head movements). Overall, I was pleased with the appearance of the static components 
that were part of my composite image, but I felt that there were algorithmic deficiencies that may have been responsible 
for some of the aberrations seen within my final composite image.   
After many hours of testing various algorithmic modifications while using a limited toolset (and using only a very small 
subset of the tools available through the ‘OpenCV’ module), I ended up with a composite image for which there was certainly
room for additional improvements. The part of the algorithm’s complexity that I struggled with specifically was 
lost-pixel-replacement, in regards to pixels that became transparent after applying a mask to my original foreground/background images.
One of these images (my clone image on right) within my component photos was particularly difficult to modify and apply to my 
composite image, and I believe this was because of the inconsistencies of the indoor lighting which were being applied at the
time these photos were taken. If you look closely at the right and left sides of my composite image, you’ll notice two lamps 
that are both turned on, and that also seem to be adversely affecting the appearance of my clones on both the left and right 
sides of my composite image. These aberrations in my composite image are, I believe, attributable to my inconsistent use of
lighting. My hands and a portions of my face are reflecting light from these lamps extensively, giving my hands a cloaked 
appearance and what I see as being subtle yet fortunately retained outlines of my hands in these specific locations within
my composite image. Perhaps without the excessive light emanating from these lamps, my composite image would have manifested 
itself more nicely, and I plan to test this in the next few days.   

The creation of the mask and its utilization within my code, as well as the lack of modifications made to my ‘fgmask’ and ‘bgmask’
along with few modifications made to their complementary thresholds values, may have been at least partially responsible for the 
shortcomings seen in my composite image, as well as the composite image created with the instructor-provided images. The composite 
I made using the instructor-provided images was roughly equivalent in quality to the instructor-provided composite made using the
same tools (non-Photoshop). My attempts to create a quality composite image of the instructor-provided photos primarily consisted
of my attempts to adjust the threshold values used for creating my masks, as well as switching the masks used when blacking-out
the subject-area within my ROI and isolating the subject-area within the foreground images. I used the ‘bgmask’ for the 
ROI black-out, and ‘fgmask’ for isolation of subject-area within the instructor’s foreground images. I employed the opposite technique
in my algorithm specific to the photos I recently took and used for this assignment; fgmask for ROI black-out and bgmask for
subject-isolation in foreground. I believe the reason why this difference was observed was the significant difference in 
available lighting when the instructor-provided photos were taken [outdoors and in very bright sunlight], in contrast to my images
which consisted of photos that were taken indoors and in the evening with the application of inconsistent lighting. This does not,
however, mean that I shouldn’t have been able to alternatively make adjustments to the algorithms within my code to apply the 
necessary changes to the output composite images, both those consisting of my images and those consisting of the instructor’s.     

In setting up my scene, I noticed that my cat appeared to be sufficiently sedated and I chose to include him as part of the scene.
His slight movements during the shoot seemed to have little impact on the quality of my images and algorithmically modified scene 
pics, including my composite image. The ‘cv2.subtraction’ function may have been more implemented more effectively [than it was] 
when modifying the masks used in my code [for creating and updating the composite image consisting of the instructor’s background
and component images]. I only used this function in one line of my code (part of a for-loop), but the final composite image 
modifications this snippet of code was responsible for were limited in scope. I believe that my future use of improved mask-creation 
and implementation techniques will be critical to improving the final composite images generated.    
