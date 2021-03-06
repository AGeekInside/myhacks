import better_exceptions
import click
import os

import myhacks as myh


@click.command()
@click.argument("parameter", required=False)
def run_myip(parameter):
    """Outputs the ip addresses for the host it runs on."""

    host_name, ip = myh.get_hostname_ip()

    print(f"Host: {host_name}\tip: {ip}")


if __name__ == "__main__":
    run_myip()
