import random
from gene_pool import GenePool
from individual import Individual


class Evolution:

    def __init__(self, gene_pool_provider=None, mutation_probability=0.05, gene_pool_size=100):
        if gene_pool_provider is None:
            self.gene_pool = GenePool()
        else:
            self.gene_pool = gene_pool_provider.get_gene_pool(size_of_gene_pool=gene_pool_size)
        self.gene_pool_size = gene_pool_size
        self.mutation_probability = mutation_probability
        print("Init Evolution")

    def number_of_individuals(self):
        return self.gene_pool.individuals.__len__()

    def randomise_gene_pool(self, number_of_individuals=1, genes_per_individual=1):
        self.gene_pool = GenePool(
            randomised=True,
            number_of_individuals=number_of_individuals,
            genes_per_individual=genes_per_individual)

    def update_gene_pool(self, new_generation=None):
        if new_generation is None:
            new_generation = self.get_next_generation()
        self.gene_pool.individuals = new_generation[:self.gene_pool_size]

    def get_next_generation(self):
        dads = self.gene_pool.individuals
        moms = self.gene_pool.individuals
        offspring = []
        for mom in moms:
            for dad in dads:
                offspring.append(Evolution.combine(mom, dad, self.mutation_probability))
        return offspring

    def print_generation(self, generation=None, generation_id='*'):
        if generation is None:
            print(self.get_next_generation())
        else:
            for i in range(0, generation.__len__()):
                print(f'%s %d - %s' % (generation_id, i, str(generation[i])))

    @staticmethod
    def combine(mom, dad, mutation_probability=0.0):
        new_genes = []
        for i in range(0, mom.genes.__len__()):
            gene_from_dad = random.randint(0, 1000) / 1000 < 0.5
            if gene_from_dad:
                new_genes.append(dad.genes[i])
            else:
                new_genes.append(mom.genes[i])

        new_individual = Individual(genes=tuple(new_genes))
        for i in range(0, new_genes.__len__()):
            if (random.randint(0, 1000) / 1000) < mutation_probability:
                new_individual.mutate(gene_index=i)
        return new_individual



