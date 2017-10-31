# Text In Image
Project 1
CPSC 353
Introduction to Computer Security
October 31, 2017

## Requirements

- Python (Ver. 3.5.4)
- Pillow (Ver. 4.1.2)

## Description

Steganography is the study of hiding data. This project hides text data into images. Hidden messages can be encoded and then decoded.

## Architecture

## Instructions

You must provide an operation flag to encode (-e) a message or decode (-d) a message.
An image filename is required as an argument.
Input from a file is optional.
Output to a file is optional.

Encode Text:

	python steganography.py -e <inputname>.jpg 
	python steganography.py -e <inputname>.jpg -f <textfilename>

Decode Text:

	python steganography.py -d <inputname>.png
	python steganography.py -d <inputname>.png -o <outputfilename>.txt