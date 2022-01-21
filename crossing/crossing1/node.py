class Node:
    def __init__(self, node_data, crossing):
        self.id = node_data["id"]
        self.type = 'Node'
        self.entries = []  # arcs
        self.exits = []  # arcs
        self.is_entry_node = node_data["entry"]
        self.is_exit_node = node_data["exit"]
        self.is_light_node = node_data["light"]
        self.is_sensor_node = node_data["sensor"]
        if self.is_sensor_node:
            crossing.add_sensor(self)
            self.signal_length = node_data["signalLength"]
        if self.is_light_node:
            crossing.add_light(self)

    def __str__(self):
        string = self.id + ' '
        if self.is_entry_node:
            string += '(entry) '
        if self.is_exit_node:
            string += '(exit) '
        string += 'Entries: ' + map(lambda e: e.id, self.entries).__str__()
        string += ' Exits: ' + map(lambda e: e.id, self.exits).__str__()
        return string


