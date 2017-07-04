from common_utils.coordinator import MongoCoordinator


class AddRemoveService(object):

    def __init__(self):
        self.coordinator = MongoCoordinator()

    def insert_new_document(self, data):
        try:
            self.coordinator.create_document(data)
            return True
        except Exception as e:
            return False

    def delete_document(self, query):
        try:
            self.coordinator.delete_many(query)
            return True
        except Exception as e:
            return False