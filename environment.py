import random


class Env:
    def __init__(self, args, agents):
        # default: 100 msec
        self.prop_delay_avg = args.prop_delay_avg / 1000.0
        self.prop_delay_std = args.prop_delay_std / 1000.0

        # all peer's address
        self.nodes_table = [agent.uri for agent in agents]

        # redrawn for negative results(absolute value).
        # prop_delay_table[_to][_from]: propagation delay table (_to)->(_from)
        self.prop_delay_table\
            = {_to: {_from: abs(random.gauss(self.prop_delay_avg, self.prop_delay_std))
                     for _from in self.nodes_table}
               for _to in self.nodes_table}
