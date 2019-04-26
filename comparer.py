#!/usr/bin/python3

import sys, getopt
import os
import difflib

def main(argv):
	inputfile = ''
	outputfile = ''
	cmd = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:c:",["ifile=","ofile=","cmd="])
	except getopt.GetoptError:
		print ('comparer.py -i <inputfile> -o <outputfile> -c <command>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('comparer.py -i <inputfile> -o <outputfile> -c <command>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		elif opt in ("-c","--cmd"):
			cmd = arg
#	print ('Input file is "', inputfile)
#	print ('Output file is "', outputfile)
	myCmd = os.popen(cmd).read()
	f=open(outputfile, "a+")
	f.write(myCmd)
	
	with open(outputfile) as f, open(inputfile) as g:
		lines1 = g.readlines()
		lines2 = f.readlines()
		diff = difflib.unified_diff(lines1, lines2, fromfile=inputfile, tofile=outputfile, lineterm='', n=0)
		lines = list(diff)[2:]
		added = [line[1:] for line in lines if line[0] == '+']
		removed = [line[1:] for line in lines if line[0] == '-']

		for line in added:
    			print (line)

		m=open(inputfile, "w")
		m.write(myCmd)

if __name__ == "__main__":
   main(sys.argv[1:])
