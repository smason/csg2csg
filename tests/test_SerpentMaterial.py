import unittest

from csg2csg.SerpentMaterialCard import SerpentMaterialCard
from csg2csg.SerpentInput import SerpentInput


class TestSerpentMaterial(unittest.TestCase):
    def test_serpent_material(self):
        string = (
            "29063 6.917000e-01 \n"
            "29065.31c 3.083000e-01 \n"
        )
        number = 1
        name = "copper"
        density = 8.93
        matcard = SerpentMaterialCard(number, name, density, string)

        assert matcard.density == density
        assert matcard.material_number == number
        assert matcard.material_name == name

        assert matcard.composition_dictionary == {
            "29063": 6.917000e-01,
            "29065": 3.083000e-01,
        }

        assert matcard.xsid_dictionary == {
            "29063": "",
            "29065": "31c",
        }

    def test_serpent_mat_input(self):
        string = [
            "mat 1 8.93\n",
            "29063 6.917000e-01\n",
            "29065 3.083000e-01\n",
        ]

        serpent = SerpentInput()
        serpent.file_lines = string
        serpent.process()
