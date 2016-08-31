# image_manipulation
# Computer Vision & Image Manipulation with Python 2.7 + OpenCV 3.1
# CS-4475-A, CS-6475-A / Summer 2016
# Georgia Institute of Technology
# [Professor] Dr. Maria Hybinette
# Original assignment URL:
# http://cobweb.cs.uga.edu/~maria/classes/2016-CompPhoto/H4-Blending.html

Link to Portfolio and to view project-corresponding images:
https://eric-malavenda.myportfolio.com/image-blending

To create a unique mask, the following steps were followed:
Step1: From the existing mask, I added contour and texture in Photoshop, along with stroke, inner glow, and outer glow for 
an enhanced effect:
Step2: The enhanced mask image from “Step 1” was then alpha-blended with an image of the Martian atmosphere/landscape 
from near-space relative to Mars.

Explanations for how I tackled each function (1 – 7). 

1. def generatingKernel(parameter): 
### Given 

2. def reduce(image):
### def reduce(): convolve ---> subsample…Step 1: "Convolve the input image with a generating ###kernel of parameter of 0.4..."
img_convolved = scipy.signal.convolve2d(image, generatingKernel(0.4), 'same')
### Step 2: "...then reduce its width and height by two."
reduced_img_convolved = img_convolved[::2, ::2] 
### "subsampling (essentially you want to index    
### every other row and every other column)."
return reduced_img_convolved ### Although the code above could be written in a single line, I prefer                         
### the readability of multiple lines.

3. def expand(image): 
### def expand(): upsample ---> convolve…Step 1: "Expand the image to double the size..." 
(x, y) = image.shape
expander = np.zeros([x * 2, y * 2])
### Step 2: "...and then convolve it with a generating kernel with a parameter of 0.4. 
expander[::2, ::2] = image
return (scipy.signal.convolve2d(expander, generatingKernel(0.4), 'same') * 4) 
### Step 3: "Finally, multiply your output image by a factor of 4 in order to scale it back up.”
Reference URL: https://developer.apple.com/library/prerelease/content/documentation/Performance/Conceptual/vImage/ConvolutionOperations/ConvolutionOperations.html
As you convolve toward the solution for the expand function specifically, you add to each element as the convolution proceeds 
and continue to add the additional impact of neighboring pixels. The bias built into the test file constrains the pixel values
to between 0 and 255, and with this particular convolution it would otherwise be possible to get negative numbers that would
allow the signal to fall outside of the 0-255 range (which OpenCV auto-constrains pixel values to). The test.py file, however,
prevents this from happening by keeps the values between 0 and 255 according to a “pixel-value” constraining algorithm within
the code, and this built-in bias will force the negative values to become 0, effectively darkening the image as it convolves. 
If you don’t multiply the expand function result by a factor of 4, the convolution will be delayed, and the effect of bias 
will be more pronounced.

4. def gaussPyramid(image, levels):
### "Construct a pyramid from the image by reducing it by the number of levels passed in by the 
###input."
output = [image]
for idx in range(levels): 
### pyramid levels appended to original output as you proceed through loop
      output.append(reduce(output[idx])) 
      ### each pyramid level consists of the output of the reduce( ) 
      ### function during an iteration of the for loop
return output 
### return whole image consisting of layered iterations of the reduce( ) function

5. def laplPyramid(gaussPyr):
### "Construct a laplacian pyramid from the gaussian pyramid, of height levels."
output = []]) 
### “The Gaussian Pyramid that is passed in is the output of your gaussPyramid   
###function,” as subsequent layers are appended to those previously generated within this function’s 
### loop.
for idx in range(len(gaussPyr) - 1):
      (x, y) = gaussPyr[idx].shape
output.append(gaussPyr[idx] - expand(gaussPyr[idx+1])[:x,:y]) 
### append process occurring within 
### each layer, and while that layer is being generated during the necessary number of iterations of 
### the for loop.
output.append(gaussPyr[len(gaussPyr) – 1]) 
### Subsequent layers are appended to those previously 
###generated within this function’s loop.
return output 
### “The Gaussian Pyramid that is passed in is the output of your gaussPyramid 
###function,” as subsequent layers are appended to those previously generated within this function’s 
### loop.

6.  def blend(laplPyrWhite, laplPyrBlack, gaussPyrMask):
pyrBlend = [ ]
for layer in range(len(laplPyrBlack)):
### Each of the three image’s pyramids have the same number of layers. Each layer also has same   
### shape as previous layer.
### Proceed with “the following computation for each layer of the pyramid:”
“output[i, j] = current_mask[i, j] * white_image[i, j] + (1 - current_mask[i, j]) * black_image[i, j]”
      _layer_ = gaussPyrMask[layer] *  laplPyrWhite[layer] + (1 - gaussPyrMask[layer])  * laplPyrBlack[layer]       
      ### Each of the two image’s corresponding Laplacian input layers are alpha ###blended, and weighted by a layer of the Gaussian image of the mask.
     pyrBlend.append(_layer_) 
     ### The result is then appended to the output as a single layer.   
return pyrBlend 
### Laplacian pyramid returned is dimensionally equivalent to each of the input 
###pyramids.

7. def collapse(pyramid):
### "Collapse an input pyramid.”
output = pyramid[len(pyramid)-1] 
### “continue the process until you are
### at the largest image. This is your result.”
for idx in range(len(pyramid) - 2, -1, -1): 
### “start at the smallest layer of the pyramid.” …Then 
### proceed to the second smallest layer…
      (x, y) = pyramid[idx].shape
output = expand(output)[:x, :y] + pyramid[idx] 
### “Expand the smallest layer, and add it to the         
### second to smallest layer.”
### “… expand the second to smallest layer”, and add it to the third smallest layer.
return output 
### “continue the process until you are
### at the largest image.” This is your final output image resulting from the operationally cascading 
### functions.
