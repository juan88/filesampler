# -*- coding: utf-8 -*-
#!/usr/bin/python
#
# See:
# 		https://docs.python.org/3.5/library/filesys.html
# 		https://docs.python.org/3.5/library/shutil.html
#

import os
import argparse
from pathlib import Path
import random

class FileSamplerException(Exception):
	pass

class Sampler(object):

	def __init__(self, input, output, sampleSize, writeFileList=False):
		self.input = input
		self.output = output
		self.sampleSize = sampleSize
		self.writeFileList = writeFileList

	def fileList(self):
		currentPath = Path(self.input)
		l = [pathitem.name for pathitem in currentPath.iterdir() if not(pathitem.is_dir())]
		return l

	def sample(self):
		l = self.fileList()
		sample = random.sample(l, self.sampleSize)
		if self.writeFileList:
			f = open(self.output+os.sep+"sampleList.txt", 'w')
			folder = self.input+os.sep
			for item in sample:
  				f.write("%s%s\n" % (folder, item))
			f.close()
		return sample

	def validate(self):
		try:
		    self.checkValidSampleSize()
		except (FileSamplerException):
		    print("Invalid size of sample.")
		except:
		    print("An unexpected error occurred")
		    raise

		return True

	def checkValidSampleSize(self):
		fileList = self.fileList()
		if len(fileList) <= self.sampleSize:
			raise FileSamplerException("Invalid sample size.")



def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("inputFolder", help="The input folder to where extract the samples")
	parser.add_argument("outputFolder", help="The output folder to place the sampled files")
	parser.add_argument("sampleSize", help="Size of the sample to consider", type=int)
	parser.add_argument("--writeFileList", help="Whether to sample the files or just return a file with the list of files", type=int, nargs='?')
	args = parser.parse_args()

	sampler = Sampler(args.inputFolder, args.outputFolder, args.sampleSize, args.writeFileList)
	sampler.sample()


if __name__ == "__main__":
    # execute only if run as a script
    main()
