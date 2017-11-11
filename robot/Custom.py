__author__ = 'Tuomo Pohjola'

import os
import sys
from subprocess import Popen, PIPE
from pymongo import MongoClient
import gridfs


class Custom:
    def __init__(self):
        print ("Hello")

    def update_data(self, *args):
        client = MongoClient('localhost', 27017)
        db = client.magick

        document = db.data.find_one({'test_name':args[0], 'suite_name':args[1]})
        post = {
            "test_status":args[2]
        }

        if document:
            db.data.find_one_and_update({'_id' : document.get('_id')}, {"$set" : post})

        client.close()

    def save_data(self,test_name,suite_name, *args):
        """
            args[0] screenshot folder
            args[1] baseimage folder
            args[2] diff folder
            args[3] image difference in pixes
        """
        client = MongoClient('localhost', 27017)
        db = client.magick

        document = db.data.find_one({'test_name':test_name, 'suite_name':suite_name})

        post = {
            "test_name":test_name,
            "suite_name": suite_name,
            "screenshot":args[0],
            "baseimage":args[1],
            "diff":args[2],
            "difference":args[3]
        }

        if document:
            db.data.find_one_and_update({'_id' : document.get('_id')}, {"$set" : post})
        else:
            db.data.insert_one(post)

        client.close()

    def image_difference(self,test_name,suite_name):
        #print (os.path.abspath(os.curdir))
        #print (os.path.abspath(os.curdir)+'\\robot\\screenshots')
        screenshots = os.path.abspath(os.curdir+'\\robot\\screenshots\\screenshot.png')
        baseimages = os.path.abspath(os.curdir+'\\robot\\baseimages\\'+test_name+'.png')
        diff = os.path.abspath(os.curdir+'\\robot\\baseimages\\'+test_name+'_diff.png')

        process = Popen('magick compare -metric ae ' +screenshots + ' '+baseimages + ' '+diff , stdout=PIPE,stderr=PIPE)
        stderr, stdout = process.communicate()

        if stdout:
            value = stdout.decode("utf-8")
            self.save_data(test_name,suite_name,screenshots,baseimages,diff,int(value))
            if int(value) > 10:
                return value
            else:
                return 'True'
        if stderr:
            print(stderr)

