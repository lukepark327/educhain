"""
@version 1.4.0
"""

# TODO: Add mallcious nodes.
# TODO: Add light clients.

from simulator import agent, environment, virtual_network
from arguments import argparser
from utils import get_delay

import json
import os
from time import sleep
import timeout_decorator
import random
import numpy as np
# from pprint import pprint


# define
IP = "http://127.0.0.1"
SEED = 950327

# random seed
random.seed(SEED)
np.random.seed(SEED)


def prestart(args):
    @timeout_decorator.timeout(args.timeout, use_signals=False)
    def all_agents_avail(agents):
        def check_agents_avail(agents):
            for agent_ in agents:
                try:
                    agent_.get_address()
                except Exception:
                    return False
            return True

        while not check_agents_avail(agents):
            pass

    @timeout_decorator.timeout(args.timeout, use_signals=False)
    def master_avail(master):
        def check_master_avail(master):
            try:
                return master.get_peers()
            except Exception:
                return []

        while not len(check_master_avail(master)) == args.nodes:
            pass

    try:
        agents = [agent.Agent(args, IP, args.https + i, args.p2ps + i)
                  for i in range(args.nodes)]
        env = environment.Env(args)
        vnet = virtual_network.Vnet(args, agents)

        # pprint(vnet.virtual_connections)
        with open('table.json', 'w') as f:
            json.dump(vnet.virtual_connections, f)

        all_agents_avail(agents)
        print("All agents are available.")

        master = virtual_network.Master(
            args, IP, args.master_http, args.master_p2p, agents)

        master_avail(master)
        print("A master node is available.")
        return agents, env, vnet, False

    except Exception as e:
        print(e)
        os.system("killall npm")
        return None, None, None, True


if __name__ == '__main__':
    args = argparser()

    agents, env, vnet, is_error = prestart(args)
    # TODO: Visualization of virtual and real network with propagation delay.
    # How many groups?
    # Use table.json

    try:
        if is_error:
            raise ValueError

        print("Simulation start.")

        for step in range(args.steps):
            who_ = random.randrange(0, len(agents))

            # TODO: How frequently?
            # Use normal distribution
            # TODO: NO ABS, DO RETRY.
            delay_ = get_delay(args.freq_avg, args.freq_std) / 1000.

            print("step: {}, agent: {}, delay: {}".format(step, who_, delay_))

            # TODO: Current implementation couldn't make multiple queries.
            # Use multi-processing.
            agents[who_].mine_block()

            # TODO: A 'reorganization' checking process must be separated with agents' action.
            # Check reorg. per unit time.
            # Use multi-processing.

            sleep(delay_)
            step += 1

        """analysis"""
        # TODO: Offer the dashboard with tensorboardX.
        # 1. Check reorg. ratio.
        # 2. Check Behind nodes ratio.
        # 3. Check TPS. (keep watching the master node.)

    finally:
        print("Simulation terminated.")
        input("Press Enter to exit: ")

        os.system("killall npm")
