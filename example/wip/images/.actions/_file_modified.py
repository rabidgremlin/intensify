import sys
import os
import PIL
from PIL import Image, ImageOps

path = sys.argv[1]
base_name = os.path.splitext(os.path.basename(path))[0]
target = os.path.join(os.path.dirname(path),"..","..","stage","images",base_name+".png")

print "Resizing %s to %s" % (path, target)

size = (480,480)
im = Image.open(path)
thumb = ImageOps.fit(im, size, Image.ANTIALIAS)
thumb.save(target, "PNG")
