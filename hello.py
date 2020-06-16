from flask import Flask

import pymongo

from flask import request

import datetime

import json

import time

from threading import Timer

import os

import shutil



app = Flask(__name__)



basedir = os.path.abspath(os.path.dirname(__file__))#当前路径

myclient = pymongo.MongoClient('mongodb://172.17.200.240:27017/',connect=False)

global user,staff,checkrecords,checklist

user = myclient['user']

staff = myclient['staff']

checkrecords = myclient['checkrecords']

checklist = myclient['checklist']



@app.route('/')

def helloworld():

    return 'hello world'



@app.route('/user',methods=['GET'])

def insertUser():#插入用户



    username = request.args.get('name')

    ID = request.args.get('userID')

    address = request.args.get('address')

    phone= request.args.get('telephone')

    longitude=request.args.get('longitude')

    latitude=request.args.get('latitude')



    nextcheckdate=str(datetime.date.today()+datetime.timedelta(days=0))

 

    userdict = { "_id":ID,"name": username, "address": address, "phone": phone,'nextcheckdate':nextcheckdate,"longitude":longitude,"latitude":latitude,'emergency':False }

 

    for x in user.collection.find({'_id':ID}):

        return 'False'

    else:

        user.collection.insert_one(userdict)

        return 'True'

 

    

@app.route('/staff',methods=['GET'])

def insertStaff():#插入员工

    staffname = request.args.get('name')

    ID = request.args.get('staffID')

    phone = request.args.get('telephone')

    password= request.args.get('password')

    kind=request.args.get('staffKind')



    staffdict={ "_id":ID,"name":staffname,"phone":phone,"password":password,"staffKind":kind }



    for x in staff.collection.find({"_id":ID}):

        return 'False'

    for x in staff.collection.find({'phone':phone}):

        return 'False'

    else:

        staff.collection.insert_one(staffdict)

        return 'True'





@app.route('/check',methods=['GET','POST'])

def minuteRecords():                #记录上传

    username = request.args.get('name')

    ID = request.args.get('userID')

    address=request.args.get('address')

    valve= request.args.get('valve')

    tube=request.args.get('tube')

    device=request.args.get('device')

    remarks=request.args.get('remarks')

    url=request.args.get('url')

    

    date=datetime.date.today()



    checkrecordsdict={ "id":ID,"name": username, "address":address ,"date": str(date), "valve": valve,"tube":tube,"device":device,"remarks":remarks,'imgurl':url }

    user.collection.update_one({'_id':ID},{"$set":{"nextcheckdate":str(datetime.date.today()+datetime.timedelta(days=1))}})

    checkrecords.collection.insert_one(checkrecordsdict)



    oldpath=url



    newpath='static/img/'+ID
    print('新路径'+newpath)
    print('老路径'+oldpath)
    filename=oldpath.split('/')[-1]
    filepath=newpath+'/'+oldpath.split('/')[-1]
    print(filepath)

    if os.path.exists(newpath):#路径存在存储图片

        shutil.move(oldpath,newpath)

        checkrecords.collection.update_one({'id':ID},{'$set':{'imgurl':filepath}})#修改数据库存储的路径

    else:#路不存在时先创建文件夹

        os.makedirs(newpath)

        shutil.move(oldpath,newpath)

        checkrecords.collection.update_one({'id':ID},{'$set':{'imgurl':filepath}})#修改数据库存储的路径

    checklist.collection.delete_one({"_id":ID})

    return 'success'

    

@app.route('/upload',methods=['GET','POST'])

def upload():#上传照片


    #获取图片文件 name = upload

    img = request.files.get('file')

 

    #定义一个图片存放的位置 存放在static下面

    path = basedir+"/static/img/"

 

    #图片名称 

    imgName = str(datetime.date.today())+'.'+img.filename.split('.')[1]

 

    #图片path和名称组成图片的保存路径

    file_path = path+imgName

 

    #保存图片

    img.save(file_path)

 

    #url是图片的路径

    url = 'static/img/'+imgName

  

    return url





@app.route('/getchecklist',methods=['GET'])

def getchecklist():#需要检查列表



    thelist=[]

    for x in checklist.collection.find():

        thelist.append(x)



    return json.dumps(thelist)


