import json
import logging


SERVER_ADDRESS = "data/servers.json"

logging.basicConfig(filename='logs/servers.log', filemode='a',
                    format='%(levelname)s::%(asctime)s - %(message)s', level=logging.INFO)


def main():
    f = open(SERVER_ADDRESS)
    data = json.loads(json.load(f))
    print(data)

    # for i in data:
    #     print(i)


if __name__ == "__main__":
    try:
        main()
        msg = "Successfully Loading Servers!"
        print(msg)
        logging.info(msg)
    except Exception:
        logging.exception("Exceptions occurred in file loadServer.py.")
