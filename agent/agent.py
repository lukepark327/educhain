import json
import ast
from requests import get, post


class Agent():
    def __init__(self, URL, HTTP_PORT, P2P_PORT):
        self.URL = URL
        self.HTTP_PORT = str(HTTP_PORT)
        self.P2P_PORT = str(P2P_PORT)

    def getBlockchain(self):
        op = "blocks"
        target = self.URL + ":" + self.HTTP_PORT + '/' + op

        res = get(target)
        return ast.literal_eval(res.text)






def addNewBlock(URL, PORT, req=""):
    op = "mineBlock"
    target = URL + ":" + str(PORT) + '/' + op

    headers = {'Content-type': 'application/json'}
    data = {"data": req}
    res = post(target, data=json.dumps(data), headers=headers)

    return res





def getPeers(URL, PORT):
    op = "peers"
    target = URL + ":" + str(PORT) + '/' + op

    res = get(target)
    return res


def addPeer(URL, PORT, req=None):
    op = "addPeer"
    target = URL + ":" + str(PORT) + '/' + op

    headers = {'Content-type': 'application/json'}
    data = {"peer": req}
    res = post(target, data=json.dumps(data), headers=headers)
    return res


def stopNode(URL, PORT):
    op = "stop"
    target = URL + ":" + str(PORT) + '/' + op

    res = post(target)
    return res
