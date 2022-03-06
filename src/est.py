from PIL.ExifTags import TAGS
from PIL import Image
import sys
import piexif

global image

f = open("metadata.txt", 'a')
f.write(f"\n")

codec = 'ISO-8859-1'

def exif_to_tag(exif_dict):
    exif_tag_dict = {}
    thumbnail = exif_dict.pop('thumbnail')
    exif_tag_dict['thumbnail'] = thumbnail.decode(codec)

    for ifd in exif_dict:
        exif_tag_dict[ifd] = {}
        for tag in exif_dict[ifd]:
            try:
                element = exif_dict[ifd][tag].decode(codec)
            except AttributeError:
                element = exif_dict[ifd][tag]
            exif_tag_dict[ifd][piexif.TAGS[ifd][tag]["name"]] = element

    return exif_tag_dict

def get_device_data():
    try:
        imageDir = sys.argv[1]
        image = Image.open(imageDir)
        exifdata = image.getexif()

        for tagid in exifdata:
            tagname = TAGS.get(tagid, tagid)
            value = exifdata.get(tagid)

            print(f"{tagname:25} : {value}")

            f = open("metadata.txt", "a")
            f.write(f"{tagname:25}: {value}\n")
            f.close()
        return image
    except Exception as error:
        print(f"\n An Error Occurred! ({error}) \n \n USAGE: \n \n python est.py image.jpg \n python est.py imagesFolder/image.jpg \n")
    
def get_location_data():
    try:
        imageDir = sys.argv[1]
        image = Image.open(imageDir)
        exif_dict = piexif.load(image.info.get('exif'))
        exif_dict = exif_to_tag(exif_dict)

        print(exif_dict['GPS'])

        f = open("metadata.txt", "a")
        f.write(f"{exif_dict['GPS']}\n")
        f.close()
    except Exception as error:
        print(f"\n An Error Occurred! ({error}) \n \n USAGE: \n \n python est.py image.jpg \n python est.py imagesFolder/image.jpg \n")

if __name__ == '__main__':
    get_device_data()
    get_location_data()