@app.route('/getusermessage',methods=['GET'])

def getusermessage():#获取用户信息

    userID = request.args.get('id')


    for x in user.collection.find({"_id":userID}):
        return json.dumps(x)
    else:
        return 'false'




@app.route('/changestaffmessage',methods=['GET'])

def changestaffmassage():#修改员工信息

    ID = request.args.get('staffID')

    phone = request.args.get('telephone')

    kind=request.args.get('staffKind')



    if staff.collection.update_one({'_id':ID},{"$set":{"phone":phone,"staffKind":kind}}):

        

        

        return 'True'

    else:

        return 'False'





@app.route('/changeusermessage',methods=['GET'])

def changeusermassage():#修改用户信息

    ID = request.args.get('userID')

    phone = request.args.get('telephone')

    address=request.args.get('address')

    longitude=request.args.get('longitude')

    latitude=request.args.get('latitude')

    emergency=request.args.get('emergency')

    if emergency=='true':
        emergency=True
    else:
        emergency=False

    print(type(emergency))


    for x in checklist.collection.find({'_id':ID}):

        checklist.collection.update_one({'_id':ID},{"$set":{"address":address,'longitude':longitude,'latitude':latitude,'emergency':emergency}})
        user.collection.update_one({'_id':ID},{"$set":{"phone":phone,"address":address,'longitude':longitude,'latitude':latitude,'emergency':emergency}})

        return 'True'

    else:
        if user.collection.update_one({'_id':ID},{"$set":{"phone":phone,"address":address,'longitude':longitude,'latitude':latitude,'emergency':emergency}}):
            return 'True'

        else:
            return 'False'


'''
def minutechecklist():#挑选需检查列表
    print('fuck')
    for x in user.collection.find():

        if (datetime.date(*map(int, x['nextcheckdate'].split('-'))).__eq__(datetime.date.today())):

            checklistdict={'_id':x['_id'],'name':x['name'],'address':x['address'] }

            checklist.collection.insert_one(checklistdict)

    #Timer(3.0, minutechecklist) .start()#循环
'''



@app.route('/deletestaff',methods=['GET'])#删除员工

def deletestaff():

    ID = request.args.get('staffID')

    for x in staff.collection.find({"_id":ID}):

        staff.collection.delete_one({"_id":ID})

        return 'True'

    else:

        return 'False'

    

@app.route('/deleteusers',methods=['GET'])#删除用户

def deleteusers():

    ID = request.args.get('userID')

    for x in user.collection.find({"_id":ID}):

        user .collection.delete_one({"_id":ID})

        return 'True'

    else:

        return 'False'

    

@app.route('/checklogin',methods=['GET'])

def checklogin():#登陆检测

    phone = request.args.get('telephone')

    password = request.args.get('password')





    for x in staff.collection.find({'phone':phone}):

        if x['password']==password :

            return json.dumps(x)

        else:

            return 'False'

    else:

        return 'False'



@app.route('/checkinformation',methods=['GET'])#修改密码确认信息

def checkinformation():

    ID = request.args.get('staffID')

    phone = request.args.get('telephone')



    for x in staff.collection.find({'_id':ID}):

        if x['phone']==phone :

            return 'True'

        else:

            return 'False'

    else:

        return 'False'



@app.route('/changepassword',methods=['GET'])#修改密码

def changepassword():

    ID = request.args.get('staffID')

    password = request.args.get('password')

    staff.collection.update_one({'_id':ID},{"$set":{"password":password}})



    return 'True'



@app.route('/getcheckrecords',methods=['GET'])#获取检查信息

def getcheckrecords():

    ID=request.args.get('id')

    date=request.args.get('date')

    records={}

    for x in checkrecords.collection.find({'id':ID}):

        if x['date']==date:

            for i in x:

                if i!='_id':

                    records.update({i:x[i]})

            return json.dumps(records)

    else:

        return 'false'

@app.route('/getposition',methods=['get'])
def getposition():
    ID=request.args.get('id')
    position=[]
    for x in user.collection.find({'_id':ID}):
        print(x)
        position.append(x['longitude'])
        position.append(x['latitude'])
        return json.dumps(position)

if __name__ == '__main__':

    #minutechecklist()

    

    app.run(host='172.17.200.240',port=5000)



    

      


