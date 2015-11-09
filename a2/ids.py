#!/usr/bin/env python

# Suppress warnings about missing IPv6 route and tcpdump bin
import logging

logging.getLogger("scapy.loading").setLevel(logging.ERROR)
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
import sys


def spoofpkt(p):
    ip_src = p[IP].src
    ip_dst = p[IP].dst
    z = ip_src.split('.')
    y = ip_dst.split('.')
    if not(int(z[0]) == 10 or int(y[0]) == 10):
        print "[Spoofed IP address]: src:" + ip_src + ", dst:" + ip_dst

def unauth(p):
    ip_src = p[IP].src
    ip_dst = p[IP].dst
    tcp_sport = p[TCP].sport
    tcp_dport = p[TCP].dport
    ack = p[TCP].flags
    z = ip_src.split('.')
    y = ip_dst.split('.')
    if( int(z[0]) != 10 and int(y[0]) == 10 and ack == 2):
        print "[Attempted server connection]: rem:" + ip_src + ", srv:" + ip_dst + ", port:" + str(tcp_dport)
    if( int(z[0]) == 10 and int(y[0]) != 10 and ack == 18):
        print "[Accepted server connection]: rem:" + ip_dst + ", srv:" + ip_src + ", port:" + str(tcp_sport)

def sinkhole(p):
    sfil = open('sinkholes.txt',"r")
    badips = sfil.readlines()
    if p[DNS].ancount == 1:
        for c in badips:
           if p[DNS].an.rdata == c.rstrip():
                z = p[DNS].qd.qname.split('.')
                print "[Sinkhole lookup]: src:" + p[IP].dst + ", host:" + z[0] + ".com, ip:" + p[DNS].an.rdata

arpdict = {}
warndict = {}
def arpspoof(p):
    arp_hwsrc = str(p[ARP].hwsrc)
    arp_psrc = str(p[ARP].psrc)
    op = p[ARP].op
    if op == 2:
        if not(arpdict.has_key(arp_psrc)):
            s1 = arp_hwsrc
            s1 = s1.upper()
            arpdict[arp_psrc] = s1
        else:
            if not(warndict.has_key(arp_hwsrc)):
                a1 = arp_hwsrc
                a1 = a1.upper()
                print "[Potential ARP spoofing]: ip:" + p[ARP].psrc + ", old:" + arpdict[arp_psrc] + ", new:" + a1
                warndict[arp_hwsrc] = 1

def iisworm(p):
    portnum = p[TCP].dport
    if portnum == 80:
        pl = str(p.payload)
        if(pl.find("%255c") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%25%35%63") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%252f") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%%35c") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%%35%63") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%C1%1C") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%C1%9C") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%C0%AF") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%c1%1c") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%c0%qf") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%c1%9c") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%c1%af") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%c0%af") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%e0%80%af") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%f0%80%80%af") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%f8%80%80%80%af") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%fc%80%80%80%80%af") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst
        if(pl.find("%e0\%80\%af") != -1):
            print "[Unicode IIS exploit]: src:" + p[IP].src + ", dst:" + p[IP].dst

def ntpddos(p):
    udp_dport = p[UDP].dport
    if udp_dport == 123:
        if p[Raw].load[3] == "*":
            print "[NTP DDoS]: vic:" + p[IP].src + ", srv:" + p[IP].dst


thisfile = sys.argv[1]
packets = rdpcap(thisfile)
packet_num = 0
packet_total_sum = 0
c = 0
for p in packets:
    packet_num+=1
    packet_total_sum += len(p)
    if IP in p:
        spoofpkt(p)
    if IP in p and UDP in p:
        ntpddos(p)
    if IP in p and TCP in p:
        unauth(p)
        iisworm(p)
    if DNS in p:
        sinkhole(p)
    if ARP in p:
        arpspoof(p)
print "Analyzed " + str(packet_num) + " packets, " + str(packet_total_sum) + " bytes"