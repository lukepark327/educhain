from daemon import Daemon
from agent import Agent
from arguments import argparser

from time import sleep


# define
IP = "http://127.0.0.1"
tmp_time = 0.5


def run():
    pass


if __name__ == '__main__':
    args = argparser()

    daemon = Daemon(args)
    daemon.start()

    """tmp"""
    sleep(tmp_time)  # temporary

    agents = [Agent(args, IP, args.https + i, args.p2ps + i) for i in range(args.nodes)]
    """tmp"""

    # ToDo: exception handling about error occuring
    daemon.killall()
