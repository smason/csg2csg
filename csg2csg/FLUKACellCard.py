#!/usr/env/python3

import re
import warnings

from csg2csg.CellCard import CellCard


# turn the generic operation type into a serpent relevant text string
def fluka_op_from_generic(Operation):
    # if we are not of type operator - we are string do nowt
    if not isinstance(Operation, CellCard.OperationType):
        if Operation == "(":
            return " + ( "
        if Operation == ")":
            return " ) "
        ival = int(Operation)
        if ival < 0:
            return f" +S{abs(ival)}"
        if ival > 0:
            return f" -S{ival}"
        return Operation

    # otherwise we need to do something
    if Operation == CellCard.OperationType.NOT:
        return " -"
    if Operation == CellCard.OperationType.AND:
        return "  "
    if Operation == CellCard.OperationType.UNION:
        return " | "

    # TODO: shouldn't this raise an exception?!
    warnings.warn(f"Unknown operation {Operation!r}")
    return "unknown operation"


# write the cell card for a fluka cell given a generic cell card
def write_fluka_cell(filestream, CellCard):
    string = f" C{CellCard.cell_id} 5 ( "  # number of adjacent cells

    # build the cell description
    for op in CellCard.cell_interpreted:
        string += fluka_op_from_generic(op)

    string += " ) \n"

    # removes any multiple spaces
    string = re.sub(" {2,}", " ", string)
    string = re.sub(r"\- \+", " -", string)

    filestream.write(string)


class FLUKACellCard(CellCard):
    def __init__(self, card_string):
        CellCard.__init__(self, card_string)
