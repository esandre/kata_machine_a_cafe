from QuantiteCafe import QuantiteCafe
from src.MachineACafe import MachineACafe


class MachineACafeBuilder:
    def __init__(self):
        self.__nombre_gobelets = 1
        self.__quantite_de_cafe = QuantiteCafe(2)

    def ayant_un_nombre_de_gobelets_defini(self, nombre_gobelets: int):
        self.__nombre_gobelets = nombre_gobelets
        return self

    def ayant_une_quantité_de_cafe_definie(self, quantite_de_cafe: QuantiteCafe):
        self.__quantite_de_cafe = quantite_de_cafe
        return self

    def build(self) -> MachineACafe:
        return MachineACafe(self.__nombre_gobelets, self.__quantite_de_cafe)



