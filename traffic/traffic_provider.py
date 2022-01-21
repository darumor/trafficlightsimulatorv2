import json
from traffic.traffic_generator import TrafficGenerator
from traffic.car import Car


class TrafficProvider:

    def __init__(self, input_filename=None, entries=None, exits=None, number_of_cars=0, max_ticks_in_between=10):
        print("Init TrafficProvider")
        self.traffic = None
        self.traffic_pointer = 0
        if input_filename is not None:
            self.traffic = self.read_input_file(input_filename)
        else:
            self.traffic = TrafficGenerator.generate_random_traffic(entries, exits, number_of_cars, max_ticks_in_between)

    @staticmethod
    def read_input_file(filename):
        with open(filename, 'r') as f:
            traffic_data = json.load(f)
            if traffic_data is not None:
                return traffic_data
            else:
                raise IOError
        return []

    def get_next_traffic_batch(self, tick=0):
        get_next = True
        to_return = []
        if self.traffic_pointer >= len(self.traffic):
            raise Exception("no more traffic")
        while get_next:
            item = self.traffic[self.traffic_pointer]
            if item['tick'] <= tick:
                to_return.append(Car(item['car_id'], item['tick'], item['entry'], item['exit']))
                self.traffic_pointer += 1
                if self.traffic_pointer >= len(self.traffic):
                    get_next = False
            else:
                get_next = False
        return to_return





