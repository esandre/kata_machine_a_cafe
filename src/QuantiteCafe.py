from ValueOutsideOfBoundsException import ValueOutsideOfBoundsException


class QuantiteCafe:
    def __init__(self, quantite_brute: int):
        if isinstance(quantite_brute, int) and quantite_brute < 0: raise ValueOutsideOfBoundsException()
        self.__inner = quantite_brute

    def est_suffisante_pour_un_expresso(self) -> bool:
        return self.__inner >= 2