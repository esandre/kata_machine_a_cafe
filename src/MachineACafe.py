from PlusAssezDeCafeException import PlusAssezDeCafeException
from QuantiteCafe import QuantiteCafe

NOMBRE_PAR_DEFAUT_INITIAL_DE_GOBELETS = 42
QUANTITE_DE_CAFE_INITIAL_PAR_DEFAUT = QuantiteCafe(42)
QUANTITE_MINIMUM_DE_CAFE = 2


class MachineACafe:
    def __init__(self,
                 nombre_initial_gobelets: int,
                 quantite_initiale_de_cafe: QuantiteCafe,
                 quantite_initiale_dargent: int) -> None:

        self.__gobelet = nombre_initial_gobelets
        self.__quantite_de_cafe = quantite_initiale_de_cafe
        self.__quantite_dargent = quantite_initiale_dargent

    def appuyer_sur_le_bouton_servir(self) -> bool:
        if self.__gobelet <= 0:
            raise Exception("Plus de gobelet")

        if not self.__quantite_de_cafe.est_suffisante_pour_un_expresso():
            raise PlusAssezDeCafeException

        if self.__quantite_dargent < 40:
            raise Exception('Pas assez dargent')

        return True
