import sys
import os
import PIL
from PIL import Image

path = sys.argv[1]
base_name = os.path.splitext(os.path.basename(path))[0]
target = os.path.join(os.path.dirname(path),"..","..","stage","images",base_name+".png")

print "Resizing %s to %s" % (path, target)

size = (128,128)
im = Image.open(path)
im.thumbnail(size, Image.ANTIALIAS)
im.save(target, "PNG")
