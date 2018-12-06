import os, sys
import json
from requests import get, post
import ast
from pprint import pprint


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


if __name__ == '__main__':
    """
    res = getBlockchain()                       # pprint(ast.literal_eval(res.text)[0]['data'])
    res = addNewBlock(req="Anything") 
    res = getPeers()                            # pprint(ast.literal_eval(res.text)[0])
    res = addPeer(req="ws://127.0.0.1:6003")
    res = stopNode()                            # pprint(ast.literal_eval(res.text)['msg'])
    
    print(res.text)
    """

    """
    URL = "http://127.0.0.1"
    PORT = 3001

    res = getBlockchain(URL, PORT)

    for output in ast.literal_eval(res.text):
        print(json.dumps(output, indent=2))
    """

    COMMAND = "npm start"  # terminal command
    os.system(COMMAND)
    