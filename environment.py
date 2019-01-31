import random
import numpy as np


class Env:
    """
    environment는 agents 정보를 포괄한다.
        -   각 agent 역시 환경의 일부이다.
    """

    def __init__(self, args, agents):
        self.args = args
        self.agents = agents

        # default: 100 msec
        self.prop_delay_avg = self.args.prop_delay_avg / 1000.0
        self.prop_delay_std = self.args.prop_delay_std / 1000.0

        # redrawn for negative results(absolute value).
        # prop_delay_table[_from][_to]: propagation delay table (_from)->(_to)
        self.prop_delay_table = {}

        # reorg ratio
        self.reorg_count = 0

    def assign_virtual_peers(self, agent):
        id = agent.p2p_port - self.args.p2ps
        peers = []

        for pre_agent in self.agents:
            if id + self.args.p2ps in pre_agent.virtual_peers:
                peers.append(pre_agent.p2p_port - self.args.p2ps)

        already_filled = len(peers)

        for _ in range(self.args.neighbors - already_filled):
            while True:
                peer = random.randrange(0, self.args.nodes)
                if (peer not in peers) & (peer != id):
                    peers.append(peer)
                    break

        peers.sort()
        return list(np.array(peers) + self.args.p2ps)

    def set_prop_delay_table(self):
        self.prop_delay_table =\
            {agent.p2p_port:
                {_to: abs(random.gauss(self.prop_delay_avg, self.prop_delay_std))
                    for _to in agent.virtual_peers} for agent in self.agents}

    """
    get
    """
    def propagation_delay(self, _from, _to):
        try:
            return self.prop_delay_table[_from][_to]
        except:
            return -1
