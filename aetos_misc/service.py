from common_utils.coordinator import MongoCoordinator
from common_utils.mongo_utils import serialize_document
from datetime import datetime


class MiscService(object):

    def __init__(self):
        self.coordinator = MongoCoordinator()

    def get_from_mongo(self, query):
        result = self.coordinator.find_many(query)
        return serialize_document(result)

    def get_trucks_in_location(self, location):
        query = {'locationdesc': {'$regex': '.*' + location + '.*', '$options': 'i'}}
        return self.get_from_mongo(query)

    def truck_start_stop_time(self, document):
        delivery_date = document.get('Addr_Date_Create').split()[0]
        start_time = datetime.strptime(
            '{} {}'.format(delivery_date, document.get('start24')), '%m/%d/%Y %H:%M')
        end_time = datetime.strptime(
            '{} {}'.format(delivery_date, document.get('end24')), '%m/%d/%Y %H:%M')
        return start_time, end_time

    def get_trucks_in_timeframe(self, document_list):
        best_truck_choice = dict()
        max_time_diff = 0
        for document in document_list:
            start_time, end_time = self.truck_start_stop_time(document)
            current_time = datetime.strptime('10/22/2013 11:47', '%m/%d/%Y %H:%M')
            if start_time < current_time < end_time:
                time_diff_from_end_time = end_time - current_time
                if time_diff_from_end_time.seconds > max_time_diff:
                    max_time_diff = time_diff_from_end_time.seconds
                    best_truck_choice = document
        return best_truck_choice

    def get_suitable_trucks(self, location_list):
        truck_for_location = dict()
        for location in location_list:
            applicable_trucks = self.get_trucks_in_location(location)
            filtered_truck = self.get_trucks_in_timeframe(applicable_trucks)
            truck_for_location.update({location: filtered_truck})
        return truck_for_location

