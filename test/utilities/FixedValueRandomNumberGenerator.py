from src.RandomNumberGeneratorInterface import RandomNumberGeneratorInterface


class FixedValueRandomNumberGenerator(RandomNumberGeneratorInterface):
    def __init__(self, fixed_value: int):
        self.fixed_value = fixed_value

    def random_int_between_1_and_10(self):
        return self.fixed_value
