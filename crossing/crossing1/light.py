from crossing.crossing1.sensor import Sensor

RED = 0
YELLOW_TURNING_GREEN = 1
GREEN = 2
YELLOW_TURNING_RED = 3

TIME_FROM_YELLOW_TO_GREEN = 100
MINIMUM_GREEN_TIME = 100
TIME_FROM_YELLOW_TO_RED = 100


class Light(Sensor):

    def __init__(self, light_id, ticker=None, arcs=None, blockable_arcs=None, signal=None):
        self.light_id = light_id
        self.states = [RED]
        for i in range(0, TIME_FROM_YELLOW_TO_GREEN):
            self.states.append(YELLOW_TURNING_GREEN)
        for i in range(0, MINIMUM_GREEN_TIME):
            self.states.append(GREEN)
        for i in range(0, TIME_FROM_YELLOW_TO_RED):
            self.states.append(YELLOW_TURNING_RED)
        if ticker is not None:
            ticker.register_entity(self)
        self.state_pointer = 0
        self.target_state = RED
        self.timer = 0
        self.arcs = arcs or []
        self.blocked_arcs = []
        self.blockable_arcs = blockable_arcs or []
        self.car_line = []
        self.on_red_time = 0
        self.on_green_time = 0
        self.signal = signal
        super().__init__(light_id, signal=signal)

    def get_state(self):
        return self.states[self.state_pointer]

    def turn_to_green(self):
        print("turning GREEN (%d)" % GREEN)
        self.target_state = GREEN

    def turn_to_red(self):
        print("turning RED (%d)" % RED)
        self.target_state = RED

    def resolve_state(self):

        if (self.get_state() != RED or not self.is_blocked()) and \
                (self.get_state() == self.next_state() or self.get_state() != self.target_state):
            self.increase_state_pointer()

        if self.get_state() == GREEN:
            self.block_blockable_arcs()
            self.open()
            self.timer = 0
        elif self.get_state() == YELLOW_TURNING_RED:
            self.block_blockable_arcs()
        elif self.get_state() == RED:
            self.release_blocked_arcs()
            self.close()
        elif self.get_state() == YELLOW_TURNING_GREEN:
            self.block_blockable_arcs()

    def is_blocked(self):
        return sum([arc.is_blocked() for arc in self.arcs]) > 0

    def open(self):
        for arc in self.arcs:
            arc.open()

    def close(self):
        for arc in self.arcs:
            arc.close()

    def block_blockable_arcs(self):
        for blockable in self.blockable_arcs:
            blockable.block(self)
            self.blocked_arcs.append(blockable)

    def release_blocked_arcs(self):
        for blocked in self.blocked_arcs:
            blocked.unblock(self)
            self.blocked_arcs.remove(blocked)

    def increase_state_pointer(self):
        self.state_pointer = self.next_pointer()
        print("new state: %d" % self.get_state())

    def next_state(self):
        return self.states[self.next_pointer()]

    def next_pointer(self):
        return (self.state_pointer + 1) % self.states.__len__()

    def update_signal(self):
        self.signal = [self.on_red_time, self.on_green_time, len(self.car_line)]

    def get_signal(self):
        return self.signal

    def __str__(self):
        return f'Light [{self.light_id}] \n' \
               f' * state = {self.get_state().__str__()} \n' \
               f' * state_pointer = {self.state_pointer.__str__()} \n' \
               f' * next_state = {self.next_state().__str__()} \n' \
               f' * target_state = {self.target_state.__str__()} \n' \
               f' * blocked = {self.is_blocked().__str__()}'

    def tick(self, value=None):
        print(f'Light.tick({value or ""})')
        self.timer = self.timer + (value or 1)
        self.resolve_state()
        self.update_signal()

