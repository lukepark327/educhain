import random
import os
from platform import system


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


# ToDo: master node
class Master:
    def __init__(self, args, IP, HTTP_PORT, P2P_PORT, agents):
        self.args = args

        self.ip_address = IP
        self.http_port = HTTP_PORT
        self.p2p_port = P2P_PORT
        self.uri = self.ip_address + ':' + str(self.http_port)

        self.start_daemon(agents)

    def start_daemon(self, agents):
        # run master node
        # set environment variable PEERS first.

        def is_windows():
            return True if system() == "Windows" else False

        try:
            os.chdir("./master")

            peers = ""
            for agent in agents:
                uri = agent.ip_address.split(':')[1]
                peers += ("ws:" + uri + ':' + str(agent.p2p_port))
                peers += ", "
            peers = peers[:-2]

            # ex) PEERS = "ws://127.0.0.1:6001, ws://127.0.0.1:6002"
            os.environ['PEERS'] = str(peers)

            os.environ['HTTP_PORT'] = str(self.http_port)
            os.environ['P2P_PORT'] = str(self.p2p_port)

            if is_windows():
                os.system("START /B npm start")
            else:
                os.system("npm start &")

        finally:
            # export PEERS="..."
            # env | grep PEERS
            # unset PEERS
            os.unsetenv('PEERS')
            os.unsetenv('HTTP_PORT')
            os.unsetenv('P2P_PORT')

            os.chdir("../")
