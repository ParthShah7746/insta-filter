#Import image from PIL
from PIL import Image

#Load images into objects
base_img = Image.open("elon.jpg")
img_filter = Image.open("t.jpg")


#Set O/P Image size
size = (3840,2160)


#Resize all images to o/p size
base_img = base_img.resize(size)
img_filter = img_filter.resize(size)


#Split each image into RGB vectors
r ,g ,b = base_img.split()
R,G,B = img_filter.split()

#Merge RGB vectors from different images
im= Image.merge("RGB",(R , g, b))
im.show()


#im.save('merged.jpg')