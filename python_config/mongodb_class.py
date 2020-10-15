import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import json
import dns
from python_config.global_variables import Global_variables

class Mongodb_class():    
    def __init__(self):
        try:
            if(Global_variables.appEnvironment == "production"):
                self._cnxn = MongoClient(Global_variables.mongoDBProductionServerURL)
            else:
                self._cnxn = MongoClient(Global_variables.mongoDBDevelopmentServerURL)
        except ConnectionFailure:
            print("Server not available")
    def find(self, collection_name, fields_object='',condition_object='', sorting_object=''):
        result=''
        db = self._cnxn[Global_variables.mongoDatabaseName]
        collection = db[collection_name]
        if sorting_object !='' and condition_object=='' and fields_object !='':
            collectiondoc = collection.find({},fields_object).sort(sorting_object['field_name'], sorting_object['sort_order'])
        elif sorting_object !='' and condition_object=='' and fields_object =='':
            collectiondoc = collection.find().sort(sorting_object['field_name'], sorting_object['sort_order'])
        elif sorting_object != '' and condition_object != '' and fields_object !='':
            collectiondoc = collection.find(condition_object,fields_object).sort(sorting_object['field_name'], sorting_object['sort_order'])
        elif sorting_object != '' and condition_object != '' and fields_object =='':
            collectiondoc = collection.find(condition_object).sort(sorting_object['field_name'], sorting_object['sort_order'])
        elif sorting_object == '' and condition_object == '' and fields_object !='':
            collectiondoc = collection.find({},fields_object)
        elif sorting_object == '' and condition_object == '' and fields_object =='':
            collectiondoc = collection.find()
        elif sorting_object == '' and condition_object != '' and fields_object =='':
            collectiondoc = collection.find(condition_object)
        elif sorting_object == '' and condition_object != '' and fields_object !='':
            collectiondoc = collection.find(condition_object,fields_object)

        for result in collectiondoc:
            print(result)
        return result
    def insert (self, collection_name, data_object):
        db = self._cnxn[Global_variables.mongoDatabaseName]
        collection = db[collection_name]
        result = collection.insert_one(data_object)
        return result 
        #insertob={
        #    "userid":"2020.002",
        #    "firstname":"2Test",
        #    "lastname":"2Test",
        #    "email":"2Test@gmail.com",
        #    "password":"2Test@gmail.com",
        #    "mobile":"9811285317",
        #    "status":2,
        #    "createdon":"2020-01-10 00:00:00",
        #    "updatedon":"2020-01-10 00:00:00"
        #}
    def insert_many(self,collection_name, data_object):
        db = self._cnxn[Global_variables.mongoDatabaseName]
        collection = db[collection_name]
        result = collection.insert_many(data_object)
        return result
        #data_object = [
        #{ "name": "Amy", "address": "Apple st 652"},
        #{ "name": "Hannah", "address": "Mountain 21"},
        #{ "name": "Michael", "address": "Valley 345"},
        #{ "name": "Sandy", "address": "Ocean blvd 2"},
        #{ "name": "Betty", "address": "Green Grass 1"},
        #{ "name": "Richard", "address": "Sky st 331"},
        #{ "name": "Susan", "address": "One way 98"},
        #{ "name": "Vicky", "address": "Yellow Garden 2"},
        #{ "name": "Ben", "address": "Park Lane 38"},
        #{ "name": "William", "address": "Central st 954"},
        #{ "name": "Chuck", "address": "Main Road 989"},
        #{ "name": "Viola", "address": "Sideway 1633"}
        #]
    def update (self, collection_name, data_object, condition_object):
        db = self._cnxn[Global_variables.mongoDatabaseName]
        complete_data_object = { "$set": data_object }
        collection = db[collection_name]
        result = collection.update_one(condition_object, complete_data_object)
        return result
        #condition_object = { "email": "FistTest@gmail.com" }
        #data_object = { "mobile": "11231","password": "11231" }
    def update_many(self, collection_name, data_object, condition_object):
        db = self._cnxn[Global_variables.mongoDatabaseName]
        collection = db[collection_name]
        complete_data_object = { "$set": data_object }
        result = collection.update_many(condition_object, complete_data_object)
        return result
        #condition_object = { "address": { "$regex": "^S" } }
        #data_object = { "$set": { "name": "Minnie" } }
    def delete(self, collection_name, condition_object):
        db = self._cnxn[Global_variables.mongoDatabaseName]
        collection = db[collection_name]
        result = collection.delete_one(condition_object)
        return result
        #condition_object = { "email": "FistTest@gmail.com" }
    def delete_many(self, collection_name, condition_object):
        db = self._cnxn[Global_variables.mongoDatabaseName]
        collection = db[collection_name]
        result = collection.delete_many(condition_object)
        return result
        #condition_object = { "address": {"$regex": "^S"} } }
    def __del__(self):
        self._cnxn.close()