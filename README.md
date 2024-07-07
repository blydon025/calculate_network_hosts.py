# Calculate Network Hosts

A Python script to determine the number of usable IP addresses in a network from the netmask. Ideal for network admins and penetration testers.

## Features

- Supports netmask input in dotted decimal notation (e.g., `255.255.255.0`) and CIDR notation (e.g., `/24`).
- Calculates the number of usable IP addresses by accounting for network and broadcast addresses.

## Usage

1. **Clone the Repository:**
   ```py
   git clone https://github.com/yourusername/calculate_network_hosts.git
   cd calculate_network_hosts
   ```
   
2. **Run the Script**
   ```py
   python calculate_network_hosts.py
   ```

3. **Input the Netmask**
   Input the netmask in either dotted decimal notation or CIDR notation when prompted.
   ```py
   $ python calculate_network_hosts.py
    Enter the netmask (in dotted decimal notation or CIDR notation): 255.255.255.0
    Usable IPs for 255.255.255.0: 254

    $ python calculate_network_hosts.py
    Enter the netmask (in dotted decimal notation or CIDR notation): /26
    Usable IPs for /26: 62
   ```

## Requirements

- Python 3.x

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Brads - @blydon025


   
