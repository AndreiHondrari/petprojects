#!python

"""
    Netcat - custom implementation in Python
    ----------------------------------------
    Author: Andrei-George Hondrari
    E-mail: andrei.hondrari@gmail.com
    Website: andreihondrari.com
    Date: 13 / 12 / 2018

"""

import sys
import argparse
import socket
import signal
import types

DEFAULT_PORT = 12345
DEFAULT_HOST_NAME = ''
NO_OF_UNACCEPTED_CONNECTIONS = 5

if __name__ == "__main__":

    parser = argparse.ArgumentParser("Netcat")
    parser.add_argument("-s", dest="host", action="store")
    parser.add_argument("-p", dest="port", action="store")
    parser.add_argument("-l", dest="listen", action="store_true")
    parser.add_argument("--listen", dest="listen", action="store_true")
    args_space = parser.parse_args()

    port = DEFAULT_PORT

    if args_space.port is None:
        print("You have not specified a port. Assuming: {}".format(port))
    else:
        port = args_space.port

    # create server
    if args_space.listen:
        running: bool = True
        server_socket = socket.socket()
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host_addr = socket.gethostbyname(DEFAULT_HOST_NAME)
        server_socket.bind((host_addr, port))

        def sigint_handler(
            sig: signal.Signals,
            frame: types.FrameType,
        ) -> None:
            global running
            print("\n\nYou pressed Ctrl+C")
            server_socket.close()
            running = False
            sys.exit(0)

        signal.signal(signal.SIGINT, sigint_handler)

        print("Listening on {}:{}\n".format(host_addr, port))
        server_socket.listen(NO_OF_UNACCEPTED_CONNECTIONS)

        while True:
            if not running:
                break

            server_connection, addr = server_socket.accept()

            try:
                while True:
                    data = server_connection.recv(1024).decode()

                    if data == "":
                        break

                    print("{}: {}".format(addr, data))
            except socket.error:
                break

        print("Listening stopped.")

    # connect to server
    else:
        host = DEFAULT_HOST_NAME
        if args_space.host is None:
            print("You have not specified a host. Assuming: {}".format(host))
        else:
            host = args_space.host

        def sigint_handler(
            sig: signal.Signals,
            frame: types.FrameType,
        ) -> None:
            sys.exit(0)

        signal.signal(signal.SIGINT, sigint_handler)

        print("Type to send to {}:{}\n".format(host, port))

        while True:
            data = input()

            client_socket = socket.socket()
            client_socket.connect((host, port))
            client_socket.settimeout(None)
            client_socket.send(data.encode())
            client_socket.close()
