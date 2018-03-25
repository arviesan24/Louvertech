from PIL import Image
import glob, os

def create_thumbnail(instance):
    size = 400, 300

    output_thumb, ext = os.path.splitext(str(instance.image_location))
    file = Image.open(instance.image_location)
    file.thumbnail(size, Image.ANTIALIAS)
    file.save(output_thumb + ".thumbnail", "JPEG")



    # size = 128, 128
    #
    # for infile in glob.glob("*.jpg"):  #select all the files with .jpeg
    #     file, ext = os.path.splitext(infile)  #split the file to filename(file) and extention(ext)
    #     im = Image.open(infile)
    #     im.thumbnail(size)
    #     im.save(file + ".thumbnail", "JPEG")


    # outfile = os.path.splitext(infile)[0] + ".thumbnail"
    # if infile != outfile:
    #     try:
    #         im = Image.open(infile)
    #         im.thumbnail(size, Image.ANTIALIAS)
    #         im.save(outfile, "JPEG")
    #     except IOError:
    #         print "cannot create thumbnail for '%s'" % infile