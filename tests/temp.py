"""
nothing
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
