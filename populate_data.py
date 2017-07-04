from pymongo import MongoClient
from datetime import datetime


class MongoConnection(object):

    def __init__(self):
        self.mongo_url = 'localhost:27017'
        self.mongo_client = self.get_mongo_client()
        self.mongo_db = self.get_db()

    def get_mongo_client(self):
        return MongoClient(self.mongo_url)

    def get_db(self):
        return self.mongo_client.FoodDelivery

    def add_data(self, data):
        self.mongo_db.delivery_model.insert(data)


class PopulateData(object):

    def __init__(self):
        self.mongo_conn = MongoConnection()
        self.file_content = self.get_file_content('Mobile_Food_Schedule.tsv')

    def get_file_content(self, filename):
        return open(filename).readlines()

    def get_headers(self):
        return self.file_content[0].strip('\xef\xbb\xbf\n').split('\t')

    def prepare_document(self, record):
        processed_document = dict()
        columns = record.strip().split('\t')
        headers = self.get_headers()
        for index, header in enumerate(headers):
            if header == 'Addr_Date_Create':
                processed_document['created_at'] = columns[index]
            if header == 'Addr_Date_Modified':
                processed_document['modified_at'] = columns[index]
            if header == 'Addr_Date_Create' or header == 'Addr_Date_Modified':
                try:
                    processed_document[header] = datetime.strptime(columns[index], '%m/%d/%Y %H:%M:%S %p')
                except Exception as e:
                    pass
            else:
                processed_document[header] = columns[index]
        return processed_document

    def insert_record_to_db(self, record):
        self.mongo_conn.add_data(record)

    def main(self):
        for index, record in enumerate(self.file_content):
            if not index:  # skip header row
                continue
            processed_document = self.prepare_document(record)
            self.insert_record_to_db(processed_document)

class_obj = PopulateData()
class_obj.main()

