import random
import json
import numpy as np


class GenePoolGenerator:

    def __init__(self, crossing_structure=None, number_of_variants=1):
        if crossing_structure is None:
            raise AttributeError("crossing_structure was not given")
        self.crossing_structure = crossing_structure
        self.number_of_variants = number_of_variants

    @staticmethod
    def get_random_weight():
        return random.randint(-1000, 1000) / 1000

    def convert_to_coefficients(self, gene_pool=None):
        if gene_pool is None or "genePool" not in gene_pool:
            raise AttributeError("Valid parameters not given")

        light_keys = list(gene_pool["genePool"].keys())
        all_coefficients = []
        light_keys.sort()
        for lkey in light_keys:
            lcoefficients = []
            sensor_keys = list(gene_pool["genePool"][lkey].keys())
            sensor_keys.sort()
            for skey in sensor_keys:
                lcoefficients.extend(np.array(gene_pool["genePool"][lkey][skey]).flatten())
            all_coefficients.append(lcoefficients)
        return all_coefficients

    def convert_from_coefficients(self, coefficients=None):
        if coefficients is None:
            raise AttributeError("coefficients was not given")
        gene_pool = {
            "name": self.crossing_structure["name"]
        }
        light_ids = []
        sensor_ids = []
        nodes = {}
        for node in self.crossing_structure["nodes"]:
            if node["light"]:
                light_ids.append(node["id"])
            if node["sensor"]:
                sensor_ids.append(node["id"])
            nodes[node["id"]] = node

        light_ids.sort()
        sensor_ids.sort()
        coefficient_light_pointer = 0
        pool = {}
        for light_id in light_ids:
            light_weights = {}
            coefficient_pointer = 0
            for sensor_id in sensor_ids:
                sensor = nodes[sensor_id]
                sensor_weights = []
                for i in range(0, sensor["signalLength"]):
                    variants = []
                    for j in range(0, self.number_of_variants):
                        variants.append(coefficients[coefficient_light_pointer][coefficient_pointer])
                        coefficient_pointer += 1
                    sensor_weights.append(variants)
                light_weights[sensor_id] = sensor_weights
            pool[light_id] = light_weights
            coefficient_light_pointer += 1
        gene_pool["genePool"] = pool
        return gene_pool

    def generate_gene_pool(self):
        gene_pool = {
            "name": self.crossing_structure["name"]
        }
        pool = {}
        nodes = self.crossing_structure["nodes"]
        for light_node in nodes:
            if light_node["light"]:
                light_weights = {}
                light_id = light_node["id"]
                for sensor_node in nodes:
                    if sensor_node["sensor"]:
                        sensor_weights = []
                        sensor_id = sensor_node["id"]

                        if "signalLength" in sensor_node:
                            signal_length = sensor_node["signalLength"]
                        else:
                            signal_length = 1

                        for i in range(0, signal_length):
                            variants = []
                            for j in range(0, self.number_of_variants):
                                variants.append(GenePoolGenerator.get_random_weight())
                            sensor_weights.append(variants)
                        light_weights[sensor_id] = sensor_weights
                pool[light_id] = light_weights
        gene_pool["genePool"] = pool
        return gene_pool

