import os, sys
import json
from requests import get, post
import ast
from pprint import pprint
from time import sleep

from . import agent



if __name__ == '__main__':
    """
    HTTP_base = 3001
    P2P_base = 6001

    total = 3

    for num in range(3):
        # node num
        os.environ['HTTP_PORT'] = str(HTTP_base + num)
        os.environ['P2P_PORT'] = str(P2P_base + num)
        os.system("npm start &")
        sleep(1)

    # interval
    sleep(10)

    # killall npm
    os.system("killall npm")
    """

    """
    os.chdir("..")
    os.system("ls")

    os.chdir("instructional-blockchain")
    os.system("ls")
    """

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

    """
    os.environ['HTTP_PORT'] =   sys.argv[1] if len(sys.argv) > 1 else '3001'
    os.environ['P2P_PORT']  =   sys.argv[2] if len(sys.argv) > 2 else '6001'
    os.system("npm start &")
    """

    """
    # node 1
    os.environ['HTTP_PORT'] = '3001'
    os.environ['P2P_PORT']  = '6001'
    os.system("npm start &")
    sleep(1)
    """
