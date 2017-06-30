from pymongo import MongoClient


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
        columns = record.strip().split('\t')
        headers = self.get_headers()
        return {header: columns[index] for index, header in enumerate(headers)}

    def insert_record_to_db(self, record):
        self.mongo_conn.add_data(record)

    def main(self):
        for index, record in enumerate(self.file_content):
            if not index:  # skip header row
                pass
            processed_document = self.prepare_document(record)
            self.insert_record_to_db(processed_document)

class_obj = PopulateData()
class_obj.main()

