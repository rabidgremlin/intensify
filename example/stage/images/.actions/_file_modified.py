import sys
import os
import glob
import json
import re

def unslug(filename):
    filename = re.sub('([A-Z]+)', r'_\1',filename).lower()
    filename = filename.replace("_"," ")
    filename = filename.replace("-"," ")    
    return filename.capitalize()
    

def build_index(path):
    dir = os.path.dirname(path) 
    
    files = glob.glob( os.path.join(dir,"*.png"))
    
    images = []
    
    for file in files:
        info ={"src":"images/" + os.path.basename(file),"name": unslug(os.path.splitext(os.path.basename(file))[0])}
        images.append(info)

    with open(os.path.join(dir,"..","index.json"), 'w') as outfile:
        json.dump({"images": images}, outfile) 

path = sys.argv[1]
build_index(path)
