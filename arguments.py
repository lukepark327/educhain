import argparse


def argparser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--steps', type=int, default=100,
                        help='The number of simulation steps.')

    parser.add_argument('--nodes', type=int, default=120,
                        help='The number of full nodes constructing blockchain.')

    parser.add_argument('--neighbors', type=int, default=8,
                        help='Each node initiates links to the amount of \'neighbors\' selected neighbors.')

    parser.add_argument('--timeout', type=int, default=30,
                        help='Maximum waiting time. (seconds)')

    parser.add_argument('--prop_delay_avg', type=float, default=100.,
                        help='The average value of propagation delay. (milliseconds)')

    parser.add_argument('--prop_delay_std', type=float, default=100.,
                        help='The standard deviation of propagation delay. (milliseconds)')

    parser.add_argument('--freq_avg', type=float, default=1000.,
                        help='The average value of frequency. (milliseconds)')

    parser.add_argument('--freq_std', type=float, default=200.,
                        help='The standard deviation of frequency. (milliseconds)')

    parser.add_argument('--master_http', type=int, default=3000,
                        help='The HTTP port of a master node.')

    parser.add_argument('--master_p2p', type=int, default=6000,
                        help='The P2P port of a master node.')

    parser.add_argument('--https', type=int, default=3001,
                        help='The base number of HTTP ports.')

    parser.add_argument('--p2ps', type=int, default=6001,
                        help='The base number of P2P ports.')

    args = parser.parse_args()
    return args
