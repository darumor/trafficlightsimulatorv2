import random

import numpy as np


class Individual:

    def __init__(self, randomised=False, size=1, genes=None):

        if randomised:
            self.genes = self.random_individual(size)
        elif genes is None:
            self.genes = self.default_individual(size)
        else:
            self.genes = genes

    def __str__(self):
        return "Individual %s" % str(self.genes)

    def set_genes_from_matrix(self, matrix):
        self.genes = np.matrix(matrix).flatten().tolist()[0]

    # matrix_dimensions should be a tuple describing the matrix dimensions -> (rows, columns), which translates to (lights, coefficients)
    def genes_as_matrix(self, matrix_dimensions=None):
        if matrix_dimensions is None:
            return self.genes
        elif not isinstance(matrix_dimensions, tuple):
            raise AttributeError('matrix_dimensions should be a tuple with matrix dimensions -> (rows, columns), which translates to (lights, coefficients), eg. (4, 12)')
        else:
            rows = matrix_dimensions[0]
            columns = matrix_dimensions[1]
            if len(self.genes) != rows * columns:
                raise AttributeError('matrix_dimensions should match the number of genes. eg (4, 12) -> 4*12=48 genes')
            return np.array(self.genes).reshape((rows, columns)).tolist()

    @staticmethod
    def random_individual(size=1):
        genes = []
        for i in range(0, size):
            genes.append(Individual.random_gene())
        return tuple(genes)

    @staticmethod
    def default_individual(size=1):
        genes = []
        for i in range(0, size):
            genes.append(1.0)
        return tuple(genes)

    @staticmethod
    def random_gene():
        return random.randint(-1000, 1000) / 1000

    def mutate(self, gene_index=None):
        print('mutating')
        if gene_index is None:
            gene_index = random.randint(0, self.genes.__len__())

        new_genes = []
        for i in range(0, self.genes.__len__()):
            if i == gene_index:
                new_gene = self.random_gene()
                print(f'old gene #{i}: {self.genes[i]}, new gene -> {new_gene}')
                new_genes.append(new_gene)
            else:
                new_genes.append(self.genes[i])
        self.genes = tuple(new_genes)

