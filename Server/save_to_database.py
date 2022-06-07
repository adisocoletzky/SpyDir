import pymongo
from notifications import Notification

#connect to database- mongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["admin"]
mycol = mydb["changes"]


def save_change(user_id, notification, relative_path, time, delta=None):
    try:
        #create dictionery for the notification
        if notification == Notification.ZIP_INIT:
            change = {"user id": user_id,
                      "zip init": relative_path,
                      "time": time}
        elif notification == Notification.DIR_CREATED:
            change = {"user id": user_id,
                      "dir created": relative_path,
                      "time": time}
        elif notification == Notification.FILE_CREATED:
            change = {"user id": user_id,
                      "file created": relative_path,
                      "time": time}
        elif notification == Notification.DIR_DELETED:
            change = {"user id": user_id,
                      "dir deleted": relative_path,
                      "time": time}
        elif notification == Notification.FILE_DELETED:
            change = {"user id": user_id,
                      "file deleted": relative_path,
                      "time": time}
        elif notification == Notification.FILE_MODIFIED:
            change = {"user id": user_id,
                      "file modified": relative_path,
                      "time": time,
                      "delta": delta}
        else:
            raise ValueError()
        mycol.insert_one(change)#insert to database the dictionery
    except:
        pass