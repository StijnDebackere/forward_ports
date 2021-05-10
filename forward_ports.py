#!/usr/bin/env python3
import argparse
import subprocess


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument(
    "port", default=8888, type=int, help="Port to forward."
)
parser.add_argument(
    "host", default="purmer", type=str, help="Host to forward."
)
parser.add_argument(
    "-r", "--remote", type=str, help="Also forward port on host to remote."
)


def forward_port_to_remote(port, host, remote):
    subprocess.run(["echo", f"Forwarding port {port} to host {host} and remote {remote}"])
    if remote is not None:
        proc = subprocess.run(["ssh", "-f", host, f"ssh -NfL localhost:{port}:localhost:{port} {remote}"])

    proc = subprocess.run(["ssh", "-NfL", f"localhost:{port}:localhost:{port}", host])


if __name__ == '__main__':
    args = parser.parse_args()
    forward_port_to_remote(port=args.port, host=args.host, remote=vars(args).get("remote", None))
