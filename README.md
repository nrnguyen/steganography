# Project 1: Text In Image
- Name: Nhat "Rocky" Nguyen
- CPSC 353: Introduction to Computer Security
- Due Date: October 31, 2017

## Requirements

- Python (Ver. 3.5.4)
- Pillow (Ver. 4.1.2)

## Description

Steganography is the study of hiding data. This project hides text data into images. The project was created using Python and Pillow for image manipulation.
Hidden messages can be encoded and then decoded. The image output uses a lossless filetype. This project was written on Microsoft Windows 10.

## Architecture

This Steganography script uses optparse to grab arguments from the CLI. The script opens an image specified by the user and the pixels are loaded. Pixel information is stored within a class and accessed when needed. The encoder writes the length of the text into the image and then the content. A new 'outputimage.png' is created after text is provided. The decoder pulls message length and text content. The output can be displayed through the CLI or saved to a text file.

## Instructions

- You must provide an operation flag to encode (-e) or decode (-d) a message.
- An image filename is required as an argument.
- Input from a file is optional.
- Output to a file is optional.

Encode Text:

	python steganography.py -e <inputname>.jpg 
	python steganography.py -e <inputname>.jpg -f <textfilename>

Decode Text:

	python steganography.py -d <inputname>.png
	python steganography.py -d <inputname>.png -o <outputfilename>.txt