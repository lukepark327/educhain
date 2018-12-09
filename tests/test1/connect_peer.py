import sys
sys.path.append("..")  # Adds higher directory to python modules path.

from agent import addPeer


# Todo: Timeout
def connectPeer(URL, PORT, who):
    """
    :return: error occurs-False- or not-True-.
    """
    try:
        addPeer(URL, PORT, req=who)

    except:
        return False

    return True
