import sys
sys.path.append("..")  # Adds higher directory to python modules path.

from agent import stopNode


# Todo: Timeout
def stopServer(URL, PORT):
    """
    :return: error occurs-False- or not-True-.
    """
    try:
        stopNode(URL, PORT)

    except:
        return False

    return True
