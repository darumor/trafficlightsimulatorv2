import json
import unittest
from evolution.gene_pool_generator import GenePoolGenerator


class TestGenerator(unittest.TestCase):

    def test_convertions(self):
        crossing_structure_json_file_name = "../../data/crossing1/structure1.json"
        with open(crossing_structure_json_file_name, 'r') as f:
            crossing_structure = json.load(f)

        generator = GenePoolGenerator(crossing_structure=crossing_structure, number_of_variants=3)
        gp = generator.generate_gene_pool()
        coefficients = generator.convert_to_coefficients(gene_pool=gp)
        gp2 = generator.convert_from_coefficients(coefficients=coefficients)
        assert gp == gp2

    def test_file_input_output(self):
        crossing_structure_json_file_name = "../../data/crossing1/structure1.json"
        gene_pool_json_file_name = "../test-data/genepool1.json"
        with open(crossing_structure_json_file_name, 'r') as f:
            structure = json.load(f)
        generator = GenePoolGenerator(crossing_structure=structure, number_of_variants=3)
        gp = generator.generate_gene_pool()

        with open(gene_pool_json_file_name, 'w') as f:
            json.dump(gp, f, indent=4, sort_keys=True)
        with open(gene_pool_json_file_name, 'r') as f:
            gp2 = json.load(f)
        assert gp == gp2
