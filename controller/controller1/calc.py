from math import sqrt
import numpy as np


class Calculator:

    def __init__(self, sensors=None):
        self.sensors = sensors
        if self.sensors is None:
            self.sensors = []
        self.light_ids = []
        self.coefficients = []

    def set_coefficients_from_dict(self, genes=None):
        if genes is None:
            raise AttributeError(f'could not set coefficients to {genes}. genes was not given')
        else:
            if not isinstance(genes, dict):
                raise AttributeError(f'could not set coefficients based on {genes}. genes in not a dict')
            light_keys = list(genes.keys())
            if len(light_keys) == 0:
                raise AttributeError(f'could not set coefficients based on {genes}. No light_ids found')
            if len(list(genes[light_keys[0]].keys())) != len(self.sensors):
                raise AttributeError(f'could not set coefficients based on {genes}. Size does not match number of sensors.')

            all_coefficients = []
            self.light_ids = []
            light_keys.sort()
            for lkey in light_keys:
                lcoefficients = []
                self.light_ids.append(lkey)
                sensor_keys = list(genes[lkey].keys())
                sensor_keys.sort()
                for skey in sensor_keys:
                    lcoefficients.extend(np.array(genes[lkey][skey]).flatten())
                all_coefficients.append(lcoefficients)
            self.coefficients = np.array(all_coefficients)

    def set_coefficients_from_list(self, coefficients=None):
        if coefficients is None:
            raise AttributeError(f'could not set coefficients to {coefficients}. Coefficients was not given')
        else:
            if not isinstance(coefficients, list):
                raise AttributeError(f'could not set coefficients to {coefficients}. Coefficients in not a list')
            if not isinstance(coefficients[0], list):
                raise AttributeError(f'could not set coefficients to {coefficients}. Coefficients[0] in not a list')
            if len(coefficients[0]) == 0:
                raise AttributeError(f'could not set coefficients to {coefficients}. No coefficients found')
            self.coefficients = np.array(coefficients)

    def which_light_should_be_green(self):
        comparatives = self.calculate_comparatives()
        return self.light_ids[int(np.argmax(comparatives))]

    def which_light_index_should_be_green(self):
        comparatives = self.calculate_comparatives()
        return int(np.argmax(comparatives))

    def calculate_comparatives(self):
        variables = Calculator.collect_variables(self.sensors)
        comparatives = self.coefficients @ variables
        print(comparatives)
        return comparatives

    @staticmethod
    def collect_variables(sensors):
        all_values = {}
        keys = []
        for sensor in sensors:
            vals = []
            for val in sensor.get_signal():
                vals.append(val)
                vals.append(val * val)
                vals.append(sqrt(val))
            all_values[sensor.sensor_id] = vals
            keys.append(sensor.sensor_id)

        keys.sort()
        all_variables = []
        for k in keys:
            all_variables.extend(all_values[k])
        return np.array(all_variables)
