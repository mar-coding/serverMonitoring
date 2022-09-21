import pickle5 as pickle
from ServerMonitor import ServerMonitor

# address to file that save servers details
SERVER_ADDRESS = "data/servers.pickle"


def main():

    servers = pickle.load(open(SERVER_ADDRESS, "rb"))
    print("Please input proper data:")

    server_name = input("Enter server name: ")
    temp_cond = True
    port = 0
    print("Enter a number for port")
    while (temp_cond):
        try:
            port = int(input())
            temp_cond = False
        except:
            print("Wrong!\n Enter a number for port")

    print("Enter a number for type of connections:(1.plain/2.ssl/3.ping)")
    temp_cond_1 = True
    connection = 0
    while (temp_cond_1):
        try:
            connection = int(input())
            if connection == 1 or connection == 2 or connection == 3:
                temp_cond_1 = False
            else:
                print(
                    "Wrong!\nEnter a number for type of connections:(1.plain/2.ssl/3.ping)")
        except:
            print("Wrong!\nEnter a type for type of connections:(1.plain/2.ssl/3.ping)")

    print("Enter a number for priority:(1.low/2.medium/3.high)")
    temp_cond_2 = True
    priority = 0
    while (temp_cond_2):
        try:
            priority = int(input())
            if priority == 1 or priority == 2 or priority == 3:
                temp_cond_1 = False
            else:
                print("Wrong!\nEnter a number for priority:(1.low/2.medium/3.high)")
        except:
            print("Wrong!\nEnter a type for priority:(1.low/2.medium/3.high)")

if __name__ == "__main__":
    main()