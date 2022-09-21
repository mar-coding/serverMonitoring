import json
import logging

from os import path

from module.ServerMonitor import ServerMonitor

# address to file that save servers details
SERVER_ADDRESS = "data/servers.json"

logging.basicConfig(filename='logs/servers.log', filemode='a',
                    format='%(levelname)s::%(asctime)s - %(message)s', level=logging.INFO)


def main():
    # try:
    #     servers = pickle.load(open(SERVER_ADDRESS, "rb"))
    # except (OSError, IOError) as e:
    #     pickle.dump("", open(SERVER_ADDRESS, "wb"))

    print("Please input proper data")

    name = input("Enter server name: ")
    temp_cond = True
    port = 0
    print("Enter a number for port: ", end="")
    while (temp_cond):
        try:
            port = int(input())
            temp_cond = False
        except:
            print("Wrong!\nEnter a number for port ", end="")

    print("Enter a number for type of connections(1.plain/2.ssl/3.ping):")
    temp_cond_1 = True
    connection = 0
    while (temp_cond_1):
        try:
            connection = int(input())
            if connection == 1 or connection == 2 or connection == 3:
                temp_cond_1 = False
            else:
                print(
                    "Wrong!\nEnter a number for type of connections(1.plain/2.ssl/3.ping):")
        except:
            print("Wrong!\nEnter a type for type of connections(1.plain/2.ssl/3.ping):")

    print("Enter a number for priority(1.low/2.medium/3.high):")
    temp_cond_2 = True
    priority = 0
    while (temp_cond_2):
        try:
            priority = int(input())
            if priority == 1 or priority == 2 or priority == 3:
                temp_cond_2 = False
            else:
                print("Wrong!\nEnter a number for priority(1.low/2.medium/3.high):")
        except:
            print("Wrong!\nEnter a type for priority(1.low/2.medium/3.high):")

    new_server = ServerMonitor(name, port, connection, priority)
    data = json.dumps(new_server.__dict__, indent=4)
    print(data)
    # with open(SERVER_ADDRESS, 'a') as f:
    #     json.dump(data, f)
    # pickle.dump(servers, open(SERVER_ADDRESS, "wb"))
    if path.exists(SERVER_ADDRESS):
        with open(SERVER_ADDRESS, 'r') as file:
            previous_json = json.load(file)
            data = previous_json + "," + data

    with open(SERVER_ADDRESS, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    try:
        main()
        msg = "Successfully Adding Server!"
        print(msg)
        logging.info(msg)
    except Exception:
        logging.exception("Exceptions occurred in file addServer.py.")
