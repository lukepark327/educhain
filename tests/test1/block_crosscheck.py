import hashlib
import random
from time import sleep
import ast
import sys
sys.path.append("..")  # Adds higher directory to python modules path.

from agent import getBlockchain, addNewBlock
from utils import hexToBinary


# Todo: Timeout
def addBlocks(URL, PORT, num=1):
    """
    :return: error occurs-False- or not-True-, list of added blocks
    """
    try:
        for i in range(num):
            res = addNewBlock(URL, PORT)
            sleep(random.randrange(10, 30) / 10)

        res = getBlockchain(URL, PORT)
        newBlocks = ast.literal_eval(res.text)[-num:]  # last 'num' element(s)

    except:
        return False, []

    return True, newBlocks


# Todo: Timeout
def check(URL, PORT, NewBlocks, num=1):
    """
    :return: error occurs-False- or not-True-.
    """
    try:
        blocks = NewBlocks

        res = getBlockchain(URL, PORT)
        fullBlocks = ast.literal_eval(res.text)

        height = len(fullBlocks)

        if height == 1:
            tmp_prevHash = "0000000000000000000000000000000000000000000000000000000000000000"
            tmp_timestamp = 0
        else:
            oldBlock = fullBlocks[-num]
            tmp_prevHash = oldBlock["previousHash"]
            tmp_timestamp = oldBlock["timestamp"]

        for i in range(num):
            index = str(blocks[i]["index"])
            previousHash = blocks[i]["previousHash"]
            timestamp = str(blocks[i]["timestamp"])
            data = str(blocks[i]["data"])
            difficulty = str(blocks[i]["difficulty"])
            nonce = str(blocks[i]["nonce"])
            hash = blocks[i]["hash"]

            # Is index valid?
            assert (index == str(height - num + i))

            # Is previousHash valid?
            assert (previousHash == tmp_prevHash)

            # Is timestamp valid?
            assert (int(timestamp) >= int(tmp_timestamp))

            # Is nonce valid?
            # const hash = calculateHash(index, previousHash, timestamp, data, difficulty, nonce);
            target = hashlib.sha256(
                index.encode() + previousHash.encode() + timestamp.encode() + data.encode() + difficulty.encode() + nonce.encode()
            ).hexdigest()
            assert (hash == target)

            # Is hash valid?
            assert (hexToBinary(hash)[0:int(difficulty)] == "0000000000000000000000000000000000000000000000000000000000000000"[0:int(difficulty)])

            # prepare next loop
            tmp_prevHash = hash
            tmp_timestamp = int(timestamp)

    except:
        return False

    return True
