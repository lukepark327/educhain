from platform import system
import os
from time import sleep


tmp_time = 0.5


class Daemon:
    def __init__(self, args):
        self.args = args

        self.n_nodes = args.nodes
        self.http_base = args.https
        self.p2p_base = args.p2ps

        self.is_windows = self.get_system_info()  # True if system is Windows, False at the others

    def get_system_info(self):
        return True if system() == "Windows" else False

    def start(self):
        """
        :return: error occurs-False- or not-True-.
        """

        # move src dir.
        os.chdir("./onechain")

        # npm install
        # sequentially
        os.system("npm install --silent")

        # number of total node(s)
        for num in range(self.n_nodes):
            sleep(tmp_time)

            try:
                # setting env.
                os.environ['HTTP_PORT'] = str(self.http_base + num)
                os.environ['P2P_PORT'] = str(self.p2p_base + num)

                # npm start
                # background execution
                if self.is_windows:
                    os.system("START /B npm start --silent")
                else:
                    os.system("nohup npm start --silent &")

            except:
                return False

            finally:
                # os.chdir("../")
                pass

        return True

    def killall(self):
        """
        :return: error occurs-False- or not-True-.
        """

        try:
            # killall npm
            if self.is_windows:
                os.system("taskkill /im node.exe /F")
            else:
                os.system("killall npm")

        except:
            return False

        return True

    def start_master_node(self):
        """
        HTTP_PORT = 3000
        P2P_PORT = 6000

        :return: error occurs-False- or not-True-.
        """
        try:
            """
            # setting env.
            os.environ['HTTP_PORT'] = str(3000)
            os.environ['P2P_PORT'] = str(6000)

            # npm start
            # background execution
            if self.is_windows:
                os.system("START /B npm start --silent")
            else:
                os.system("nohup npm start --silent &")
            """
            pass
        except:
            return False

        # ToDo: return master node's agent

        return True
