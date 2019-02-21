import random


def get_delay(mu, std):
    delay_ = random.gauss(mu, std)
    while delay_ <= 0:
        delay_ = random.gauss(mu, std)
    return delay_
