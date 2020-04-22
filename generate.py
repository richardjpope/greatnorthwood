# import glob
# import exifread

# for image_path in glob.glob('data/*.jpeg'):
#     image_file = open(image_path, 'rb')
#     image_exif = exifread.process_file(image_file)

#     print(image_exif.get('Image Description', '0'))
#     # image_info = {
#     #     'Image DateTime': image_exif.get('Image DateTime', '0'),
#     #     'GPS GPSLatitudeRef': image_exif.get('GPS GPSLatitudeRef', '0'),
#     #     'GPS GPSLatitude': image_exif.get('GPS GPSLatitude', '0'),
#     #     'GPS GPSLongitudeRef': image_exif.get('GPS GPSLongitudeRef', '0'),
#     #     'GPS GPSLongitude': image_exif.get('GPS GPSLongitude', '0')
#     # }

#     # for k in image_exif:
#     # 	print(image_exif.get(k, False))


import os.path
from PIL import Image
import yaml
import osxphotos
import models
from jinja2 import Environment, FileSystemLoader, select_autoescape

def crop_square(image):
    width, height = image.size

    if width > height:
        return image.crop((0, 0, height, height))
    else:
        return image.crop((0, 0, width, width))
                         

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

# Photos
db = os.path.expanduser("~/Pictures/Photos Library.photoslibrary")
photosdb = osxphotos.PhotosDB(db)
photos = photosdb.photos(albums=["greatnorthwood"])

for photo in photos:
    image = Image.open(photo.path)
    cropped_image = crop_square(image)
    cropped_image.save("%s/docs/images/%s" % (os.getcwd(), photo.filename))

    ##tree page
    tree = models.Tree(photo)
    template = env.get_template('tree.html')
    with open("%s/docs/trees/%s.html" % (os.getcwd(), photo.uuid), "w") as file:
        file.write(template.render(tree=tree))

##index
template = env.get_template('index.html')
with open("%s/docs/index.html" % os.getcwd(), "w") as file:
    file.write(template.render(photos=photos))