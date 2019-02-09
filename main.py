"""
@version 1.2.0
"""

from simulator import agent, environment, virtual_network
from arguments import argparser

from platform import system
import json
import os
from time import sleep
import random
import numpy as np
from pprint import pprint


def is_windows():
    return True if system() == "Windows" else False


# define
IP = "http://127.0.0.1"
SEED = 950327

# random seed
random.seed(SEED)
np.random.seed(SEED)


if __name__ == '__main__':
    # argparser
    args = argparser()

    try:
        # agent
        agents = [agent.Agent(IP, args.https + i, args.p2ps + i) for i in range(args.nodes)]

        # environment
        env = environment.Env(args)

        """virtual network"""
        vnet = virtual_network.Vnet(args, agents)
        # pprint(vnet.virtual_connections)

        # save propagation delay table
        with open('table.json', 'w') as f:
            json.dump(vnet.virtual_connections, f)

        # ToDo: Visualization of virtual and real network with propagation delay

        """master node"""
        # need some interval before connection.
        sleep(args.sleep)

        master = virtual_network.Master(args, IP, args.master_http, args.master_p2p, agents)

        """create and propagate blocks"""
        # ToDo: Make blocks randomly

        """analysis"""
        # 각 에이전트의 블록 생성 비율, 채택 비율
        # tps (마스터노드를 통과하는 초당 블록의 갯수)
        # 포크 발생 비율
        # ToDo: Offer the dashboard with tensorboardX

    finally:
        # need some interval before kill npm.
        sleep(args.sleep * 1000)

        if is_windows():
            os.system("taskkill /im node.exe /F")
        else:
            os.system("killall npm")
