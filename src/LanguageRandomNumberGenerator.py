import random

from src.RandomNumberGeneratorInterface import RandomNumberGeneratorInterface


class LanguageRandomNumberGenerator(RandomNumberGeneratorInterface):
    def random_int_between_1_and_10(self):
        return random.randrange(1, 11)