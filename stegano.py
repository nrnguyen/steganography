from PIL import Image
import binascii
import optparse

def Main():
	parser = optparse.OptionParser('usage %prog '+\
		'-e/-d <target file> -f <target textfile>')

	parser.add_option('-e', dest='hide', type='string', \
		help='target picture path to hide text')

	parser.add_option('-f', dest='file', type='string', \
		help='target text file to read and hide')

	parse.add_option('-d', dest='retr', type='string', \
		help='target picture path to retrieve text')

	(options, args) = parser.parse_args()
	if (options.hide != None && options.text != None):
		file = open(options.file, "r")
		text = file.read()
		print hide(options.hide, text)
	elif (options.hide != None):
		text = raw_input("Enter a message to hide: ")
		print hide(options.hide, text)
	elif (options.retr != None):
		print retr(options.retr)
	else:
		print parser.usage
		exit(0)

if __name__ == '__main__':
	Main()