import sys
from . import genesis_block

"""
1.  genesis block check
2.  generate new block: 10s for peer #1, 16s for peer #2, 24s for peer #3: with data *something*
3.  connect peer #1 with #2, and connect peer #1 with #3
4.  generate new block:  4s for peer #1,  3s for peer #2,  1s for peer #3: with data *something*
5.  stop peers
"""
def tests():



    print("pass" if genesis_block.scenario()  else "FAIL", end=' ')
    print("tests/chain_selection/same_length")
