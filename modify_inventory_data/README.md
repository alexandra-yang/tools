# Purpose
ODM wants to change all the nodes inventory on opensync NOC with their own logic

# ODM's rule
OS3411 MAC rules since 3.2.7b4: \n
Label MAC is the root MAC to calculate all the others. \n
eth0 MAC = label MAC \n
eth1 MAC = label MAC first octet + 2\n
eth2 MAC = label MAC first octet + 6 \n
Bluetooth MAC = label MAC first octet + 10 \n
2.4G WiFi(wifi1) MAC = label MAC last octet + 1 \n
5G WiFi(wifi0) MAC = label MAC last octet + 2   \n
6G WiFi(wifi2) MAC = label MAC last octet + 3   \n

Example:        \n
LABEL_MAC=FC:20:2E:77:91:50     \n
ETH0_MAC=FC:20:2E:77:91:50      \n
ETH1_MAC=FE:20:2E:77:91:50      \n
ETH2_MAC=02:20:2E:77:91:50      \n
BLE_MAC=06:20:2E:77:91:50       \n
24G_MAC=FC:20:2E:77:91:51       \n
5G_MAC=FC:20:2E:77:91:52        \n
6G_MAC=FC:20:2E:77:91:53        \n

# Usage:
- login http://inventory-development.shared.us-west-2.aws.plume.tech:3005/explorer/
- Use Getter to fetch all devices which is on opensync cloud and store it as 'xxx.json'
- Adjust filter_id.py if there is any logic changed.
- Excute filter_id.py and script will process the xxx.json
- Once you get output csv file
- Import output csv to above URL.

# Wiki:
https://plumedesign.atlassian.net/wiki/spaces/~62a69e98979e6e006903dbf2/pages/14374207495/Modify+node+inventory+python+code
