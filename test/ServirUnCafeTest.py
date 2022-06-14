import unittest

from src.LanguageRandomNumberGenerator import LanguageRandomNumberGenerator
from src.MachineACafe import MachineACafe
from utilities.builder.MachineACafeBuilder import MachineACafeBuilder
from utilities.FixedValueRandomNumberGenerator import FixedValueRandomNumberGenerator

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

    def test_pas_de_chance(self):
        rng = FixedValueRandomNumberGenerator(0)
        machine = MachineACafeBuilder()\
            .ayant_un_rng_defini(rng)\
            .build()

        with self.assertRaises(Exception):
            machine.appuyer_sur_le_bouton_servir()


if __name__ == '__main__':
    unittest.main()
