from simulator import TrafficLightsSimulator
from traffic import TrafficProvider

class Analyser:
    def __init__(self, waiting_time_factor=0.9, total_time_factor=0.1):
        print('init analyser')
        self.waiting_time_factor = waiting_time_factor
        self.total_time_factor = total_time_factor
        self.simulation_id = 0

    def analyse(self, variations, simulator=None):
        values = Values()
        for variation in variations:
            simulator = TrafficLightsSimulator(
                coefficients=variation.genes_as_matrix(),
                graph=None,
                traffic_provider=None,
                tick_rate=10,
                max_ticks=5000,
                simulator_id=f'simulator_{self.simulation_id}'
            )
            values.add(self.run_simulation(simulator, variation))
            self.simulation_id += 1
        values.sort()
        return map(lambda v: v.variation, values.values)

    def run_simulation(self, traffic_lights_simulator, variation):
        traffic_lights_simulator.start()

        waiting_time = 0
        total_time = 0
        cars = traffic_lights_simulator.traffic_provider.traffic
        for car in cars:
            waiting_time += car.waiting_time
            total_time += car.waiting_time
            total_time += car.moving_time
        comparable_value = self.waiting_time_factor * waiting_time + self.total_time_factor * total_time
        print(f'total waiting time: {waiting_time}, total time: {total_time}, comparable: {comparable_value}')
        return Value(comparable_value, variation)


class Values:
    @staticmethod
    def key(value):
        return value.value

    def __init__(self):
        self.values = []

    def sort(self):
        print('sorting')
        self.values.sort(key=self.key)

    def add(self, value):
        self.values.append(value)


class Value:
    def __init__(self, value, variation):
        self.value = value
        self.variation = variation


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starting...")
