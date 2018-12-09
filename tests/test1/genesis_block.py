import json
import ast
import sys
sys.path.append("..")  # Adds higher directory to python modules path.

from agent import getBlockchain


# Todo: Timeout
def check(URL, PORT):
    """
    :return: error occurs-False- or not-True-.
    """
    try:
        res = getBlockchain(URL, PORT)
        genesisBlock = ast.literal_eval(res.text)[0]

        assert genesisBlock["index"] == 0
        assert genesisBlock["previousHash"] == "0000000000000000000000000000000000000000000000000000000000000000"
        assert genesisBlock["timestamp"] == 1535165503
        assert genesisBlock["data"] == "Genesis block"
        assert genesisBlock["hash"] == "997d082838d06e301961597bb2daabb0a16aae046629d65127ddd4fa0539a1c7"
        assert genesisBlock["difficulty"] == 0
        assert genesisBlock["nonce"] == 0

    except:
        return False

    return True
