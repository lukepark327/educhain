from daemon import Daemon
from agent import Agent
from environment import Env
from arguments import argparser

from time import sleep
import random
import numpy as np
from pprint import pprint


# define
IP = "http://127.0.0.1"
tmp_time = 0.5
SEED = 950327


def run():
    pass


if __name__ == '__main__':
    # random seed
    random.seed(SEED)
    np.random.seed(SEED)

    # argparser
    args = argparser()

    # daemon
    daemon = Daemon(args)
    daemon.start()
    sleep(tmp_time)

    # agent
    agents = [Agent(args, IP, args.https + i, args.p2ps + i) for i in range(args.nodes)]
    sleep(tmp_time)

    # environment
    env = Env(args, agents)
    sleep(tmp_time)

    """tmp"""
    sleep(1)  # temporary
    """tmp"""

    # ToDo: exception handling about error occuring
    daemon.killall()
