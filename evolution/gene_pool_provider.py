import json
import random

from evolution import GenePool


class GenePoolProvider:

    def __init__(self, input_filename=None, input_starting_configuration_key='bestConfiguration', input_gene_pool_key='genePool', number_of_weights=1):
        print("Init GenePoolProvider")
        self.configuration = None
        self.gene_pool = None
        if input_filename is not None:
            self.read_input_file(input_filename, input_starting_configuration_key, input_gene_pool_key)
        else:
            self.configuration = GenePoolProvider.generate_random_configuration(number_of_weights)

    def read_input_file(self, filename=None, input_starting_configuration_key='bestConfiguration', input_gene_pool_key='genePool'):
        with open(filename, 'r') as f:
            orig_config = json.load(f)
        if orig_config is not None:
            self.configuration = tuple(orig_config[input_starting_configuration_key])
            if orig_config.keys().__contains__(input_gene_pool_key):
                pool = orig_config[input_gene_pool_key]
                if pool is not None:
                    self.gene_pool = []
                    for arr in pool:
                        self.gene_pool.append(tuple(arr))

    def get_gene_pool(self, size_of_gene_pool=5, mutation_probability=0.05):
        if self.gene_pool is None:
            return GenePool.create_gene_pool(original_genes=self.configuration, size_of_gene_pool=size_of_gene_pool, mutation_probability=mutation_probability)
        else:
            return GenePool(gene_pool=self.gene_pool[:size_of_gene_pool])

    @staticmethod
    def generate_random_configuration(number_of_weights=1):
        weights = []
        for i in range(0, number_of_weights):
            weights.append(random.randint(0, 1000) / 1000)
        return tuple(weights)


