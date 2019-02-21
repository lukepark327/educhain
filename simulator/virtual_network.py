from utils import get_delay

import random
import os
import requests
import ast


class Vnet:
    def __init__(self, args, agents):
        self.nodes = args.nodes
        self.p2ps = args.p2ps
        self.neighbors = args.neighbors
        self.prop_delay_avg = args.prop_delay_avg / 1000.0
        self.prop_delay_std = args.prop_delay_std / 1000.0
        self.virtual_connections = self.set_virtual_connections(agents)

    def set_virtual_connections(self, agents):
        peers = self.set_virtual_peers(agents)
        delays = self.set_virtual_prop_delay(agents, peers)
        return {
            key: [
                (elem, delays[key][elem])
                for elem in elems
            ]
            for key, elems in peers.items()
        }

    def set_virtual_peers(self, agents):
        virtual_peers = {}

        for agent in agents:
            peers = []
            for key, val in virtual_peers.items():
                if agent.p2p_port in val:
                    peers.append(key)

            already_filled = len(peers)

            for _ in range(self.neighbors - already_filled):
                while True:
                    peer = random.randrange(0, self.nodes) + self.p2ps
                    if (peer not in peers) & (peer != agent.p2p_port):
                        peers.append(peer)
                        break

            peers.sort()
            virtual_peers[agent.p2p_port] = peers

        return virtual_peers

    def set_virtual_prop_delay(self, agents, virtual_peers):
        # prop_delay_table[_from][_to]: propagation delay table (_from)->(_to)
        return {
            agent.p2p_port: {
                _to: get_delay(self.prop_delay_avg, self.prop_delay_std)
                for _to in virtual_peers[agent.p2p_port]
            }
            for agent in agents
        }


class Master:
    def __init__(self, args, IP, HTTP_PORT, P2P_PORT, agents):
        self.ip_address = IP
        self.http_port = HTTP_PORT
        self.p2p_port = P2P_PORT
        self.uri = self.ip_address + ':' + str(self.http_port)

        self.start_daemon(agents)

    def start_daemon(self, agents):
        # run master node
        # set environment variable PEERS first.

        try:
            os.chdir("./master")

            peers = ""
            for agent in agents:
                uri = agent.ip_address.split(':')[1]
                peers += ("ws:" + uri + ':' + str(agent.p2p_port))  # ws://127.0.0.1:6001
                peers += ", "
            peers = peers[:-2]  # ex) PEERS = "ws://127.0.0.1:6001, ws://127.0.0.1:6002"

            os.environ['PEERS'] = str(peers)
            os.environ['HTTP_PORT'] = str(self.http_port)
            os.environ['P2P_PORT'] = str(self.p2p_port)

            os.system("nohup npm start </dev/null &>/dev/null &")
            # os.system("npm start &")

        finally:
            os.unsetenv('PEERS')
            os.unsetenv('HTTP_PORT')
            os.unsetenv('P2P_PORT')
            os.chdir("../")

    def get_peers(self):
        res = requests.get(self.uri + '/peers')
        return ast.literal_eval(res.text)
