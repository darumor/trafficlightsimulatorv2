from random import randint


class TrafficGenerator:

    def __init__(self):
        print("Init generator")

    @staticmethod
    def generate_random_traffic(entries=None, exits=None, number_of_cars=0, max_ticks_in_between=10):
        print("Generating")
        to_return = []
        noc = 0
        current_tick = 0
        current_id = 0
        while noc < number_of_cars:
            current_tick = current_tick + randint(1, max_ticks_in_between)
            current_id += 1
            car = {
                "car_id": f'car-{current_id}',
                "tick": current_tick,
                "entry": entries[randint(0, len(entries)-1)],
                "exit": exits[randint(0, len(exits)-1)]
            }
            to_return.append(car)
            noc += 1
        return to_return

