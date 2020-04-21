import glob
import exifread

for image_path in glob.glob('data/*.jpeg'):
    image_file = open(image_path, 'rb')
    image_exif = exifread.process_file(image_file)

    print(image_exif.get('Image Description', '0'))
    # image_info = {
    #     'Image DateTime': image_exif.get('Image DateTime', '0'),
    #     'GPS GPSLatitudeRef': image_exif.get('GPS GPSLatitudeRef', '0'),
    #     'GPS GPSLatitude': image_exif.get('GPS GPSLatitude', '0'),
    #     'GPS GPSLongitudeRef': image_exif.get('GPS GPSLongitudeRef', '0'),
    #     'GPS GPSLongitude': image_exif.get('GPS GPSLongitude', '0')
    # }


    # for k in image_exif:
    # 	print(image_exif.get(k, False))
