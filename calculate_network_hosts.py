# calculate_network_hosts.py

import ipaddress


def calculate_hosts(netmask):
    # Convert the netmask to a network object
    network = ipaddress.IPv4Network(f'0.0.0.0/{netmask}', strict=False)
    # Calculate the number of hosts
    num_hosts = network.num_addresses - 2  # subtract network and broadcast addresses
    return num_hosts


def main():
    # Ask the user for a netmask
    netmask = input(
        "Enter the netmask (in dotted decimal notation or CIDR notation): ")
    # Calculate the number of usable hosts
    try:
        num_hosts = calculate_hosts(netmask)
        print(f'Usable IPs for {netmask}: {num_hosts}')
    except ValueError as e:
        print(f'Invalid netmask provided: {e}')
    main()


if __name__ == "__main__":
    main()
