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
tmp_time = 5
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
    try:
        daemon = Daemon(args)
        daemon.start()
        sleep(tmp_time)  # need for safe running with bash op(s).

        # agent
        agents = [Agent(IP, args.https + i, args.p2ps + i) for i in range(args.nodes)]
        sleep(tmp_time)

        # environment
        env = Env(args, agents)

        """connect"""
        # connect with neighbors
        for agent in agents:
            agent.set_virtual_peers(env)

        # set propagation delay for each pair of connected peers
        env.set_prop_delay_table()







        """tmp"""
        sleep(1)  # temporary

        pprint(env.prop_delay_table)

        for agent in agents:
            print(agent.uri, agent.virtual_peers)


        """tmp"""

    finally:
        daemon.killall()
