from csg2csg.MCNPMaterialCard import MCNPMaterialCard


def test_mcnp_material():
    string = (
        "29063 6.917000e-01 \n"
        "29065.31c 3.083000e-01 \n"
    )
    number = 1
    matcard = MCNPMaterialCard(number, string)

    assert matcard.material_number == number
    assert matcard.material_name == f"M{number}"

    assert matcard.composition_dictionary == {
        "29063": 6.917000e-01,
        "29065": 3.083000e-01,
    }

    assert matcard.xsid_dictionary == {
        "29063": "",
        "29065": "31c",
    }


def test_mcnp_material_with_duplicates():
    string = (
        "29063 2 \n"
        "29063 1 \n"
        "29065.31c 3.083000e-01 \n"
    )
    number = 1
    matcard = MCNPMaterialCard(number, string)

    assert matcard.material_number == number
    assert matcard.material_name == f"M{number}"

    assert matcard.composition_dictionary == {
        "29063": 3,
        "29065": 3.083000e-01,
    }

    assert matcard.xsid_dictionary == {
        "29063": "",
        "29065": "31c",
    }


def test_mcnp_material_with_keywords():
    string = (
        "29063 6.917000e-01 \n"
        "29065.31c 3.083000e-01 \n"
        "hlib=.70h  pnlib=70u"
    )
    number = 1
    matcard = MCNPMaterialCard(number, string)

    assert matcard.material_number == number
    assert matcard.material_name == f"M{number}"

    assert matcard.composition_dictionary == {
        "29063": 6.917000e-01,
        "29065": 3.083000e-01,
    }

    assert matcard.xsid_dictionary == {
        "29063": "",
        "29065": "31c",
    }


def test_mcnp_material_with_keyword():
    string = (
        "29063 6.917000e-01 \n"
        "29065.31c 3.083000e-01 \n"
        "hlib=.70h"
    )
    number = 1
    matcard = MCNPMaterialCard(number, string)

    assert matcard.material_number == number
    assert matcard.material_name == f"M{number}"

    assert matcard.composition_dictionary == {
        "29063": 6.917000e-01,
        "29065": 3.083000e-01,
    }

    assert matcard.xsid_dictionary == {
        "29063": "",
        "29065": "31c",
    }
