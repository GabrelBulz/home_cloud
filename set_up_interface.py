#!/usr/bin/env python

import sys
import os

def set_up_interface():

    interface = sys.argv[1]
    ip_static = sys.argv[2]
    mask = sys.argv[3]
    gateway = sys.argv[4]
    DNS = sys.argv[5]

    f = open(interface, 'rw+')
    f.write("auto " + interface + "\n"
            + "iface " + interface + " inet static\n"
            + "address " + ip_static + "\n"
            + "netmask " + mask + "\n"
            + "gateway " + gateway + "\n"
            + "dns-nameservers " + DNS)
    f.close()

def main():

    if os.geteuid() is 0:
        set_up_interface()
    else:
        print("You must be root")

main()