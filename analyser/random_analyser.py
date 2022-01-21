import random
from analyser import Analyser


class RandomAnalyser(Analyser):
    def __init__(self):
        super().__init__()
        print('init RandomAnalyser')

    def analyse(self, variations, number_of_the_fittest=5, simulator=None):
        print('randomizing')
        to_return = []
        for variation in variations:
            i = random.randint(0, to_return.__len__())
            to_return.insert(i, variation)
        to_return = to_return[:number_of_the_fittest]
        return to_return


