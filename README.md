# calculate_network_hosts.py
A Python script to determine the number of usable IP addresses in a network from the netmask. Ideal for network admins and pentesters.

Features
Supports netmask input in dotted decimal notation (e.g., 255.255.255.0) and CIDR notation (e.g., /24).
Calculates the number of usable IP addresses by accounting for network and broadcast addresses.
Usage
Clone the Repository:

```sh
git clone https://github.com/yourusername/calculate_network_hosts.git
cd calculate_network_hosts
Run the Script:
```

```sh
python calculate_network_hosts.py
Enter the Netmask:
Input the netmask in either dotted decimal notation or CIDR notation when prompted.
```

```sh
$ python calculate_network_hosts.py
Enter the netmask (in dotted decimal notation or CIDR notation): 255.255.255.0
Usable IPs for 255.255.255.0: 254

$ python calculate_network_hosts.py
Enter the netmask (in dotted decimal notation or CIDR notation): /26
Usable IPs for /26: 62
```

Requirements
Python 3.x
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Brads - blydon025
