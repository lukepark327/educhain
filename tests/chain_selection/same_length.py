import json
import ast

import sys
sys.path.append("..")  # Adds higher directory to python modules path.

from agent import getBlockchain


# Todo: Timeout
def scenario():
    """
    :return: error occurs-False- or not-True-.
    """

    URL = "http://127.0.0.1"
    PORT = 3001

    res = getBlockchain(URL, PORT)

    for output in ast.literal_eval(res.text):
        print(json.dumps(output, indent=2))

    return True
