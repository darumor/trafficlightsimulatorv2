import unittest
from evolution import Individual


class TestIndividual(unittest.TestCase):

    def test_init(self):
        c = Individual()
        assert c.genes == tuple([1.0])

        c = Individual(randomised=False, size=5)
        assert c.genes == tuple([1.0, 1.0, 1.0, 1.0, 1.0])
        c = Individual(randomised=False, size=9, genes=(0.1111, 0.22, 0.3, 0.43))
        assert c.genes == tuple([0.1111, 0.22, 0.3, 0.43])

        c = Individual(randomised=True)
        assert c.genes.__len__() == 1
        c = Individual(randomised=True, size=5)
        assert c.genes.__len__() == 5
        c = Individual(randomised=True, size=5, genes=(0.1111, 0.22, 0.3, 0.43))
        assert c.genes.__len__() == 5
