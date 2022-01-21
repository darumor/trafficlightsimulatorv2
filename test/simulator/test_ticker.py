import unittest
from simulator.ticker import Ticker


class TestUnitTicker(unittest.TestCase):

    def test_trivial_tick(self):
        tickee = self.TrivialTickee()
        ticker = Ticker(1000, 1000)
        ticker.register_entity(tickee)
        ticker.start()
        ticker.join()
        assert tickee.value == 1000

    def test_run_some(self):
        tickee = self.TrivialTickee()
        ticker = Ticker(1000, 1000)
        ticker.register_entity(tickee)
        ticker.run_some(200)
        assert tickee.value == 200
        ticker.run_some(400)
        assert tickee.value == 600
        assert not ticker.running

    class TrivialTickee:

        def __init__(self):
            self.value = 0

        def tick(self, value=None):
            if value is not None:
                self.value = value
            else:
                self.value = self.value + 1
