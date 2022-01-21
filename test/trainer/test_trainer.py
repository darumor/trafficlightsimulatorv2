import unittest
from trainer import Trainer
from evolution import GenePoolProvider
from simulator import TrafficLightsSimulator
from analyser import RandomAnalyser


class TestTrainer(unittest.TestCase):

    def test_init(self):
        gpp = GenePoolProvider(number_of_weights=5)
        sim = TrafficLightsSimulator()
        t = Trainer(analyser_instance=RandomAnalyser(), simulator_instance=sim, gene_pool_provider=gpp, mutation_probability=0.5)
        t.start(number_of_generations=5)


