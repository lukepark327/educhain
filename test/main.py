import os, sys
import json
from requests import get, post
import ast
from pprint import pprint
from time import sleep


def start(total):
    """
    :param total:   number of total node(s).
    :return:        error occurs-False- or not-True-.
    """

    # move src dir.
    os.chdir("../src")

    # npm install
    os.system("npm install")  # sequentially

    # default port num.
    HTTP_base = 3001
    P2P_base = 6001

    # number of total node(s)
    for num in range(total):
        try:
            # npm start
            os.environ['HTTP_PORT'] = str(HTTP_base + num)
            os.environ['P2P_PORT'] = str(P2P_base + num)
            os.system("npm start &")  # background execution
            sleep(1)  # for logging
        except:
            return False

    return True


def killall():
    """
    :return:    error occurs-False- or not-True-.
    """

    try:
        # killall npm
        os.system("killall npm")
    except:
        return False

    return True


if __name__ == '__main__':
    num_node = 3

    # npm start
    start(num_node)

    # interval
    sleep(10)

    #
    killall()
