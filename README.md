[![license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![version](https://img.shields.io/badge/version-1.0.0-red.svg)](https://github.com/twodude/instructional-blockchain)
[![node](https://img.shields.io/badge/node-%3E%3D4.3.2-brightgreen.svg)](https://nodejs.org/en/)
[![python](https://img.shields.io/badge/python-3.7.1-blue.svg)](https://www.python.org)   

# instructional-blockchain

![symbol](https://github.com/twodude/instructional-blockchain/blob/master/images/symbol.png)

```instructional-blockchain``` is an automated testing software.
> The main project of
**Sogang Univ. Blockchain Lab.**   
> Based on [one-chain](https://github.com/twodude/onechain)   

## Abstract
```instructional-blockchain``` is a simple blockchain implementation for educational purpose. It supports generating blocks, varifying blocks, mining blocks, consensus about conflicting chains, connecting peers, and various wallet functions, et al. Like
*[Pintos](https://web.stanford.edu/class/cs140/projects/pintos/pintos.html)*, simple operating system framework for the 80x86 architecture, instructional-blockchain project is intended to introduce undergraduates to concepts in blockchain core design and implementation.

It was created at Sogang University's Blockchain Lab. by
**[Luke Park (Sanghyeon Park)](https://github.com/twodude)**
in 2018.

## Overview

![diagram](https://github.com/twodude/instructional-blockchain/blob/master/images/overview.png)

*Fill in the blanks, simulate your own code, check the score, and modify it.*

The simulator written in python automatically tests your code(s) and provides you some feedback
**-pass/FAIL-**
in all possible situations.

* [Goto the problem branch](https://github.com/twodude/instructional-blockchain/tree/problem)
* [Goto the solution branch](https://github.com/twodude/instructional-blockchain/tree/solution)

## Details

For example, a ```./tests/test1/main.py``` file describes following situation:

1. Check each peer's genesis block   
2. Generate new blocks on each peer   
    1. 2 blocks on peer #1   
    2. 4 blocks on peer #2   
    3. 2 blocks on peer #3   
3. Connect peers   
    1. peer #1 with #2 (1->2)   
    2. peer #1 with #3 (1->(2 and 3))   
4. Generate new blocks   
    1. 3 blocks on peer #1   
    2. 5 blocks on peer #3   
5. Stop all peers   

The above simulator tests each situation step by step.

# How to Use
[![video](http://img.youtube.com/vi/6L_c4Ug-KwE/0.jpg)](https://www.youtube.com/watch?v=6L_c4Ug-KwE)   
> Click on the image above to play the video.

## Environments
Blockchain core and its accompanying parts are written in Node.js. Testing or simulating parts are written in Python.
- Node.js v8.11.3 (>=4.3.2)
- Python 3.7.1 

## Run node independently
* move ```./src```
```
cd ./src
```

* install required modules
```
npm install
```
See [```./src/package.json```](https://github.com/twodude/instructional-blockchain/blob/master/src/package.json)'s 'dependencies' field if you wonder.

* start node
```
npm start
```
Visit the [one-chain](https://github.com/twodude/onechain) repository to read more details.

## Testing and Scoring
* move ```./tests```
```
cd tests
```

* run test program
```
python main.py
```

## Trouble Shootings
* if
*```ImportError: No module named requests```*
occurs:
```
pip install requests
```

* if 
*```Error: listen EADDRINUSE :::3001```*
occurs:
```
killall npm
```
*or*
```
taskkill /im node.exe /F
```

# References
> https://github.com/twodude/onechain   
> https://web.stanford.edu/class/cs140/projects/pintos/pintos.html#SEC_Top   

# License
> The instructional-blockchain project is licensed under the [Apache License, Version 2.0](https://opensource.org/licenses/Apache-2.0), also included in our repository in the [LICENSE](https://github.com/twodude/instructional-blockchain/blob/master/LICENSE) file.
