from simulator.ticker import Ticker
from controller.controller1.ctrl import Controller
from crossing.crossing1.crsg import Crossing


class TrafficLightsSimulator:

    def __init__(self, coefficients=None, graph_file_name=None, traffic_provider=None, tick_rate=1, max_ticks=0, simulator_id=None):
        print("Init TrafficLightsSimulator")
        self.coefficients = coefficients
        self.traffic_provider = traffic_provider
        self.ticker = Ticker(tick_rate, max_ticks)
        self.ticker.register_entity(self)
        self.crossing = Crossing(ticker=self.ticker, graph_file_name=graph_file_name, traffic_provider=traffic_provider)
        self.controller = Controller(ticker=self.ticker, crossing=self.crossing, coefficients=coefficients)
        self.done = False
        if simulator_id is not None:
            self.simulator_id = f'[{simulator_id}]'
        else:
            self.simulator_id = ""

    def start(self):
        # get entry points of crossing
        # get exit points of crossing


        print(f'Starting simulation{self.simulator_id}')
        self.ticker.start()
        self.ticker.join()
        self.done = True
        print(f'Simulation{self.simulator_id} has ended')

    def tick(self, value=None):
        print(f'Simulator{self.simulator_id}.tick({value or ""})')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starting...")
    sim = TrafficLightsSimulator(coefficients=coefficients, graph_file_name=graph_file_name, traffic_provider=traffic_provider, simulator_id="default", max_ticks=10000, tick_rate=10)
    sim.start()
