import unittest

from gene_pool_provider import GenePoolProvider


class TestGenePoolProvider(unittest.TestCase):

    def test_init(self):
        gene_pool_provider = GenePoolProvider(input_filename='../test-data/config1.json')
        assert gene_pool_provider.configuration == tuple([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        assert gene_pool_provider.gene_pool == [
            tuple([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]),
            tuple([0.2, 0.4, 0.6, 0.8, 0.10, 0.12, 0.14, 0.16, 0.18, 0.9]),
            tuple([0.3, 0.6, 0.9, 0.12, 0.15, 0.18, 0.21, 0.24, 0.27, 0.8]),
            tuple([0.4, 0.8, 0.12, 0.16, 0.20, 0.24, 0.28, 0.32, 0.36, 0.7]),
            tuple([0.5, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.6])
        ]

    def test_get_gene_pool(self):
        gene_pool_provider = GenePoolProvider(input_filename='../test-data/config2.json', input_starting_configuration_key='onlyConfiguration')
        assert gene_pool_provider.configuration == tuple([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
        gene_pool = gene_pool_provider.get_gene_pool(size_of_gene_pool=5)
        assert gene_pool.individuals.__len__() == 5
