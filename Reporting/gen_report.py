"""
Script name: gen_report.py
This script prints out all hosts that are connected to DNAC network devices in a tabular list format.
"""

import sys
from dnac import *
from mail import send_mail
import config

def get_host():
    """
    This function returns a tabular list of all hosts that are connected to DNAC network devices.
    Return:
    ------
    list: a list of all hosts and network devices with a number tag
    """
    host_list=[]
    try:
        resp = get(api="host")
        response_json = resp.json()
        print ("Status: ",resp.status_code)
    except:
        print ("Something wrong with GET /host request!")
        sys.exit(1)
    # Now create a list of host summary
    i=0
    for item in response_json["response"]:
        i+=1
        host_list.append([i,item["hostIp"],item["hostMac"],item["hostType"],item["connectedNetworkDeviceName"]])
    return host_list

def get_network_device():
    """
    This function returns a tabular list of all network devices.
    Return:
    ------
    list: a list of all network devices with a number tag
    """
    network_device_list=[]
    try:
        resp = get(api="network-device")
        response_json = resp.json()
        print ("Status: ",resp.status_code)
    except:
        print ("Something wrong with GET /network-device request!")
        sys.exit(1)
    # Now create a list of host summary
    i=0
    for item in response_json["response"]:
        i+=1
        network_device_list.append([i,item["hostname"],item["reachabilityStatus"],item["collectionStatus"], item["managementIpAddress"], item["type"], item["macAddress"],item["bootDateTime"]])
    return network_device_list

if __name__ == "__main__":
    host=get_host()
    networkDevice=get_network_device()
    message = "\n#### All Hosts connected to the Network ####\n" + \
              (tabulate(host,headers=['Number','Host IP','Mac Address ','Host Type','Connected to Network Device'], tablefmt="rst")) + \
              "\n\n#### All Network Devices ####\n" + \
              (tabulate(networkDevice, headers=['Number','Hostname','Reachability','Collection Status','IP Address','type','Mac Address','Boot Time'], tablefmt="rst"))
    for recipient in config.MAIL_RECIPIENTS:
        send_mail(recipient, message)






