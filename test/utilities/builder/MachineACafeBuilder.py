from src.MachineACafe import MachineACafe
from src.RandomNumberGeneratorInterface import RandomNumberGeneratorInterface

from utilities.StubRandomNumberGenerator import StubRandomNumberGenerator


class MachineACafeBuilder:
    def __init__(self):
        self.__nombre_gobelets = None
        self.__quantite_de_cafe = None
        self.__rng = StubRandomNumberGenerator()

    def ayant_un_nombre_de_gobelets_defini(self, nombre_gobelets: int):
        self.__nombre_gobelets = nombre_gobelets
        return self

    def ayant_une_quantité_de_cafe_definie(self, quantite_de_cafe: float):
        self.__quantite_de_cafe = quantite_de_cafe
        return self

    def ayant_un_rng_defini(self, rng: RandomNumberGeneratorInterface):
        self.__rng = rng
        return self

    def build(self) -> MachineACafe:
        if self.__nombre_gobelets is None and self.__quantite_de_cafe is None:
            return MachineACafe(self.__rng)
        elif self.__nombre_gobelets is None and self.__quantite_de_cafe is not None:
            return MachineACafe(self.__rng, quantite_de_cafe=self.__quantite_de_cafe)
        elif self.__nombre_gobelets is not None and self.__quantite_de_cafe is None:
            return MachineACafe(self.__rng, gobelet=self.__nombre_gobelets)
        else:
            return MachineACafe(self.__rng, gobelet=self.__nombre_gobelets, quantite_de_cafe=self.__quantite_de_cafe)



