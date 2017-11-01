# -*- coding:utf-8 -*-
import pymongo

class MongoPipeline(object):

    def __init__(self,  mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.open()

    def open(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close(self):
        self.client.close()

    def process_item(self, item, collection_name):
        self.db[collection_name].insert_one(dict(item))
