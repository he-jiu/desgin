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

global user,staff,checkrecords,checklist

user = myclient['user']



checklist = myclient['checklist']



def minutechecklist():#挑选需检查列表

    print('success')

    for x in user.collection.find():

        if (datetime.date(*map(int, x['nextcheckdate'].split('-'))).__eq__(datetime.date.today())):

            checklistdict={'_id':x['_id'],'name':x['name'],'address':x['address'],'longitude':x['longitude'],'latitude':x['latitude'],'emergency':x['emergency'] }

            checklist.collection.insert_one(checklistdict)

    Timer(86400.0, minutechecklist) .start()#循环



if __name__ == '__main__':

    

    minutechecklist()

    
