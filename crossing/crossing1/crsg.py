# read lights, move cars and send signals
import json
from crossing.crossing1.node import Node
from crossing.crossing1.arc import Arc
from crossing.crossing1.sensor import Sensor
from crossing.crossing1.light import Light
from crossing.crossing1.pathfinder import PathFinder


class Crossing:
    def __init__(self, ticker, graph_file_name, traffic_provider):
        self.traffic_provider = traffic_provider
        self.cars = set([])

        self.name = None
        self.nodes = {}
        self.arcs = {}
        self.sensors = {}
        self.lights = {}
        self.entries = []
        self.exits = []
        self.import_graph(graph_file_name)
        self.path_finder = PathFinder(self)

        self.ticker = ticker
        ticker.register_entity(self)

    def handle_batch(self, batch):
        print(f'crossing - handle_batch, size={len(batch)}')
        for car in batch:
            car.set_path(path=self.path_finder.find_path(car.entry_node, car.exit_node))
            self.ticker.register_entity(car)
            self.cars.add(car)


    def move_cars(self, value):
        print("moving cars")
        # check lights
        # move cars
        #

    def update_sensors(self):
        print("updating sensors")

    def tick(self, value=None):
        print(f'Crossing[{self.name}].tick({value or ""})')
        self.handle_batch(self.traffic_provider.get_next_traffic_batch(value))
        self.move_cars(value)
        self.update_sensors()

    def add_sensor(self, sensor_node):
        self.sensors[sensor_node.id] = Sensor(sensor_node.id)

    def add_light(self, light_node):
        self.lights[light_node.id] = Light(light_node.id, self.ticker)

    def add_arc(self, arc):
        self.nodes[arc.start.id].exits.append(arc)
        self.nodes[arc.end.id].entries.append(arc)

    def register_controller(self, controller):
        for sensor in self.sensors:
            controller.register_sensor(sensor)
        for light in self.lights:
            controller.register_light(light)

    def import_graph(self, graph_file_name):
        if graph_file_name is None:
            raise AttributeError("graph_file_name not given")
        with open(graph_file_name, 'r') as f:
            data = json.load(f)

        self.name = data["name"]
        for node in data["nodes"]:
            self.nodes[node["id"]] = Node(node, self)
        for arc in data["arcs"]:
            self.arcs[arc["id"]] = Arc(arc, self)
        for arc in data["arcs"]:
            for blocked_arc in arc["blocks"]:
                self.arcs[arc["id"]].blocks.append(self.arcs[blocked_arc])





