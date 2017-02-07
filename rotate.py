import sys

from PIL import Image



def rotate(image_filepath):
    #new_im = Image.open("http://static.boredpanda.com/blog/wp-content/uploads/2017/01/cute-zoo-animal-tweet-off-2.jpg")
    new_im = Image.open(image_filepath)
    rot_im = new_im.rotate(45).show()




image_filepath = sys.argv[1]
rotate(image_filepath)
