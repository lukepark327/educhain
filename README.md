[![license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![version](https://img.shields.io/badge/version-v2.0.0-orange.svg)](https://github.com/twodude/educhain)
[![node](https://img.shields.io/badge/node-%3E%3D4.3.2-yellow.svg)](https://nodejs.org/en/)
[![python](https://img.shields.io/badge/python-3.7.1-blue.svg)](https://www.python.org)   


# edu-chain :: Instructional Blockchain

![educhain_logo](https://github.com/twodude/educhain/blob/master/images/logo.png)

```educhain``` is an instructional purpose blockchain.   
```#blockchain``` ```#simulator``` ```#testing-tools``` ```#test-automation```

> The 6th D2 CAMPUS FEST Finalists   
> The main project of
**Sogang Univ. Blockchain Lab.**   
> Based on [one-chain](https://github.com/twodude/onechain)   
> Based on [blockchain-simulator](https://github.com/twodude/blockchain-simulator)   


## Overview

*Fill in the blanks, simulate your own code, check the score, and improve it.*   
*Make your own blockchain core.*   

It was created at Sogang University's Blockchain Lab. by
**[Luke Park (Sanghyeon Park)](https://github.com/twodude)**.

![approach](https://github.com/twodude/educhain/blob/master/images/approach.png)

```educhain``` is a simple blockchain implementation for instructional and educational purpose.
Like *[Pintos](https://web.stanford.edu/class/cs140/projects/pintos/pintos.html)*, simple operating system framework for the 80x86 architecture, educhain project is intended to introduce undergraduates to concepts in blockchain core design and implementation.

The simulator written in python automatically tests your code(s) and provides you some important information.   
There are some examples of important information...
* Reorganization ratio.   
* Effective throughput and nodes behind ratio.   
* TPS(Transactions Per Seconds).   

![educhain2](https://github.com/twodude/educhain/blob/master/images/educhain2.png)

```educhain``` *version 2.0.0* targets a more general blockchain implementation. Now students can implement the blockchain core in various ways. For example, you can implement a consensus algorithm in PoW(Proof-of-Work), PoS(Proof-of-Stake), and PoA(Proof-of-authority); whatever you want. Not only consensus parts, but also block or blockchain structure, validation processes, communication parts, and identification.

Get ```educhain``` *version 1.0.0* at [v1.0.0 branch](https://github.com/twodude/educhain/tree/v1.0.0).


## Problem Solving
- Goto the [problem branch](https://github.com/twodude/educhain/tree/problem)
  - **Q1**: [Consensus Algorithm](https://github.com/twodude/educhain/blob/problem/onechain/src/blockchain.js#L92)
- Goto the [solution branch](https://github.com/twodude/educhain/tree/solution)


# How to Use
[![video](http://img.youtube.com/vi/oR6GdZUqGmM/0.jpg)](https://www.youtube.com/watch?v=oR6GdZUqGmM)   
> Click on the image above to play the video.


## Environments
Blockchain core and its accompanying parts are written in Node.js. Testing or simulating parts are written in Python.
- Node.js v8.11.3 (>=4.3.2)
- Python 3.6.7 


## Start a Simulation

### Preconditions
```bash
$ sh preconditions.sh
```

### Run
```bash
$ sh run.sh
```
*or*
```bash
$ python3 main.py --nodes=24 --neighbors=3
```
There are several arguments that control simulation settings.
```bash
$ python3 main.py --help
  --steps STEPS         The number of simulation steps.
  --nodes NODES         The number of full nodes constructing blockchain.
  --neighbors NEIGHBORS
                        Each node initiates links to the amount of 'neighbors'
                        selected neighbors.
  --timeout TIMEOUT     Maximum waiting time. (seconds)
  --prop_delay_avg PROP_DELAY_AVG
                        The average value of propagation delay. (milliseconds)
  --prop_delay_std PROP_DELAY_STD
                        The standard deviation of propagation delay.
                        (milliseconds)
  --freq_avg FREQ_AVG   The average value of frequency. (milliseconds)
  --freq_std FREQ_STD   The standard deviation of frequency. (milliseconds)
  --master_http MASTER_HTTP
                        The HTTP port of a master node.
  --master_p2p MASTER_P2P
                        The P2P port of a master node.
  --https HTTPS         The base number of HTTP ports.
  --p2ps P2PS           The base number of P2P ports.
```

## Cleanup
```bash
$ sh cleanup.sh
```


## APIs

### Get blockchain
```bash
curl http://127.0.0.1:3001/blocks
```
You can pretty-print JSON with:
```bash
curl http://127.0.0.1:3001/blocks | python -m json.tool
```
Python >= 2.6 required.

### Get connected peers
```bash
curl http://127.0.0.1:3001/peers
```

### Get Address
```bash
curl http://127.0.0.1:3001/address
```


## Trouble Shootings
* if
*```ImportError: No module named requests```*
occurs:
```bash
$ pip install requests
```

* if 
*```Error: listen EADDRINUSE :::3001```*
occurs:
```bash
$ killall npm
```

* if
*```'Time out'```*
occurs:
```bash
$ sh preconditions.sh
```


# References
- https://github.com/twodude/onechain   
- https://github.com/twodude/blockchain-simulator   
- https://web.stanford.edu/class/cs140/projects/pintos/pintos.html#SEC_Top   


# License
The educhain project is licensed under the [Apache License, Version 2.0](https://opensource.org/licenses/Apache-2.0), also included in our repository in the [LICENSE](https://github.com/twodude/educhain/blob/master/LICENSE) file.
