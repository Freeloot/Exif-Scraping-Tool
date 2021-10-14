"""Dependencies"""
from PIL.ExifTags import TAGS
from PIL import Image
import sys

f = open("metadata.txt", 'a')
f.write(f"\n")

try:

    imageDir = sys.argv[1]
    print('\n')
    image = Image.open(imageDir)

    exifdata = image.getexif()

    for tagid in exifdata:
          
        tagname = TAGS.get(tagid, tagid)
      
        value = exifdata.get(tagid)
        print(f"{tagname:25} : {value}")

        f = open("metadata.txt", "a")
        f.write(f"{tagname:25}: {value}\n")
        f.close()
except Exception as error:
    print(f"\n An Error Occurred! ({error}) \n \n USAGE: \n \n python est.py image.jpg \n python est.py imagesFolder/image.jpg \n")
