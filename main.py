from module.ServerMonitor import ServerMonitor, ConnectionType, PriorityType
import pickle5 as pickle


def load_server(file_name: str):
    """
    load server list from address that we give to it
    Args:
        file_name (str): address of file (*.pickle)

    Returns:
        list: list of servers
    """
    try:
        servers = pickle.load(open(file_name, "rb"))
    except:
        servers = [
            ServerMonitor("reddit.com", 80,
                          ConnectionType.PLAIN, PriorityType.HIGH),
            ServerMonitor("msn.com", 80, ConnectionType.PLAIN,
                          PriorityType.HIGH),
            ServerMonitor("smtp.google.com", 465,
                          ConnectionType.SSL, PriorityType.HIGH),
            ServerMonitor("192.1681.164", 80,
                          ConnectionType.PING, PriorityType.HIGH),
            ServerMonitor("yahoo.com", 80,
                          ConnectionType.PLAIN, PriorityType.HIGH),
            ServerMonitor("google.com", 80,
                          ConnectionType.PLAIN, PriorityType.HIGH),
        ]
    pickle.dump(servers, open(file_name, "wb"))
    return servers


def main():
    servers = load_server(file_name="data/servers.pickle")
    for server in servers:
        server.connection_checker()
        print(len(server.history))
        print(server.history[-1])


if __name__ == "__main__":
    main()
