from abc import abstractmethod


class RandomNumberGeneratorInterface:
    @abstractmethod
    def random_int_between_1_and_10(self):
        pass
