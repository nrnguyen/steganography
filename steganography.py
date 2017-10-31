#!/bin/bash/python3

from PIL import Image
from io import BytesIO
import optparse

def getCurrentPixel(image):
    #Get current pixel
    if "RGB" not in image.mode:
        print ("Error: Improper image type.")

    (width, height) = image.size
    for y in range(height - 1, -1, -1):
        for x in range(width - 1, -1, -1):
            for channel in range(3):
                yield pixelContainer(image, (x, y), channel)


def decode(inputFile, outputFile=None):
    #Pulls text out of an image.
    image = Image.open(inputFile)
    currentPixel = getCurrentPixel(image)

    #Read big-endian integer from image.
    value = 0
    try:
        for i in range(32):
            bit = next(currentPixel).bitData
            value = (value << 1) | bit
    except:
        print ("Error: Something went wrong.")
    #Ignore 33rd value
    next(currentPixel)

    bitLength = value
    if not ((bitLength // 8) * 8 == bitLength):
        print ("Error: Incorrect length of bits.")
    byteLength = bitLength // 8

    if outputFile:
        with open(outputFile, mode="wb") as output:
            #Write text from the image to the output file.
            for i in range(byteLenth):
                output.write(pullByte(currentPixel))
        print("Text written to file: {}".format(outputFile))
    else:
        with BytesIO() as output:
            #Write the text from the image to CLI.
            for i in range(byteLength):
                output.write(pullByte(currentPixel))
            try:
                print(output.getvalue().decode())
            except:
                print ("Error: Invalid format.")

def pullInteger(currentPixel, count):
    #Pull out a big-endian integer from the image.
    endianValue = 0
    try:
        for i in range(count):
            bit = next(currentPixel).bitData
            endianValue = (endianValue << 1) | bit
        return endianValue
    except:
        print ("Error: Something went wrong.")

def pullByte(currentPixel):
    #Pull out a byte from the image.
    bytePulled = pullInteger(currentPixel, 8)
    return bytes([bytePulled])

def Main():
    parser = optparse.OptionParser('usage %prog '+\
        '-e/-d <target imagefile> -f <target textfile>')

    parser.add_option('-e', dest='hide', type='string', \
        help='target picture path to hide text')

    parser.add_option('-f', dest='file', type='string', \
        help='target file to read and hide text')

    parser.add_option('-d', dest='retr', type='string', \
        help='target picture path to retrieve text')

    parser.add_option('-o', dest='out', type='string', \
        help='target output file to save text')

    (options, args) = parser.parse_args()
    if (options.hide != None and options.file != None):
        #Encode a message using a file.
        file = open(options.file, "r")
        text = file.read()
        encode(options.hide, text)
    elif (options.hide != None):
        #Encode a custom message using the CLI.
        text = input("Enter a message to hide: ")
        encode(options.hide, text)
    elif (options.retr != None):
        if (options.out != None):
            #Decode a hidden message and write to a file.
            decode(options.retr, options.out)
        else:
            #Decode a hidden message and print to CLI.
            decode(options.retr)
    else:
        exit(0)

if __name__ == '__main__':
    Main()