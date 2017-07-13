# -*- coding: utf-8 -*-
#!/usr/bin/python
#
# Ver:
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

	def __init__(self, input, output, sampleSize):
		self.input = input
		self.output = output
		self.sampleSize = sampleSize

	def fileList(self):
		currentPath = Path(self.input)
		l = [pathitem.name for pathitem in currentPath.iterdir() if not(pathitem.is_dir())]
		return l

	def sample(self):
		return random.sample(self.fileList(), self.sampleSize)

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
	args = parser.parse_args()
	print(args.inputFolder)
	print(args.outputFolder)
	print(args.sampleSize)

	sampler = Sampler(args.inputFolder, args.outputFolder, args.sampleSize)
	sampler.sample()


if __name__ == "__main__":
    # execute only if run as a script
    main()