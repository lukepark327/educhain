import argparse


def argparser():
    parser = argparse.ArgumentParser()

    """Simulation Settings"""
    parser.add_argument('--nodes', type=int, default=4,
                        help='The number of full nodes constructing blockchain.')

    parser.add_argument('--https', type=int, default=3001,
                        help='The base number of HTTP ports.')

    parser.add_argument('--p2ps', type=int, default=6001,
                        help='The base number of P2P ports.')

    args = parser.parse_args()
    return args
