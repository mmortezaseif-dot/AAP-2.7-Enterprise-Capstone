#!/usr/bin/env python3
import argparse
import select
import socket
import ssl


def relay(client, upstream):
    sockets = [client, upstream]
    while True:
        readable, _, _ = select.select(sockets, [], [], 60)
        if not readable:
            continue
        for source in readable:
            data = source.recv(65535)
            if not data:
                return
            target = upstream if source is client else client
            target.sendall(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--listen-host", default="127.0.0.1")
    parser.add_argument("--listen-port", type=int, required=True)
    parser.add_argument("--remote-host", required=True)
    parser.add_argument("--remote-port", type=int, required=True)
    args = parser.parse_args()

    context = ssl.create_default_context()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((args.listen_host, args.listen_port))
        listener.listen(5)

        while True:
            client, _ = listener.accept()
            try:
                raw_upstream = socket.create_connection(
                    (args.remote_host, args.remote_port), timeout=20
                )
                with context.wrap_socket(
                    raw_upstream, server_hostname=args.remote_host
                ) as upstream:
                    with client:
                        relay(client, upstream)
            except Exception:
                client.close()
                raise


if __name__ == "__main__":
    main()
