
from src.RandomNumberGeneratorInterface import RandomNumberGeneratorInterface

NOMBRE_PAR_DEFAUT_INITIAL_DE_GOBELETS = 42
QUANTITE_DE_CAFE_INITIAL_PAR_DEFAUT = 42
QUANTITE_MINIMUM_DE_CAFE = 2


class PlusAssezDeCafeException(Exception):
    pass


class MachineACafe:
    def __init__(self, rng: RandomNumberGeneratorInterface, gobelet: int=NOMBRE_PAR_DEFAUT_INITIAL_DE_GOBELETS, quantite_de_cafe: float=QUANTITE_DE_CAFE_INITIAL_PAR_DEFAUT) -> None:
        self.__gobelet = gobelet
        self.__quantite_de_cafe = quantite_de_cafe
        self.__rng = rng

    def appuyer_sur_le_bouton_servir(self) -> bool:
        if self.__rng.random_int_between_1_and_10() == 0:
            raise Exception("Pas cette fois, désolé")

        if self.__gobelet <= 0:
            raise Exception("Plus de gobelet")

        if self.__quantite_de_cafe <= QUANTITE_MINIMUM_DE_CAFE:
            raise PlusAssezDeCafeException

        return True
