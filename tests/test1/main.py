import sys
sys.path.append("..")  # Adds higher directory to python modules path.

from utils import npm_decorator


# num_node = 3
@ npm_decorator(3)
def scenario():
    """
    1. Check each peer's genesis block
    2. Generate new blocks on each peer
        2.1. 2 blocks on peer #1
        2.2. 4 blocks on peer #2
        2.3. 2 blocks on peer #3
    3. Connect peers
        3.1. peer #1 with #2 (1->2)
        3.2. peer #1 with #3 (1->(2 and 3))
    4. Generate new blocks
        4.1. 3 blocks on peer #1
        4.2. 5 blocks on peer #3
    5. Stop all peers
    """
    LOCAL_HOST = "http://127.0.0.1"

    # import functions
    from . import genesis_block
    from . import create_block
    from . import connect_peer
    from . import stop_server
    from . import block_crosscheck

    total_cnt = 0
    pass_cnt = 0

    # 1. Check each peer's genesis block
    try:
        assert genesis_block.check(LOCAL_HOST, 3001)
        assert genesis_block.check(LOCAL_HOST, 3002)
        assert genesis_block.check(LOCAL_HOST, 3003)

        print("pass", end=' ')
        pass_cnt += 1

    except:
        print("FAIL", end=' ')

    finally:
        print("test1/genesis_block")
        total_cnt += 1

    # 2. Generate new blocks
        # 2.1. 2 blocks on peer #1
        # 2.2. 4 blocks on peer #2
        # 2.3. 2 blocks on peer #3
    try:
        assert create_block.addBlocks(LOCAL_HOST, 3001, num=2)
        assert create_block.check(LOCAL_HOST, 3001, num=2)

        assert create_block.addBlocks(LOCAL_HOST, 3002, num=4)
        assert create_block.check(LOCAL_HOST, 3002, num=4)

        assert create_block.addBlocks(LOCAL_HOST, 3003, num=2)
        assert create_block.check(LOCAL_HOST, 3003, num=2)

        print("pass", end=' ')
        pass_cnt += 1

    except:
        print("FAIL", end=' ')

    finally:
        print("test1/create_block")
        total_cnt += 1

    # 3. Connect peers
        # 3.1. peer #1 with #2 (1->2)
        # 3.2. peer #1 with #3 (1->(2 and 3))
    try:
        assert connect_peer.connectPeer(LOCAL_HOST, 3001, "ws://127.0.0.1:6002")
        assert connect_peer.connectPeer(LOCAL_HOST, 3001, "ws://127.0.0.1:6003")

        print("pass", end=' ')
        pass_cnt += 1

    except:
        print("FAIL", end=' ')

    finally:
        print("test1/connect_peer")
        total_cnt += 1

    # 4. Generate new blocks
        # 4.1. 3 blocks on peer #1
        # 4.2. 5 blocks on peer #3
    try:
        isPass, newBlocks = block_crosscheck.addBlocks(LOCAL_HOST, 3001, num=3)
        assert isPass
        assert block_crosscheck.check(LOCAL_HOST, 3002, newBlocks, num=3)
        assert block_crosscheck.check(LOCAL_HOST, 3003, newBlocks, num=3)

        isPass, newBlocks = block_crosscheck.addBlocks(LOCAL_HOST, 3003, num=5)
        assert isPass
        assert block_crosscheck.check(LOCAL_HOST, 3001, newBlocks, num=5)
        assert block_crosscheck.check(LOCAL_HOST, 3002, newBlocks, num=5)

        print("pass", end=' ')
        pass_cnt += 1

    except:
        print("FAIL", end=' ')

    finally:
        print("test1/block_crosscheck")
        total_cnt += 1

    # 5. Stop all peers
    try:
        assert stop_server.stopServer(LOCAL_HOST, 3001)
        assert stop_server.stopServer(LOCAL_HOST, 3002)
        assert stop_server.stopServer(LOCAL_HOST, 3003)

        print("pass", end=' ')
        pass_cnt += 1

    except:
        print("FAIL", end=' ')

    finally:
        print("test1/stop_server")
        total_cnt += 1

    # return pass_cnt_per_test and total_cnt_per_test
    return pass_cnt, total_cnt
