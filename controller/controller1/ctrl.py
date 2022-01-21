from controller.controller1.calc import Calculator


class Controller:
    def __init__(self, ticker=None, crossing=None, coefficients=None):
        self.crossing = crossing
        self.sensors = {}
        self.lights = {}
        crossing.register_controller(self)
        self.calculator = Calculator(self.sensors)
        self.calculator.set_coefficients_from_dict(genes=coefficients)
        self.ticker = ticker
        ticker.register_entity(self)

    def register_sensor(self, sensor):
        self.sensors[sensor.sensor_id] = sensor

    def register_light(self, light):
        self.lights[light.light_id] = light

    def tick(self, value=None):
        print(f'Controller.tick({value or ""})')
        self.set_lights()

    def set_lights(self):
        green = self.calculator.which_light_should_be_green()
        self.lights[green].turn_to_green()
