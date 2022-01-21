import random
from individual import Individual


class GenePool:

    def __init__(self, randomised=False, number_of_individuals=1, genes_per_individual=1, gene_pool=None):
        if randomised:
            self.individuals = self.random_gene_pool(number_of_individuals, genes_per_individual)
        elif gene_pool is None:
            self.individuals = self.default_gene_pool(number_of_individuals, genes_per_individual)
        else:
            self.individuals = self.create_individuals(gene_pool)
        print("Init GenePool")
        self.print_individuals()

    def print_individuals(self):
        for i in range(0, self.individuals.__len__()):
            print(f'%d - %s' % (i, str(self.individuals[i])))

    @staticmethod
    def random_gene_pool(number_of_individuals=1, genes_per_individual=1):
        gene_pool = []
        for i in range(0, number_of_individuals):
            gene_pool.append(Individual(randomised=True, size=genes_per_individual))
        return gene_pool

    @staticmethod
    def default_gene_pool(number_of_individuals=1, genes_per_individual=1):
        gene_pool = []
        for i in range(0, number_of_individuals):
            gene_pool.append(Individual(size=genes_per_individual))
        print("--Default GenePool %s" % gene_pool)
        return gene_pool

    @staticmethod
    def create_individuals(gene_pool=None):
        if gene_pool is None:
            gene_pool = [tuple([1.0])]
        individuals = []
        for genes in gene_pool:
            individuals.append(Individual(genes=genes))
        return individuals

    @staticmethod
    def create_gene_pool(original_genes, size_of_gene_pool=1, mutation_probability=0.05):
        gene_pool = [original_genes]
        genes = original_genes
        print("original genes %s" % str(original_genes))
        for i in range(0, size_of_gene_pool - 1):
            mutant = Individual(genes=genes)
            print(str(mutant))
            for j in range(0, genes.__len__()):
                if (random.randint(0, 1000) / 1000) < mutation_probability:
                    mutant.mutate(gene_index=j)
            gene_pool.append(mutant.genes)
        return GenePool(gene_pool=gene_pool)
