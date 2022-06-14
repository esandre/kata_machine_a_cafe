import unittest

from PlusAssezDeCafeException import PlusAssezDeCafeException
from QuantiteCafe import QuantiteCafe
from utilities.builder.MachineACafeBuilder import MachineACafeBuilder

'''
    QUAND on appuie sur le bouton "Servir"
    ALORS on obtient un expresso

    ETANT DONNE qu'il n'y a plus de gobelet
    QUAND on appuie sur le bouton "Servir"
    ALORS la machine affiche le message "Plus de gobelets"

    ETANT DONNE qu'il n'y a plus de café
    QUAND on appuie sur le bouton "Servir"
    ALORS la machine affiche le message "Plus de café"

    ETANT DONNE qu'il n'y a plus de café ni de gobelet
    QUAND on appuie sur le bouton "Servir"
    ALORS la machine affiche le message "Plus de café ni de gobelet"
    
    ETANT DONNE qu'il y a <x> cts sur la machine
    ET que <x> est supérieur ou égal à 40
    QUAND on appuie sur le bouton "Servir"
    ALORS la machine affiche le message "Pas assez d'argent"
'''


class ServirUnCafeTest(unittest.TestCase):
    def test_servir_expresso(self):
        machine = MachineACafeBuilder().build()

        expresso_servi = machine.appuyer_sur_le_bouton_servir()
        self.assertTrue(expresso_servi)

    def test_plus_de_gobelet(self):
        machine = MachineACafeBuilder()\
            .ayant_un_nombre_de_gobelets_defini(0)\
            .build()

        with self.assertRaises(Exception):
            machine.appuyer_sur_le_bouton_servir()

    def test_plus_assez_de_cafe(self):
        machine = MachineACafeBuilder() \
            .ayant_une_quantité_de_cafe_definie(QuantiteCafe(0)) \
            .build()

        with self.assertRaises(PlusAssezDeCafeException):
            machine.appuyer_sur_le_bouton_servir()

    def test_pas_assez_dargent(self):
        machine = MachineACafeBuilder().ayant_une_quantité_dargent_definie(35).build()

        with self.assertRaises(Exception):
            machine.appuyer_sur_le_bouton_servir()

if __name__ == '__main__':
    unittest.main()
