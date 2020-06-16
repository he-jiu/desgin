from flask import Flask

import pymongo

from flask import request

import datetime

import json

import time

from threading import Timer

import os

import shutil

myclient = pymongo.MongoClient('mongodb://172.17.200.240:27017/',connect=False)

checkrecords = myclient['checkrecords']

def changeurl(ID,url):



    oldpath=url



    newpath='static/img/'+ID



    if os.path.exists(newpath):



        shutil.move(oldpath,newpath)



    else:



        os.makedirs(newpath)



        shutil.move(oldpath,newpath)



        checkrecords.collection.update_one({'id':ID},{'$set':{'imgurl':newpath+'/'+oldpath.split('/')[-1]}})


