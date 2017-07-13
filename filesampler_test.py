# -*- coding: utf-8 -*-
#!/usr/bin/python

import unittest
import os
from filesampler import *

from sys import argv, exit


class FileSamplerTest(unittest.TestCase):
    
    def testSamplerCreatedOk(self):
        """ Check that the object is created with the correct parameters """
        sampler = Sampler("in", "out", 2)
        self.assertEqual("in", sampler.input)
        self.assertEqual("out", sampler.output)
        self.assertEqual(2, sampler.sampleSize)

    def testSamplerReadsFileListOk(self):
        """ Given a directory, read the files in it correctly """
        sampler = Sampler("testdirs/01/in", "out", 2)
        fileList = sampler.fileList()
        fileList.sort()
        self.assertEqual(fileList, ["001.txt","002.txt","003.txt","004.txt","005.txt"])

    def testSamplerReadsFileListOkAndDoesNotIncludeFolders(self):
        """ Check that files are listed not directories """
        sampler = Sampler("testdirs/02/in", "out", 1)
        fileList = sampler.fileList()
        fileList.sort()
        self.assertEqual(fileList, ["001.txt","002.txt"])

    def testSamplerThrowsExceptionIfInvalidSampleSize(self):
        """ Check that if the sample size is bigger than the directory list an exception is thrown """
        sampler = Sampler("testdirs/02/in", "out", 1000)
        self.assertRaises(FileSamplerException, sampler.checkValidSampleSize)

    def testSamplerValidatesOnValidSampleSize(self):
        """ Check that if the sample size is ok the sampler validates """
        sampler = Sampler("testdirs/02/in", "out", 1)
        self.assertTrue(sampler.validate())

    def testFileSamplesInsideFileList(self):
        """ check that the sample size is correct and the items are effectively a sample of the original """
        sampler = Sampler("testdirs/01/in", "out", 3)
        fileList = sampler.fileList()
        sample = sampler.sample()

        for s in sample:
            self.assertTrue(s in fileList)

    def testFileSampleListHasTheCorrectSize(self):
        """ check that the sample size is correct and the items are effectively a sample of the original """
        sampler = Sampler("testdirs/01/in", "out", 2)
        sample = sampler.sample()
        self.assertEqual(2, len(sample))
        
    def testFileSampleListHasTheCorrectSize2(self):
        """ check that the sample size is correct and the items are effectively a sample of the original """
        sampler = Sampler("testdirs/01/in", "out", 4)
        sample = sampler.sample()
        self.assertEqual(4, len(sample))
        


    def fileList(self):
        currentPath = Path(self.input)
        l = [pathitem.name for pathitem in currentPath.iterdir() if not(pathitem.is_dir())]
        return l

    def readFile(self, ruta):
        if not os.path.exists(ruta):
            sys.exit("El archivo '%s' no existe." % ruta)
        elif not os.path.isfile(ruta):
            sys.exit("El archivo '%s' es invalido." % ruta)

        archivo = open(ruta, "r")
        return archivo.read()



def main():
    unittest.main()

if __name__ == '__main__':
    main()