class Car:

    def __init__(self, car_id, tick, entry_node, exit_node):
        print(f'Initializing car {car_id or ""}')
        self.car_id = car_id
        self.tick = tick
        self.entry_node = entry_node
        self.exit_node = exit_node
        self.waiting_time = 0
        self.moving_time = 0
        self.moving = True
        self.latest_tick = None
        self.ticker = None
        self.path = None

    def tick(self, value=None):
        print(f'Car[{self.car_id}].tick({value or ""})')
        if self.latest_tick is None:
            self.latest_tick = value
        if self.moving:
            self.moving_time += value - self.latest_tick
        else:
            self.waiting_time += value - self.latest_tick
        self.latest_tick = value

    def start(self):
        self.moving = True

    def stop(self):
        self.moving = False

    def set_path(self, path):
        self.path = path


