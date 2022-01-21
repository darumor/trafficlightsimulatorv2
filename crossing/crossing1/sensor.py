import numpy as np

# at some point it may be that Sensor needs more subtypes to enable different types of signal. Light is one subtype.
class Sensor:

    def __init__(self, sensor_id, signal=None):
        self.sensor_id = sensor_id
        if signal is None:
            signal = 0
        if isinstance(signal, int):
            signal = [signal]
        if isinstance(signal, list):
            self.signal = np.array(signal)
        else:
            raise AttributeError(f'could not initialize with {signal}')

    def up(self, value=1):
        np.add(self.signal, value)

    def down(self, value=1):
        np.subtract(self.signal, value)

    def get_signal(self):
        return self.signal

