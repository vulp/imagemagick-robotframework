__author__ = 'Tuomo Pohjola'

import os
import sys
from subprocess import Popen, PIPE
from pymongo import MongoClient
import gridfs


class Custom:
    def __init__(self):
        print ("Hello")

    def save_image(self,test_name,suite_name):
        print('saving')
        db = MongoClient('localhost', 27017).gridfs_example
        fs = gridfs.GridFS(db)
        baseimage = os.path.abspath(os.curdir+'\\robot\\baseimages\\baseimage.png')
        #fileID = fs.put( open( baseimage, 'rb')  )
#        with open(baseimage, 'rb') as image:
#            fs.put(image,meta='test1')

        a = fs.find_one({'meta':'test1'})
        print(a)
        print(a._id)
        print(a.read())
        fs.get('59f5fa3d751f693518f43507').read()

    def image_difference(self,test_name,suite_name):
        #magick compare -metric ae selenium-screenshot-1.png base1.png diff.png
        print ("asdf",test_name)
        print (os.path.abspath(os.curdir))
        print (os.path.abspath(os.curdir)+'\\robot\\screenshots')
        screenshots = os.path.abspath(os.curdir+'\\robot\\screenshots\\screenshot.png')
        baseimages = os.path.abspath(os.curdir+'\\robot\\baseimages\\'+test_name+'.png')
        diff = os.path.abspath(os.curdir+'\\robot\\baseimages\\'+test_name+'_diff.png')

        process = Popen('magick compare -metric ae ' +screenshots + ' '+baseimages + ' '+diff , stdout=PIPE,stderr=PIPE)
        stderr, stdout = process.communicate()

        #todo save to database
        # name, suitename, imagediff

        if stdout:

            value = stdout.decode("utf-8")
            if int(value) > 10:
                return value
            else:
                return 'True'
        if stderr:
            print('testi seuraava2;')
            print(stderr)

#def main():
#    Parsing()
#
#if __name__ == '__main__':
#    main()