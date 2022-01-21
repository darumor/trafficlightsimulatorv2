import unittest
from crossing.crossing1.crossing import Crossing
from simulator.ticker import Ticker
from traffic.car import Car


class TestUnitCrossing(unittest.TestCase):

    def test_trivial_crossing(self):
        ticker = Ticker(100, 200)
        cross = Crossing(ticker=ticker, graph=None)
        car = Car("id-1", 50, "entry-id-1", "exit-id-2")
        cross.handle_batch([car])
        ticker.start()
        ticker.join()
        assert cross.cars.__contains__(car)



