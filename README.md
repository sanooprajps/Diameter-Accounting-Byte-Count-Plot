# Diameter-Accounting-Byte-Count-Plot
This will parse diameter interface (Client and Server) packet capture and calculate Client side and Server side bytes out of it. These values are plotted as graphical images.

Main.sh
-------
## Script will count bytes from diameter interfaces like PGW, CCF etc.
## It accepts packet captures from above interfaces
## And it accepts server port - ccf port

Usage: ./Main.sh <Pgw pcap> <Client pcap> <CCF pcap> <CCF Port>
  
diameterTrace.py
----------------
## Script will count Client & server side Accounting input/ouput octets
## Script accepts Client, server side pcaps and server port as the input
## Output will be sum of Client/Server, Accounting input/output bytes

It automatically takes input as "graph-mdn-sessionCount.txt" file (This is having byte records), and plot the graph.
