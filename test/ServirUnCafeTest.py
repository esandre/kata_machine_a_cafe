import unittest

from src.MachineACafe import MachineACafe

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
        machine = MachineACafe()

        expresso_servi = machine.appuyer_sur_le_bouton_servir()
        self.assertTrue(expresso_servi)

    def test_plus_de_gobelet(self):
        machine = MachineACafe(gobelet=0)

        with self.assertRaises(Exception):
            machine.appuyer_sur_le_bouton_servir()


if __name__ == '__main__':
    unittest.main()
