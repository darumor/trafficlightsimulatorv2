import unittest
import main


class TestSmoke(unittest.TestCase):

    def test_smoke(self):
        smoke = "No smoke detected"
        assert main.smoke(smoke) == smoke

