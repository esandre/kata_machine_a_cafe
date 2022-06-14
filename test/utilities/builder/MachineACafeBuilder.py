from src.MachineACafe import MachineACafe
from src.RandomNumberGeneratorInterface import RandomNumberGeneratorInterface

from utilities.FixedValueRandomNumberGenerator import FixedValueRandomNumberGenerator
from utilities.StubRandomNumberGenerator import StubRandomNumberGenerator


class MachineACafeBuilder:
    def __init__(self):
        self.__nombre_gobelets = None
        self.__rng = StubRandomNumberGenerator()

    def ayant_un_nombre_de_gobelets_defini(self, nombre_gobelets: int):
        self.__nombre_gobelets = nombre_gobelets
        return self

    def ayant_un_rng_defini(self, rng: RandomNumberGeneratorInterface):
        self.__rng = rng
        return self

    def build(self) -> MachineACafe:
        return MachineACafe(self.__rng) \
            if self.__nombre_gobelets is None \
            else MachineACafe(self.__rng, self.__nombre_gobelets)
