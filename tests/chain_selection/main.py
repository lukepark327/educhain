import sys
sys.path.append("..")  # Adds higher directory to python modules path.

from . import same_length


def tests():
    print("pass" if same_length.scenario()  else "FAIL", end=' ')
    print("tests/chain_selection/same_length")
