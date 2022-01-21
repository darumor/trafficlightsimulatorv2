import unittest
import numpy as np
from controller.controller1.calc import Calculator
from crossing.crossing1.sensor import Sensor
from crossing.crossing1.light import Light


class TestUnitCalculator(unittest.TestCase):

    def test_simple_calculator(self):
        sensor1 = Sensor('sensor1', signal=1)
        sensor2 = Sensor('sensor2', signal=[2, 2])
        light1 = Light('light1', signal=0)
        light2 = Light('light2', signal=[3, 3])
        coefficients = {
            "light1": {
                "sensor1": [
                    [1, 0, 0]
                ],
                "sensor2": [
                    [2, 0, 0],
                    [0, 2, 0]
                ],
                "light1": [
                    [1, 0, 0]
                ],
                "light2": [
                    [2, 1, 0],
                    [1, 1, 1]
                ]

            },
            "light2": {
                "sensor1": [
                    [1, 0, 0]
                ],
                "sensor2": [
                    [1, 1, 0],
                    [1, 1, 1]
                ],
                "light1": [
                    [1, 0, 0]
                ],
                "light2": [
                    [1, 2, 0],
                    [0, 0, 0]
                ]
            }
        }

        calculator1 = Calculator([sensor1, sensor2, light1, light2])
        calculator1.set_coefficients_from_dict(genes=coefficients)

        # 1*(1) + 0*(1)^2 + 0*sqrt(1) =                                  1
        # 2*(2) + 0*(2)^2 + 0*sqrt(2) + 0*(2) + 2*(2)^2 + 0*sqrt(2) =   12
        # 1*(0) + 0*(0)^2 + 0*sqrt(0) =                                  0
        # 2*(3) + 1*(3)^2 + 0*sqrt(3) + 1*(3) + 1*(3)^2 + 1*sqrt(3) =   28,73
        # -------------------------------------------------------------------
        #                 SUM(LIGHT1) =                                 41,73

        # 1*(1) + 0*(1)^2 + 0*sqrt(1) =                                  1
        # 1*(2) + 1*(2)^2 + 0*sqrt(2) + 1*(2) + 1*(2)^2 + 1*sqrt(2) =   13,41
        # 1*(0) + 0*(0)^2 + 0*sqrt(0) =                                  0
        # 1*(3) + 2*(3)^2 + 0*sqrt(3) + 0*(3) + 0*(3)^2 + 0*sqrt(3) =   21
        # -------------------------------------------------------------------
        #                 SUM(LIGHT2) =                                 35,41

        assert np.array_equal(np.round(calculator1.calculate_comparatives(), decimals=2), np.array([41.73, 35.41]))
        assert calculator1.which_light_should_be_green() == 'light1'

    def test_simple_calculator2(self):
        sensor1 = Sensor('sensor1', signal=1)
        sensor2 = Sensor('sensor2', signal=[2, 2])
        light1 = Light('light1', signal=0)
        light2 = Light('light2', signal=[3, 3])
        calculator2 = Calculator([sensor1, sensor2, light1, light2])
        coefficients = {
            "light1": {
                "sensor1": [
                    [1, 1, 1]
                ],
                "sensor2": [
                    [1, 1, 1],
                    [1, 1, 1]
                ],
                "light1": [
                    [1, 1, 1]
                ],
                "light2": [
                    [1, 1, 1],
                    [1, 1, 1]
                ]

            },
            "light2": {
                "sensor1": [
                    [1, 1, 1]
                ],
                "sensor2": [
                    [1, 1, 1],
                    [1, 1, 1]
                ],
                "light1": [
                    [1, 1, 1]
                ],
                "light2": [
                    [1, 1, 1],
                    [1, 1, 1]
                ]
            }
        }
        calculator2.set_coefficients_from_dict(genes=coefficients)

        # 1*(1) + 1*(1)^2 + 1*sqrt(1) =  1 + 1^2 + sqrt(1) =                                         3
        # 1*(2) + 1*(2)^2 + 1*sqrt(2) + 1*(2) + 1*(2)^2 + 1*sqrt(2) =  2 * (2 + 2^2 + sqrt(2)) =    12 + 2*sqrt(2)
        # 1*(0) + 1*(0)^2 + 1*sqrt(0) =                                                              0
        # 1*(3) + 1*(3)^2 + 1*sqrt(3) + 1*(3) + 1*(3)^2 + 1*sqrt(3) =  2 * (3 + 3^2 + sqrt(3))=     24 + 2*sqrt(3)
        # --------------------------------------------------------------------------------------------------------
        #                 SUM(LIGHTX) =                                                             45,29
        # print(f'default comparative = {3+12+24+2*sqrt(2)+2*sqrt(3)}')
        result = calculator2.calculate_comparatives()

        assert np.array_equal(np.round(result, decimals=2), np.array([45.29,  45.29]))
        assert calculator2.which_light_should_be_green() == 'light1'

    def test_simple_calculator3(self):
        sensor1 = Sensor('sensor1', signal=1)
        sensor2 = Sensor('sensor2', signal=[2, 2])
        light1 = Light('light1', signal=0)
        light2 = Light('light2', signal=[3, 3])
        coefficients = [
            [  # light1
                1, 0, 0,  # light1
                2, 1, 0, 1, 1, 1,  # light2
                1, 0, 0,  # sensor1
                2, 0, 0, 0, 2, 0  # sensor2
            ],
            [  # light2
                1, 0, 0,  # light1
                1, 2, 0, 0, 0, 0,  # light2
                1, 0, 0,  # sensor1
                1, 1, 0, 1, 1, 1  # sensor2
            ]
        ]

        calculator1 = Calculator([sensor1, sensor2, light1, light2])
        calculator1.set_coefficients_from_list(coefficients=coefficients)

        # 1*(1) + 0*(1)^2 + 0*sqrt(1) =                                  1
        # 2*(2) + 0*(2)^2 + 0*sqrt(2) + 0*(2) + 2*(2)^2 + 0*sqrt(2) =   12
        # 1*(0) + 0*(0)^2 + 0*sqrt(0) =                                  0
        # 2*(3) + 1*(3)^2 + 0*sqrt(3) + 1*(3) + 1*(3)^2 + 1*sqrt(3) =   28,73
        # -------------------------------------------------------------------
        #                 SUM(LIGHT1) =                                 41,73

        # 1*(1) + 0*(1)^2 + 0*sqrt(1) =                                  1
        # 1*(2) + 1*(2)^2 + 0*sqrt(2) + 1*(2) + 1*(2)^2 + 1*sqrt(2) =   13,41
        # 1*(0) + 0*(0)^2 + 0*sqrt(0) =                                  0
        # 1*(3) + 2*(3)^2 + 0*sqrt(3) + 0*(3) + 0*(3)^2 + 0*sqrt(3) =   21
        # -------------------------------------------------------------------
        #                 SUM(LIGHT2) =                                 35,41

        assert np.array_equal(np.round(calculator1.calculate_comparatives(), decimals=2), np.array([41.73, 35.41]))
        assert calculator1.which_light_index_should_be_green() == 0
