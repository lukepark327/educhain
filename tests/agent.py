import json
from requests import get, post


def getBlockchain(URL, PORT):
    op = "blocks"
    target = URL + ":" + str(PORT) + '/' + op

    res = get(target)
    return res


def addNewBlock(URL, PORT, req=None):
    op = "mineBlock"
    target = URL + ":" + str(PORT) + '/' + op

    if req == None:
        res = post(target)
    else:
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
