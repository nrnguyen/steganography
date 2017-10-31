from PIL import Image
from io import BytesIO
import optparse

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
	if (options.hide != None and options.text != None):
		file = open(options.file, "r")
		text = file.read()
		embed_text(options.hide, text)
	elif (options.hide != None):
		text = raw_input("Enter a message to hide: ")
		embed_text(options.hide, text)
	elif (options.retr != None):
		if (options.out != None):
			extract_text(options.retr, options.out)
		else:
			extract_text(options.retr)
	else:
		exit(0)

if __name__ == '__main__':
	Main()