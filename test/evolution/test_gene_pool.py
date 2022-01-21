import unittest
from evolution import GenePool


class TestGenePool(unittest.TestCase):

    def test_init(self):
        g = GenePool()
        assert g.individuals.__len__() == 1
        assert g.individuals[0].genes == tuple([1.0])

        g = GenePool(randomised=False, number_of_individuals=5)
        assert g.individuals.__len__() == 5
        assert g.individuals[0].genes == tuple([1.0])
        assert g.individuals[1].genes == tuple([1.0])
        assert g.individuals[2].genes == tuple([1.0])
        assert g.individuals[3].genes == tuple([1.0])
        assert g.individuals[4].genes == tuple([1.0])

        g = GenePool(randomised=False, genes_per_individual=5)
        assert g.individuals.__len__() == 1
        assert g.individuals[0].genes == tuple([1.0, 1.0, 1.0, 1.0, 1.0])

        g = GenePool(randomised=False, number_of_individuals=3, genes_per_individual=3)
        assert g.individuals.__len__() == 3
        assert g.individuals[0].genes == tuple([1.0, 1.0, 1.0])
        assert g.individuals[1].genes == tuple([1.0, 1.0, 1.0])
        assert g.individuals[2].genes == tuple([1.0, 1.0, 1.0])

        test_genes = []
        g = GenePool(randomised=False, number_of_individuals=3, genes_per_individual=3, gene_pool=test_genes)
        assert g.individuals.__len__() == 0
        assert g.individuals == []

        test_genes = [(0.1111, 0.22, 0.3, 0.43),
                        (0.2222, 0.44, 0.2, 0.43),
                        (0.3333, 0.66, 0.1, 0.43)]
        g = GenePool(randomised=False, number_of_individuals=3, genes_per_individual=3, gene_pool=test_genes)
        assert g.individuals.__len__() == 3
        assert g.individuals[0].genes == tuple([0.1111, 0.22, 0.3, 0.43])
        assert g.individuals[1].genes == tuple([0.2222, 0.44, 0.2, 0.43])
        assert g.individuals[2].genes == tuple([0.3333, 0.66, 0.1, 0.43])

        g = GenePool(randomised=True)
        assert g.individuals.__len__() == 1
        assert g.individuals[0].genes.__len__() == 1

        g = GenePool(randomised=True, number_of_individuals=5)
        assert g.individuals.__len__() == 5
        assert g.individuals[0].genes.__len__() == 1
        assert g.individuals[1].genes.__len__() == 1
        assert g.individuals[2].genes.__len__() == 1
        assert g.individuals[3].genes.__len__() == 1
        assert g.individuals[4].genes.__len__() == 1

        g = GenePool(randomised=True, genes_per_individual=5)
        assert g.individuals.__len__() == 1
        assert g.individuals[0].genes.__len__() == 5

        g = GenePool(randomised=True, number_of_individuals=3, genes_per_individual=3)
        assert g.individuals.__len__() == 3
        assert g.individuals[0].genes.__len__() == 3
        assert g.individuals[1].genes.__len__() == 3
        assert g.individuals[2].genes.__len__() == 3

        test_genes = []
        g = GenePool(randomised=True, number_of_individuals=3, genes_per_individual=3, gene_pool=test_genes)
        assert g.individuals.__len__() == 3
        assert g.individuals[0].genes.__len__() == 3
        assert g.individuals[1].genes.__len__() == 3
        assert g.individuals[2].genes.__len__() == 3

        test_genes = [(0.1111, 0.22, 0.3, 0.43),
                        (0.2222, 0.44, 0.2, 0.43),
                        (0.3333, 0.66, 0.1, 0.43)]

        g = GenePool(randomised=True, number_of_individuals=3, genes_per_individual=3, gene_pool=test_genes)
        assert g.individuals.__len__() == 3
        assert g.individuals[0].genes.__len__() == 3
        assert g.individuals[1].genes.__len__() == 3
        assert g.individuals[2].genes.__len__() == 3
