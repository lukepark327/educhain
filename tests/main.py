import os
import sys
from platform import system
from time import sleep


def isWindows():
    return True if system() == "Windows" else False


def start(total):
    """
    :param total:   number of total node(s).
    :return:        error occurs-False- or not-True-.
    """

    # move src dir.
    os.chdir("../src")

    # npm install
    os.system("npm install")  # sequentially

    # default port num.
    HTTP_base = 3001
    P2P_base = 6001

    # number of total node(s)
    for num in range(total):
        try:
            # setting env.
            os.environ['HTTP_PORT'] = str(HTTP_base + num)
            os.environ['P2P_PORT'] = str(P2P_base + num)

            # npm start
            # background execution
            if isWindows():
                os.system("START /B npm start")
            else:
                os.system("npm start &")

            # for logging
            sleep(1)

        except:
            return False

    return True


def killall():
    """
    :return: error occurs-False- or not-True-.
    """

    try:
        # killall npm
        if isWindows():
            os.system("taskkill /im node.exe /F")
        else:
            os.system("killall npm")

    except:
        return False

    return True


if __name__ == '__main__':
    """
    """
    num_node = 3

    # npm start
    if not start(num_node):
        print("[FAIL] npm start")
        killall()
        sys.exit(1)


    """
    body
    """
    from scenarios import main as scenarios

    scenarios.tests()
    sleep(10)


    # killall npm
    if not killall():
        print("[FAIL] killall npm")
        sys.exit(1)
