import requests
import json
import ast


class Agent:
    def __init__(self, args, IP, HTTP_PORT, P2P_PORT):
        self.args = args

        self.ip_address = IP
        self.http_port = str(HTTP_PORT)
        self.p2p_port = str(P2P_PORT)

        self.address = self.get_address()  # public key
        self.blockchain = self.get_blocks()
        self.current_version = self.get_version()
        self.peers = self.get_peers()

    """
    get
    """
    def get_blocks(self):
        uri = self.ip_address + ':' + self.http_port + '/' + 'blocks'

        """
        if you are a light client, gathering only 'header' fields
        """
        res = requests.get(uri)
        return ast.literal_eval(res.text)

    def get_address(self):
        uri = self.ip_address + ':' + self.http_port + '/' + 'address'

        res = requests.get(uri)
        return ast.literal_eval(res.text)['address']

    def get_version(self):
        uri = self.ip_address + ':' + self.http_port + '/' + 'version'

        res = requests.get(uri)
        return res.text

    def get_peers(self):
        uri = self.ip_address + ':' + self.http_port + '/' + 'peers'

        res = requests.get(uri)
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
        uri = self.ip_address + ':' + self.http_port + '/' + 'mineBlock'

        headers = {'Content-type': 'application/json'}
        data = {"data": req}
        res = requests.post(uri, headers=headers, data=json.dumps(data))
        return res.text

    def add_peers(self, req=None):
        uri = self.ip_address + ':' + self.http_port + '/' + 'addPeers'

        headers = {'Content-type': 'application/json'}
        data = {"peers": req}
        res = requests.post(uri, headers=headers, data=json.dumps(data))
        return res.text

    def block_version(self, req=None):
        uri = self.ip_address + ':' + self.http_port + '/' + 'blockVersion'

        headers = {'Content-type': 'application/json'}
        data = {"index": req}
        res = requests.post(uri, headers=headers, data=json.dumps(data))
        return res.text

    # CreateWallet
    # DeleteWallet
    # stop
