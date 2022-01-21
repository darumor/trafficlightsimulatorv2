import unittest

from traffic import TrafficProvider


class TestTrafficProvider(unittest.TestCase):

    def test_trivial_input_file(self):
        provider = TrafficProvider(input_filename='../test-data/trivial_traffic.json')
        batch = provider.get_next_traffic_batch(0)
        assert len(batch) == 0
        batch = provider.get_next_traffic_batch(20)
        assert len(batch) == 1
        assert batch[0].car_id == "1"
        self.assertRaises(Exception, provider.get_next_traffic_batch, 90)

    def test_random_traffic(self):
        provider = TrafficProvider(entries=["entry-id-1", "entry-id-2"], exits=["exit-id-1", "exit-id-2"],
                                   number_of_cars=5, max_ticks_in_between=100)
        batch = provider.get_next_traffic_batch(1000)
        assert len(batch) == 5

    def test_basic_traffic(self):
        provider = TrafficProvider(input_filename='../test-data/traffic1.json')
        batch = provider.get_next_traffic_batch(0)
        assert len(batch) == 0
        batch = provider.get_next_traffic_batch(200)
        assert len(batch) == 9
        batch = provider.get_next_traffic_batch(500)
        assert len(batch) == 11
        batch = provider.get_next_traffic_batch(1000)
        assert len(batch) == 1
        self.assertRaises(Exception, provider.get_next_traffic_batch, 500)
