import random

from src.RandomNumberGeneratorInterface import RandomNumberGeneratorInterface

NOMBRE_PAR_DEFAUT_INITIAL_DE_GOBELETS = 42


class MachineACafe:
    def __init__(self, rng: RandomNumberGeneratorInterface, gobelet=NOMBRE_PAR_DEFAUT_INITIAL_DE_GOBELETS):
        self.__gobelet = gobelet
        self.__rng = rng

    def appuyer_sur_le_bouton_servir(self) -> bool:
        if self.__rng.random_int_between_1_and_10() == 0:
            raise Exception ("Pas cette fois, désolé")

        if self.__gobelet <= 0:
            raise Exception ("Plus de gobelet")
        return True
