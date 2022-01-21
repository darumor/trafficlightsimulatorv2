import unittest
from evolution import Evolution, GenePool
from evolution import Individual
from gene_pool_provider import GenePoolProvider


class TestEvolution(unittest.TestCase):

    def test_init(self):
        e = Evolution()
        assert e.gene_pool.individuals.__len__() == 1
        assert e.gene_pool.individuals[0].genes == tuple([1.0])

        i1 = (0.2, 0.4, 0.6, 0.8)
        i2 = (0.1, 0.3, 0.5, 0.7)
        i3 = (0.11, 0.22, 0.88, 0.99)
        i4 = (0.33, 0.55, 0.44, 0.77)
        e = Evolution(gene_pool=GenePool(gene_pool=[i1, i2, i3, i4]), mutation_probability=0.0)

        assert e.gene_pool.individuals[0].genes == (0.2, 0.4, 0.6, 0.8)
        assert e.gene_pool.individuals[1].genes == (0.1, 0.3, 0.5, 0.7)
        assert e.gene_pool.individuals[2].genes == (0.11, 0.22, 0.88, 0.99)
        assert e.gene_pool.individuals[3].genes == (0.33, 0.55, 0.44, 0.77)

    def test_randomise(self):
        e = Evolution()
        assert e.gene_pool.individuals.__len__() == 1
        assert e.gene_pool.individuals[0].genes == tuple([1.0])

        e.randomise_gene_pool(number_of_individuals=3, genes_per_individual=3)
        assert e.gene_pool.individuals.__len__() == 3
        assert e.gene_pool.individuals[0].genes.__len__() == 3
        assert e.gene_pool.individuals[1].genes.__len__() == 3
        assert e.gene_pool.individuals[2].genes.__len__() == 3

    def test_combine(self):
        mom = Individual(genes=(0.2, 0.4, 0.6, 0.8, 0.99, 0.17))
        dad = Individual(genes=(0.1, 0.3, 0.5, 0.7, 0.12, 0.15))
        kid = Evolution.combine(mom, dad)
        assert kid.genes.__len__() == 6
        assert [0.1, 0.2].__contains__(kid.genes[0])
        assert [0.3, 0.4].__contains__(kid.genes[1])
        assert [0.5, 0.6].__contains__(kid.genes[2])
        assert [0.7, 0.8].__contains__(kid.genes[3])
        assert [0.99, 0.12].__contains__(kid.genes[4])
        assert [0.17, 0.15].__contains__(kid.genes[5])

        kid = Evolution.combine(mom, dad, mutation_probability=0.4)
        assert kid.genes.__len__() == 6
        assert not [0.1, 0.2].__contains__(kid.genes[0]) or \
            not [0.3, 0.4].__contains__(kid.genes[1]) or \
            not [0.5, 0.6].__contains__(kid.genes[2]) or \
            not [0.7, 0.8].__contains__(kid.genes[3]) or \
            not [0.99, 0.12].__contains__(kid.genes[4]) or \
            not [0.17, 0.15].__contains__(kid.genes[5])

        assert [0.1, 0.2].__contains__(kid.genes[0]) or \
               [0.3, 0.4].__contains__(kid.genes[1]) or \
               [0.5, 0.6].__contains__(kid.genes[2]) or \
               [0.7, 0.8].__contains__(kid.genes[3]) or \
               [0.99, 0.12].__contains__(kid.genes[4]) or \
               [0.17, 0.15].__contains__(kid.genes[5])

    def test_get_next_generation(self):
        i1 = (0.2, 0.4, 0.6, 0.8)
        i2 = (0.1, 0.3, 0.5, 0.7)
        i3 = (0.11, 0.22, 0.88, 0.99)
        i4 = (0.33, 0.55, 0.44, 0.77)
        e = Evolution(gene_pool=GenePool(gene_pool=[i1, i2, i3, i4]))
        offspring = e.get_next_generation(mutation_probability=0.0)

        assert offspring.__len__() == 16
        for kid in offspring:
            assert kid.genes.__len__() == 4
            [0.2, 0.1, 0.11, 0.33].__contains__(kid.genes[0])
            [0.4, 0.3, 0.22, 0.55].__contains__(kid.genes[1])
            [0.6, 0.5, 0.88, 0.44].__contains__(kid.genes[2])
            [0.8, 0.7, 0.99, 0.77].__contains__(kid.genes[3])

    def test_update_gene_pool(self):
        i1 = (0.2, 0.4, 0.6, 0.8)
        i2 = (0.1, 0.3, 0.5, 0.7)
        i3 = (0.11, 0.22, 0.88, 0.99)
        i4 = (0.33, 0.55, 0.44, 0.77)

        e = Evolution(gene_pool=GenePool(gene_pool=[i1, i2, i3, i4]), mutation_probability=0.0)
        offspring = e.get_next_generation(mutation_probability=0.0)
        e.update_gene_pool(new_generation=offspring[:4])
        new_generation = e.gene_pool.individuals

        assert new_generation.__len__() == 4
        assert new_generation[0].genes == offspring[0].genes
        assert new_generation[1].genes == offspring[1].genes
        assert new_generation[2].genes == offspring[2].genes
        assert new_generation[3].genes == offspring[3].genes

        e.update_gene_pool(new_generation=offspring[:2])
        new_generation = e.gene_pool.individuals
        assert new_generation == offspring[:2]

    def test_evolution_loop(self):
        e = Evolution(mutation_probability=0.2, max_gene_pool_size=10)
        e.randomise_gene_pool(number_of_individuals=10, genes_per_individual=10)
        e.update_gene_pool()
        e.gene_pool.print_individuals()
        e.update_gene_pool()
        e.gene_pool.print_individuals()
        e.update_gene_pool()
        e.gene_pool.print_individuals()
        e.update_gene_pool()
        e.gene_pool.print_individuals()
        assert e.gene_pool.individuals.__len__() == 10

    def test_create_evolution_from_config(self):
        gene_pool_provider = GenePoolProvider(input_filename='../test-data/config1.json')
        evolution = Evolution(
            gene_pool=gene_pool_provider.get_gene_pool(size_of_gene_pool=3),
            mutation_probability=0.5,
            max_gene_pool_size=5)
        assert evolution.gene_pool.individuals.__len__() == 3
        offspring = evolution.get_next_generation()
        assert offspring.__len__() == 9
        evolution.update_gene_pool(offspring)
        assert evolution.gene_pool.individuals.__len__() == 5
        offspring = evolution.get_next_generation()
        assert offspring.__len__() == 25
        evolution.update_gene_pool(offspring)
        assert evolution.gene_pool.individuals.__len__() == 5
