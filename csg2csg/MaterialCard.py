#!/usr/env/python3

from csg2csg.Card import Card
from csg2csg import MaterialData

MCNP_COLOURS = [
    "0 208 31",
    "0 0 255",
    "255 255 0",
    "0 255 0",
    "0 255 255",
    "255 164 0",
    "255 192 202",
    "159 31 239",
    "164 42 42",
    "111 128 144",
    "239 255 255",
    "222 184 134",
    "126 255 0",
    "255 0 255",
    "255 126 80",
    "255 248 220",
    "177 33 33",
    "255 214 0",
    "239 255 239",
    "239 230 139",
    "175 47 95",
    "218 111 213",
    "218 164 31",
    "221 159 221",
    "255 245 237",
    "159 82 44",
    "215 190 215",
    "255 98 70",
    "64 223 208",
    "245 222 179",
    "249 128 113",
    "95 158 159",
    "184 133 10",
    "84 107 46",
    "106 90 205",
    "255 139 0",
    "153 49 204",
    "143 187 143",
    "46 79 79",
    "255 19 146",
    "0 190 255",
    "249 235 214",
    "255 239 245",
    "172 215 230",
    "237 221 130",
    "255 182 193",
    "30 144 255",
    "255 159 121",
    "134 206 249",
    "255 255 223",
    "185 84 210",
    "175 196 222",
    "146 111 219",
    "255 69 0",
    "151 250 151",
    "174 237 237",
    "219 111 146",
    "223 255 255",
    "65 105 224",
    "187 143 143",
    "134 206 235",
    "0 255 126",
    "70 130 180",
    "255 0 0",
    "0 0 0",
    "0 0 255",
    "191 0 0",
    "0 255 0",
    "191 0 255",
    "255 255 0",
    "255 255 255",
]


# get the mcnp colour for the material
# this is mostly for automated testing
def get_material_colour(idx):
    # this obviously returns the same colour more than once
    # but this is what MCNP does so we duplicate this behavior
    return MCNP_COLOURS[idx % 63]


class MaterialCard(Card):

    """A fully defined material card should have a name, a material number,
    a density, a composition dictionary, and optionally a xsid dictionary.
    MCNP being an exception, most MC codes define the density of a material
    belonging to the material definition as opposed to a given cell. This
    approach is taken here for maximal compability amongst codes.
    """


    # constructor
    def __init__(self, material_number=0, card_string=""):
        Card.__init__(self, card_string)
        self.material_number = material_number
        self.material_name = ""
        self.composition_dictionary = {}
        self.xsid_dictionary = {}
        self.density = 0
        self.material_colour = 0
        self.mat_data = MaterialData.MaterialData()

    def __str__(self):
        string = "Material: " + self.material_name + "\n"
        string += "Material num: " + str(self.material_number) + "\n"
        string += "Density: " + str(self.density) + "\n"
        string += "Colour: " + str(self.material_colour) + "\n"
        string += "Composition \n"
        for item in self.composition_dictionary.keys():
            string += item + " " + str(self.composition_dictionary[item]) + "\n"

        return string

    # normalise the material composition such that the sum is 1.0
    def normalise(self):
        sum = 0.0
        # get the sum
        for nuc in self.composition_dictionary:
            sum += float(self.composition_dictionary[nuc])

        # dont divide by -ve number ! mass->atom
        sum = abs(sum)

        for nuc in self.composition_dictionary:
            self.composition_dictionary[nuc] = (
                float(self.composition_dictionary[nuc]) / sum
            )

        # all done
        return

    # explode elements loop through the dictionary and any material that has elements
    # and explode it into its nuclidewise definition
    def explode_elements(self):
        keys_to_remove = []
        new_nuclides = {}
        for nuc in self.composition_dictionary:
            if int(nuc) % 1000 == 0:
                keys_to_remove.append(nuc)
                nuclides = self.mat_data.get_nucs(int(nuc))
                # loop over the nuclides
                for nuclide in nuclides:
                    if (
                        self.composition_dictionary[nuc] < 0
                    ):  # if its mass fraction then
                        new_nuclides[str(nuclide)] = (
                            self.composition_dictionary[nuc]
                            * MaterialData.NATURAL_ABUNDANCE[nuclide * 10000]
                            / 100
                            * self.mat_data.atomic_mass(int(nuc))
                            / self.mat_data.get_aa(nuclide)
                        )
                    else:  # its atom fraction pure multiplication
                        new_nuclides[str(nuclide)] = (
                            self.composition_dictionary[nuc]
                            * MaterialData.NATURAL_ABUNDANCE[nuclide * 10000]
                            / 100
                        )

        # print(self.composition_dictionary)
        for key in keys_to_remove:
            del self.composition_dictionary[key]

        for key in new_nuclides.keys():
            self.composition_dictionary[key] = new_nuclides[key]
            self.xsid_dictionary[key] = ""
