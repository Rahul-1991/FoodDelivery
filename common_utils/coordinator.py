from pymongo import MongoClient


class MongoCoordinator(object):

    def __init__(self):
        self.client = MongoClient('localhost:27017')
        self.db = self.client.FoodDelivery

    def find_one(self, query={}):
        return self.db.collection.find_one(query)

    def find_many(self, query={}):
        return self.db.collection.find(query)

    def create_document(self, data={}):
        self.db.collection.insert(data)

    def delete_one(self, query={}):
        self.db.collection.delete_one(query)

    def delete_many(self, query={}):
        self.db.collection.delete_many(query)
