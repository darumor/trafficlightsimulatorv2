from evolution import Evolution
from simulator import TrafficLightsSimulator
from gene_pool_provider import GenePoolProvider
from analyser import Analyser

config = {
    "config_file": "../data/crossing1/config1.json",
    "crossing_structure_file": "../data/crossing1/structure1.json",
    "mutation_probability": 0.05,
    "number_of_generations": 5,
    'size_of_gene_pool': 5
}


class Trainer:

    def __init__(self, analyser_instance, gene_pool_provider=None, gene_pool_size=config['size_of_gene_pool'], mutation_probability=None):
        self.analyser = analyser_instance
        self.gene_pool_size = gene_pool_size
        self.evolution = Evolution(
            gene_pool_provider=gene_pool_provider,
            mutation_probability=mutation_probability,
            gene_pool_size=self.gene_pool_size)
        print("Init Trainer")

    def start(self, number_of_generations=config["number_of_generations"]):
        for i in range(0, number_of_generations):

            variations = self.evolution.get_next_generation()
            sorted_individuals = self.analyser.analyse(variations=variations, simulator=simulator)
            self.evolution.print_generation(sorted_individuals[:self.gene_pool_size], str(i))
            self.evolution.update_gene_pool(sorted_individuals[:self.gene_pool_size])


if __name__ == '__main__':
    print("Starting Trainer...")
    analyser = Analyser()
    trainer = Trainer(analyser,
                      gene_pool_provider=GenePoolProvider(input_filename=config["config_file"]),
                      mutation_probability=config["mutation_probability"])
    trainer.start(number_of_generations=config["number_of_generations"])




