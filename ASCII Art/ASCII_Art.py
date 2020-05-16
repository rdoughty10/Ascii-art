from PIL import Image
from colorama import init, Fore
from termcolor import colored

from colr import Colr as C

init()

im = Image.open("ryan.jpg")
im.rotate(90)
pix = im.load()


imageWidth, imageHeight = im.size

pixels = [[0]*imageWidth]*imageHeight
luminosity = [[0]*imageWidth]*imageHeight

print(pix[imageWidth/2, imageHeight/4])

ascii = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def getBrightness():
    brightness = []
    minBrightness = 255
    maxBrightness = 0
    for i in range(imageHeight):
        for j in range(imageWidth):
            rgb = pix[j,i]
            pixBrightness = (rgb[0]+rgb[1]+rgb[2])/3
            brightness.append(pixBrightness)

            if (pixBrightness > maxBrightness): maxBrightness=pixBrightness
            if (pixBrightness < minBrightness): minBrightness=pixBrightness


    averageBrightness = 0
    for i in brightness:
        averageBrightness += i
    averageBrightness /= (len(brightness))

    print(averageBrightness)
    print(minBrightness)
    print(maxBrightness)

    return averageBrightness
    
getBrightness()


for i in range(imageHeight):
    print()
    for j in range(imageWidth):
        rgb = pix[j,i]

        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]

        redInv = 255-red
        greenInv = 255-green
        blueInv = 255-blue

        luminosity = 0.21 * red + 0.72 * green + 0.07 * blue
        luminosityInverted = 0.21 * redInv + 0.72 * greenInv + 0.07 * blueInv
        average = (red+green+blue)/3

        asciiNum = int(((len(ascii))*(luminosity))/255)-1
        asciiDigit = ascii[asciiNum]

        asc = asciiDigit * 2

        #print(C().rgb(red, green, blue, asc), end = '')
        print(asc, end='')
        

