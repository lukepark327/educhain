import argparse


def argparser():
    parser = argparse.ArgumentParser()

    """Simulation Settings"""
    parser.add_argument('--nodes', type=int, default=120,
                        help='The number of full nodes constructing blockchain.')

    parser.add_argument('--https', type=int, default=3001,
                        help='The base number of HTTP ports.')

    parser.add_argument('--p2ps', type=int, default=6001,
                        help='The base number of P2P ports.')

    parser.add_argument('--prop_delay_avg', type=float, default=100,
                        help='The average value of propagation delay. (milliseconds)')

    parser.add_argument('--prop_delay_std', type=float, default=100,
                        help='The standard deviation of propagation delay. (milliseconds)')

    parser.add_argument('--neighbors', type=int, default=8,
                        help='Each node initiates links to the amount of \'neighbors\' selected neighbors.')

    args = parser.parse_args()
    return args
