import sys
import os
from PIL import Image


def rotate(image_filepath, outfile):
    new_im = Image.open(image_filepath)
    rot_im = new_im.rotate(45)
    rot_im.save(outfile)

    print("Done.")
    #rot_im_2 = rot_im.save(outfile)

# image_filepath = sys.argv[1]
# outfile = sys.argv[2]
if __name__ == "__main__":
    try:
        this_file, image_filepath, outfile = sys.argv

    except ValueError:
        raise ValueError("Missing required args, Try passing both in and out filenames.")

    finally:
        #rotate(image_filepath, outfile)
        rotate(image_filepath, outfile)
