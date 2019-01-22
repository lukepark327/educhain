from pprint import pprint
import argparse

import sys
sys.path.append("..")  # Adds higher directory to python modules path.

from agent.agent import Agent
from daemon import start, killall


URL_PREFIX = "http://127.0.0.1"
HTTP_PORT_BASE = 3001
P2P_PORT_BASE = 6001


def argparser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--n_agent', type=int, default=10, help='TBA')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = argparser()

    start(2)

    agents = [Agent(URL_PREFIX, (HTTP_PORT_BASE + i), (P2P_PORT_BASE + i)) for i in range(args.n_agent)]

    pprint(agents[0].getBlockchain())

    killall()
