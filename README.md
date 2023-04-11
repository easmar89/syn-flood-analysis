# SYN Flood Analysis

A new low level exploration. This time we analyze a pcap file to determine the percentage of incoming SYN messages that were ACKed. The analysis is performed without using any network traffic tools such as Wireshark, relying only on reading binary data from the pcap file.

<br>

## Objectives

- Understand the structure of a PCAP file.
- Understand the structure of IP and TCP headers and payloads.
- Understand what a SYN flood attack is.

<br>

## Syn flood attack:

From [wikipedia](https://en.wikipedia.org/wiki/SYN_flood):

> A SYN flood is a form of denial-of-service attack in which an attacker rapidly initiates a connection to a server without finalizing the connection. The server has to spend resources waiting for half-opened connections, which can consume enough resources to make the system unresponsive to legitimate traffic.

<br>

## Program sample output:

```txt
...
80 -> 49183  SYN  ACK
58084 -> 80  SYN
58085 -> 80  SYN
80 -> 49184  SYN  ACK
58086 -> 80  SYN
58087 -> 80  SYN
80 -> 49185  SYN  ACK
58088 -> 80  SYN
58089 -> 80  SYN
80 -> 49187  SYN  ACK
58090 -> 80  SYN
80 -> 49188  SYN  ACK
58091 -> 80  SYN
80 -> 49190  SYN  ACK
58092 -> 80  SYN
58093 -> 80  SYN
80 -> 49191  SYN  ACK
58094 -> 80  SYN
58095 -> 80  SYN
80 -> 49192  SYN  ACK
58096 -> 80  SYN
80 -> 49193  SYN  ACK
58097 -> 80  SYN
58098 -> 80  SYN
80 -> 49194  SYN  ACK
58099 -> 80  SYN

Total number of packets:  95829
Total number of SYN sent to port 80:  56298
Total number of SYN acknowledged by the server: 39531
Percentage of ACKed SYNs: 70.22%
```

We see a shortage of 30%. Due to the syn flood attack, the server was unable to respond to 30% of the requests. It's far from being a complete DoS, but something to investigate and learn more about.
