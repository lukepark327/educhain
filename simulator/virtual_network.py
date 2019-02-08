import random


# ToDo: master node


class Vnet:
    def __init__(self, args, agents):
        self.args = args

        # default: 100 msec
        self.prop_delay_avg = self.args.prop_delay_avg / 1000.0
        self.prop_delay_std = self.args.prop_delay_std / 1000.0

        # key -> (peer, delay)
        """
        {
            "6001": [
                ("6002", 0.989),
                ("6003", 0.102),
                ...,
                ("6010", 0.100)
            ],
            "6002": [
                ("6001", 0.102),
                ...
            ],
            ...
        }
        """
        self.virtual_connections = self.set_virtual_connections(agents)

    def set_virtual_connections(self, agents):
        peers = self.set_virtual_peers(agents)
        delays = self.set_virtual_prop_delay(agents, peers)

        virtual_connections = {key: [(elem, delays[key][elem]) for elem in elems]
                               for key, elems in peers.items()}

        return virtual_connections

    def set_virtual_peers(self, agents):
        virtual_peers = {}

        for agent in agents:
            peers = []
            for key, val in virtual_peers.items():
                if agent.p2p_port in val:
                    peers.append(key)

            already_filled = len(peers)

            for _ in range(self.args.neighbors - already_filled):
                while True:
                    peer = random.randrange(0, self.args.nodes) + self.args.p2ps
                    if (peer not in peers) & (peer != agent.p2p_port):
                        peers.append(peer)
                        break

            peers.sort()
            virtual_peers[agent.p2p_port] = peers

        return virtual_peers

    def set_virtual_prop_delay(self, agents, virtual_peers):
        # redrawn for negative results(absolute value).
        # prop_delay_table[_from][_to]: propagation delay table (_from)->(_to)
        return {
            agent.p2p_port: {
                _to: abs(random.gauss(self.prop_delay_avg, self.prop_delay_std))
                for _to in virtual_peers[agent.p2p_port]
            }
            for agent in agents
        }
