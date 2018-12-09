from time import sleep
import sys
sys.path.append("..")  # Adds higher directory to python modules path.

from daemon import start, killall


def scenario():
    """
    1. Check each peer's genesis block
    2. Generate new blocks with data *something: something you will be able to identify* on each peer
        2.1. 2 blocks on peer #1
        2.2. 4 blocks on peer #2
        2.3. 2 blocks on peer #3
    3. Connect peer #1 with #2 (1->2)
    4. Generate new blocks with data *something*
        4.1. 1 blocks on peer #1
        4.2. 2 blocks on peer #3
    5. Connect peer #1 with #3 (1->(2, and 3))
    6. Generate 2 new blocks with data *something* on each peer
    7. Stop peer #1
    8. Generated a new block with data *something* on peer #2, and #3
    9. Stop peer #2, and #3
    """
    # import functions
    from . import genesis_block

    # number of codes
    num_node = 3

    """
    npm start
    """
    if not start(num_node):
        print("[FAIL] npm start")
        killall()
        sys.exit(1)

    """
    Run scenario(s)
    """
    total_cnt = 0
    pass_cnt = 0

    # 1. Check each peer's genesis block
    try:
        if genesis_block.check("http://127.0.0.1", 3001) &\
                genesis_block.check("http://127.0.0.1", 3002) &\
                genesis_block.check("http://127.0.0.1", 3003):
            print("pass", end=' ')
            pass_cnt += 1
        else:
            print("FAIL", end=' ')
    except:
        print("FAIL", end=' ')

    finally:
        print("test1/genesis_block")
        total_cnt += 1

    # 2. Generate new blocks with data *something* on each peer



        # 2.1. 2 blocks on peer #1
        # 2.2. 4 blocks on peer #2
        # 2.3. 2 blocks on peer #3
    # 3. Connect peer #1 with #2 (1->2)
    # 4. Generate new blocks with data *something*
        # 4.1. 1 blocks on peer #1
        # 4.2. 2 blocks on peer #3
    # 5. Connect peer #1 with #3 (1->(2, and 3))
    # 6. Generate 2 new blocks with data *something* on each peer
    # 7. Stop peer #1
    # 8. Generated a new block with data *something* on peer #2, and #3
    # 9. Stop peer #2, and #3



    """
    Killall npm
    """
    if not killall():
        print("[FAIL] killall npm")
        sys.exit(1)

    # return pass_cnt_per_test and total_cnt_per_test
    return pass_cnt, total_cnt
