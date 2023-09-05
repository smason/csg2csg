#!/usr/env/python3

from csg2csg.MaterialCard import MaterialCard
from csg2csg.MCNPFormatter import get_fortran_formatted_number


# write a specific serpent material card
def write_serpent_material(filestream, material):
    parts = []

    # human readable comment
    parts.append(f"% {material.material_name}\n")

    # material header line
    parts.append(f"mat {material.material_number}")
    parts.append(f" {material.density}")
    # if its a non tally material set the relevant colour
    if material.material_colour:
        parts.append(f" rgb {material.material_colour}")
    parts.append("\n")

    # material composition
    for nucid, frac in material.composition_dictionary.items():
        xsid = material.xsid_dictionary[nucid]
        if xsid:
            parts.append(f"{nucid}.{xsid} {frac:e}\n")
        else:
            parts.append(f"{nucid} {frac:e}\n")

    filestream.write("".join(parts))


""" Class to handle SerpentMaterialCard tranlation
"""


class SerpentMaterialCard(MaterialCard):
    def __init__(self, material_number, material_name, material_density, card_string):
        MaterialCard.__init__(self, material_number, card_string)
        self.material_name = material_name
        self.material_number = material_number
        self.density = material_density
        self.__process_string()

    # populate the Serpent Material Card
    def __process_string(self):
        # need to reset the dictionary
        # otherwise state seems to linger - weird
        self.composition_dictionary = {}

        mat_string = self.text_string
        mat_string = mat_string.replace("\n", " ")

        # split string
        tokens = mat_string.split()

        if len(tokens) % 2 != 0:
            raise Exception("Material string not correctly processed")

        while len(tokens) != 0:
            nuclide = tokens[0].split(".")
            nucid = nuclide[0]
            try:
                xsid = nuclide[1]
            except IndexError:
                xsid = ""
            frac = get_fortran_formatted_number(tokens[1])
            tokens.pop(0)
            tokens.pop(0)
            self.composition_dictionary[nucid] = frac
            self.xsid_dictionary[nucid] = xsid
        return
