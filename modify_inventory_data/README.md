# Purpose
ODM wants to change all the nodes inventory on opensync NOC with their own logic

# ODM's rule
OS3411 MAC rules since 3.2.7b4: \
Label MAC is the root MAC to calculate all the others. \
eth0 MAC = label MAC \
eth1 MAC = label MAC first octet + 2\
eth2 MAC = label MAC first octet + 6 \
Bluetooth MAC = label MAC first octet + 10 \
2.4G WiFi(wifi1) MAC = label MAC last octet + 1 \
5G WiFi(wifi0) MAC = label MAC last octet + 2   \
6G WiFi(wifi2) MAC = label MAC last octet + 3   \

Example:        \
LABEL_MAC=FC:20:2E:77:91:50     \
ETH0_MAC=FC:20:2E:77:91:50      \
ETH1_MAC=FE:20:2E:77:91:50      \
ETH2_MAC=02:20:2E:77:91:50      \
BLE_MAC=06:20:2E:77:91:50       \
24G_MAC=FC:20:2E:77:91:51       \
5G_MAC=FC:20:2E:77:91:52        \
6G_MAC=FC:20:2E:77:91:53        \

# Usage:
- login http://inventory-development.shared.us-west-2.aws.plume.tech:3005/explorer/
- Use Getter to fetch all devices which is on opensync cloud and store it as 'xxx.json'
- Adjust filter_id.py if there is any logic changed.
- Excute filter_id.py and script will process the xxx.json
- Once you get output csv file
- Import output csv to above URL.

# Wiki:
https://plumedesign.atlassian.net/wiki/spaces/~62a69e98979e6e006903dbf2/pages/14374207495/Modify+node+inventory+python+code
