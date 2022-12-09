# Author: Alexandra Yang
# Email: ayang@plume.com
# Purpose: This tool is to modify os3411's inventory,
#           and store it into csv.

import string
import sys
import json
import re
import csv

def macToInt(mac):
    mac = mac.replace(":", "")
    return int(mac, 16)


def intToMac(intMac):
    if len(hex(intMac)) % 2 != 0:
        hexStr = '0{0:X}'.format(intMac)
    else:
        hexStr = '{0:X}'.format(intMac)

    i = 0
    ret = ""

    while i <= len(hexStr) - 2:
        if ret == "":
            ret = hexStr[i:(i + 2)]
        else:
            ret = "".join([ret, ":", hexStr[i:(i + 2)]])
        i = i + 2
    return ret

# Read all OS3411 inventory data through API
def read_article_file():
    with open('OS3411_all_inventory_dev_NOC.json') as f:
        contents = json.load(f)
        f.close()
    return contents

# fileter the required data and process it.
def fileter_id(contents):
    # define a dictionary
    json_list = []
    for item in contents:
        store_details = {}
        try:
            pod_sn = item['serialNumber']
            serialNumber = item['serialNumber']
            node_model = item['model']
            eth0_mac = item['ethernetMac']

        except KeyError as e:
            #print('KeyError: ',e, pod_sn)
            continue



        # ETH MAC calculate
        post_eth = eth0_mac[2:]
        prefix_eth1 = int(eth0_mac[:2], 16) + 2

        eth1_mac = '{:x}'.format(int(eth0_mac[:2], 16) + 2) + post_eth
        eth2_mac = '{:x}'.format(int(eth0_mac[:2], 16) + 6) + post_eth
        bt_mac = hex(int(eth0_mac[:2], 16) + 10)[-2:]+post_eth


        # WIFI MAC calculate
        wifi24_mac = intToMac(macToInt(eth0_mac)+1)
        wifi5_mac = intToMac(macToInt(eth0_mac)+2)
        wifi6_mac = intToMac(macToInt(eth0_mac)+3)

        #store_details.append({'POD_NO':pod_sn, 'NODE_MODEL':node_model, 'POD_SN':serialNumber, 'ETH0_MAC':eth0_mac, 'ETH1_MAC': eth1_mac, 'WIFI24_MAC': wifi24_mac, 'WIFI5_MAC': wifi5_mac, 'WIFI6_MAC': wifi6_mac, 'BT_MAC': bt_mac, 'WIFI5_MAC': wifi5_mac})
        store_details.update({'POD_NO':pod_sn, 'NODE_MODEL':node_model, 'POD_SN':serialNumber, 'ETH0_MAC':eth0_mac, 'ETH1_MAC': eth1_mac, 'WIFI24_MAC': wifi24_mac, 'WIFI5_MAC': wifi5_mac, 'WIFI6_MAC': wifi6_mac, 'BT_MAC': bt_mac, 'WIFI5_MAC': wifi5_mac})
        print(pod_sn)
        json_list += [store_details]

    print(json_list)
    return json_list

# Write them into csv
def write_csv_using_dict_writer(file_path, rows_data, headings):
    with open(file_path, 'w') as csvfile:
        data_writer = csv.DictWriter(csvfile, fieldnames=headings, lineterminator='\n')
        data_writer.writeheader()
        data_writer.writerows(rows_data)
    return True



headings = ['POD_NO', 'NODE_MODEL', 'POD_SN', 'ETH0_MAC', 'ETH1_MAC', 'WIFI24_MAC', 'WIFI5_MAC', 'WIFI6_MAC', 'BT_MAC', 'WIFI5_MAC']
contents = read_article_file()
parsed_data = fileter_id(contents)
write_csv_using_dict_writer('parse_json.csv', parsed_data, headings)
