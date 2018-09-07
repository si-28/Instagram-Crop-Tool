from PIL import Image

def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    #cropped_image.show()


if __name__ == '__main__':

    image_file = "image.jpg"
    im = Image.open(image_file)

    # get image dimensions
    imageWidth = im.size[0]
    imageHeight = im.size[1]

    # set # of tiles
    tileWidthNum = 3;
    
    tileWidth = imageWidth/tileWidthNum
    tileHeight = tileWidth
    tileHeightNum = imageHeight / tileHeight

    # number of output tiles
    tileNum = tileWidthNum * tileHeightNum


    count = 0
    for j in range (0, tileHeightNum):
        for i in range(0, tileWidthNum):
            x1 = i*tileWidth
            y1 = j*tileHeight
            x2 = (i+1) * tileWidth
            y2 = (j+1) * tileHeight

            crop(image_file, (x1, y1, x2, y2), str(count) + '.jpg' )
            count+=1
