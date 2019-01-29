import requests
import json
import ast


class Agent:
    def __init__(self, args, IP, HTTP_PORT, P2P_PORT):
        self.args = args

        self.ip_address = IP
        self.http_port = str(HTTP_PORT)
        self.p2p_port = str(P2P_PORT)
        self.uri = self.ip_address + ':' + self.http_port

        self.address = self.get_address()  # public key
        self.blockchain = self.get_blocks()
        self.current_version = self.get_version()
        self.peers = self.get_peers()

    """
    get
    """
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

    """
    need update
    """
    def update_blocks(self):
        self.blockchain = self.get_blocks()

    def update_address(self):
        self.address = self.get_address()

    def update_version(self):
        self.current_version = self.get_version()

    def update_peers(self):
        self.peers = self.get_peers()

    """
    post
    """
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
