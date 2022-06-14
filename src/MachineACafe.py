NOMBRE_PAR_DEFAUT_INITIAL_DE_GOBELETS = 42


class MachineACafe:
    def __init__(self, gobelet=NOMBRE_PAR_DEFAUT_INITIAL_DE_GOBELETS):
        self.__gobelet = gobelet

    def appuyer_sur_le_bouton_servir(self) -> bool:
        if self.__gobelet <= 0:
            raise Exception ("Plus de gobelet")
        return True
