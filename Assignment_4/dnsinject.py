# https://thepacketgeek.com/scapy/sniffing-custom-actions/part-1/
# https://www.exploit-db.com/docs/48606
from scapy.all import IP, UDP, DNS, DNSQR
import socket
import sys


def main(interface="wlp2s0", hostnames="hostnames"):
    # https://www.binarytides.com/python-packet-sniffer-code-linux/
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

    # while True:
    # receive a packet from port 53 b/c that's the UDP/DNS port
    packet = s.recvfrom(53)

    print("DNS:", packet[0])

    # https://0xbharath.github.io/art-of-packet-crafting-with-scapy/scapy/creating_packets/index.html
    dnsQuery = IP(dst="10.6.6.6") / UDP(dport=53) /\
        DNS(rd=1, qd=DNSQR(qname="foo.example.com"))

    print(dnsQuery)

    return None


if __name__ == "__main__":
    # Take in command line arguments and pass onto main
    # main(sys.argv[1], sys.argv[2])

    # TODO remove before final implementation
    # Temporary main for testing purposes
    main("wlp2s0", "hostnames")

# Two processes: 1) capturing packets to  a data structure
# 2) Polling into data structure looking for a dns request,
# takes features out of dns, sends packets out to the network
# NEed to exract info out of the packets
