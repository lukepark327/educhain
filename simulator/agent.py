import requests
import json
import ast
from platform import system
import os


class Agent:
    def __init__(self, IP, HTTP_PORT, P2P_PORT):
        self.ip_address = IP
        self.http_port = HTTP_PORT
        self.p2p_port = P2P_PORT
        self.uri = self.ip_address + ':' + str(self.http_port)
        """
        self.address = self.get_address()  # public key
        self.blockchain = self.get_blocks()
        self.current_version = self.get_version()
        self.peers = self.get_peers()  # only master node
        """
        self.start_daemon()

    """daemon"""
    def start_daemon(self):
        def is_windows():
            return True if system() == "Windows" else False

        try:
            os.chdir("./onechain")  # move src dir.

            # precondition: npm install
            # os.system("npm install --silent")

            # setting env. variables
            os.environ['HTTP_PORT'] = str(self.http_port)
            os.environ['P2P_PORT'] = str(self.p2p_port)

            # npm start
            # background execution
            if is_windows():
                os.system("START /B npm start --silent")
            else:
                os.system("nohup npm start --silent &")

        finally:
            os.chdir("../")

    """RESTful APIs"""
    # GET
    def get_blocks(self):
        """
        if you are a light client, gathering only 'header' fields
        """
        res = requests.get(self.uri + '/blocks')
        return ast.literal_eval(res.text)

    def get_address(self):
        res = requests.get(self.uri + '/address')
        return ast.literal_eval(res.text)['address']

    def get_version(self):
        res = requests.get(self.uri + '/version')
        return res.text

    def get_peers(self):
        res = requests.get(self.uri + '/peers')
        return ast.literal_eval(res.text)

    # POST
    def mine_block(self, req=None):
        headers = {'Content-type': 'application/json'}
        data = {"data": req}
        res = requests.post(self.uri + '/mineBlock', headers=headers, data=json.dumps(data))
        return res.text

    def add_peers(self, req=None):
        headers = {'Content-type': 'application/json'}
        data = {"peers": req}
        res = requests.post(self.uri + '/addPeers', headers=headers, data=json.dumps(data))
        return res.text

    def block_version(self, req=None):
        headers = {'Content-type': 'application/json'}
        data = {"index": req}
        res = requests.post(self.uri + '/blockVersion', headers=headers, data=json.dumps(data))
        return res.text

    # CreateWallet
    # DeleteWallet
    # stop
