import unittest
from simulator.simulator import TrafficLightsSimulator


class TestUnitSimulator(unittest.TestCase):

    def test_trivial_simulation(self):
        sim = TrafficLightsSimulator(coefficients=None, graph={}, traffic_provider={},
                                     tick_rate=100, max_ticks=200, simulator_id="SIMU")
        assert sim.done is False
        sim.start()
        assert sim.done is True

