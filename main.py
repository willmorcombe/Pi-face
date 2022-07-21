from PIL import Image, ImageOps



# resize the image
def resizeImage(img):
    resize_factor = 130
    size = [int(img.size[0] / resize_factor), int(img.size[1] / resize_factor)]
    print('Image size after resizing: ', size)
    return img.resize(size)

# function to remap the image (turn it to greyscale and map between 0-10)
def remapImage(img):
    img = ImageOps.grayscale(img) # to grayscale

    # transforms pixels to fit on a scale between 0-10
    pixels_for_pi = [int(value / 25.5) for value in list(img.getdata())]

    # transforms pixels back to a scale of 255 for viewing purposes
    pixels = [value * 25.5 for value in pixels_for_pi]

    # shows new rempaed image
    img = Image.new(img.mode, img.size)
    img.putdata(pixels)
    # img.show()

    return pixels_for_pi



def piLoop(pixels):
    # opens file and saves to ...
    with open('data/pi data/pi.txt') as f:
        for line in f:
            data = line[2:]
    print('loaded')

    for x in range(len(data) - len(pixels)):
        if data[x:len(pixels)+x] == pixels:
            print('success!!!!!!!!!!!!!!!!')





if __name__ == '__main__':

    img_path = 'data/img data/face.jpg'
    img = Image.open(img_path)

    img = resizeImage(img)
    pixels = remapImage(img)
    pixels = ''.join([str(x) for x in pixels])
    print(pixels)

    piLoop(pixels)
