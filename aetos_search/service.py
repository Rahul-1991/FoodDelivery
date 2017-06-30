from common_utils.mongo_utils import serialize_document
from common_utils.coordinator import MongoCoordinator


class SearchService(object):

    def __init__(self):
        self.coordinator = MongoCoordinator()

    def get_from_mongo(self, query):
        result = self.coordinator.find_many(query)
        return serialize_document(result)

    def get_filtered_names(self, name):
        query = {'Applicant': {'$regex': '.*' + name + '.*', '$options': 'i'}}
        return self.get_from_mongo(query)

    def get_filtered_streets(self, street_name):
        query = {'locationdesc': {'$regex': '.*' + street_name + '.*', '$options': 'i'}}
        return self.get_from_mongo(query)

