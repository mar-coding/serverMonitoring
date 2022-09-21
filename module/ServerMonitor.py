import socket
import ssl
from datetime import datetime
import pickle5 as pickle
import logging
import os
import subprocess
import platform
from enum import Enum

from dotenv import load_dotenv

EMAIL = os.getenv('EMAIL')


class ConnectionType(Enum):
    PLAIN = 1
    SSL = 2
    PING = 3
    OTHERS = 4


class PriorityType(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class ServerMonitor():

    def __init__(self, name, port, connection: ConnectionType, priority: PriorityType):
        """
        initial server for being monitored

        Args:
            name (_type_): server name
            port (_type_): server port that we want to connect
            connection (_type_): different kind of connections: ping,ssl,...
            priority (_type_): server priority
            history (_type_): to keep history list
            alert (_type_): to send alert to your email or sms.(it need to set priority)
        """
        self.name = name
        self.port = port
        self.connection = connection
        self.priority = priority
        self.history = []
        self.alert = False
        logging.basicConfig(filename='logs/servers.log', filemode='a',
                            format='%(levelname)s::%(asctime)s - %(message)s', level=logging.INFO)

    def connection_checker(self):
        """
        to check our connection to server
        """
        # msg: used to display a msg to show the connection status
        msg = ""
        # connected: show connection is successful or not
        connected = False
        current_data_time = datetime.now()

        try:
            self.alert = False
            if self.connection == ConnectionType.PLAIN:
                # bind address to socket
                socket.create_connection((self.name, self.port), timeout=10)
                msg = "{} is running. On port {} with {}".format(
                    self.name, self.port, self.connection)
                logging.info(msg)
                connected = True
            elif self.connection == ConnectionType.SSL:
                # bind address to socket then wrap it in ssl
                ssl.wrap_socket(socket.create_connection(
                    (self.name, self.port), timeout=10))
                msg = "{} is running. On port {} with {}".format(
                    self.name, self.port, self.connection)
                logging.info(msg)
                connected = True
            else:
                if self.ping():
                    msg = "{} is running. On port {} with {}".format(
                        self.name, self.port, self.connection)
                    logging.info(msg)
                    connected = True
        except socket.timeout:
            msg = "Server: {} timeout. On port {}".format(self.name, self.port)
            logging.info(msg)
        except (ConnectionRefusedError, ConnectionResetError) as e:
            msg = "Server: {} got this error: {}".format(self.name, e)
            logging.info(msg)
        except Exception as e:
            msg = "Unknown error: {}".format(e)
            logging.warning(msg)

        if connected == False and self.alert == False:
            # send alert
            self.alert = True
            send_alert(self.name, "Date: {} \n Error: {}".format(
                current_data_time, msg), EMAIL)

        # create history for server
        self.history_maker(msg, connected, current_data_time)

    def history_maker(self, msg, connected, date):
        """
        create history for server with maximum limit defined, 
        and if the history limit exceeds, it will delete the older one
        Args:
            msg (_type_): used to display a msg to show the connection status
            connected (_type_): show connection is successful or not
            date (_type_): show current date and time
        """
        max_limit = 100

        while len(self.history) > max_limit:
            self.history.pop(0)

        self.history.append((msg, connected, date))

    def ping(self):
        """
        will ping the server or computer. If the ping is successful,
        it will output True, and if the connection failed, it will return False
        Returns:
            boolean: True for connected and False for Problem in connections
        """
        output = False
        try:
            temp = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system(
            ).lower() == "windows" else 'c', self.name), shell=True, universal_newlines=True)
            if 'unreachable' not in temp:
                output = True
        except Exception:
            logging.exception("Exceptions occurred in ping method.")
            pass
        return output

    
