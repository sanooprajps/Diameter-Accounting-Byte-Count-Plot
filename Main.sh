#!/bin/bash

##################################################
## Script will count bytes from diameter interfaces like PGW, CCF etc.
## It accepts packet captures from above interfaces
## And it accepts server port - ccf port
##################################################

#if [ $# -ne 4 ]; then
	#clear; echo -e "Number of arguments given are wrong ...\n"; echo $LINE
	#echo -e "Usage : `basename "$0"` <Pgw pcap> <Client pcap> <CCF pcap> <CCF Port>"; echo $LINE
	#exit
#fi

#################################################
## Variable initialization
#################################################

client_pcap=$1
server_pcap=$2
server_port=$3
client_port=$4

#echo -e "Inside shell script ---: $client_pcap"
#echo -e "Inside shell script ---: $server_pcap"
#echo -e "Inside shell script ---: $server_port"
#echo -e "Inside shell script ---: $client_port"


clear

#################################################
## Packet capture parser
## Make sure tshark is installed in the server that you are running this script.
#################################################

tshark -r ${client_pcap} -odiameter.tcp.ports:${client_port} -R 'diameter.cmd.code == 271 and diameter.flags.request==1 and !tcp.analysis.retransmission' -Tpdml -Tfields -ediameter.Subscription-Id-Data -ediameter.Session-Id  -ediameter.Accounting-Record-Type -ediameter.Accounting-Record-Number -ediameter.Accounting-Input-Octets -ediameter.Accounting-Output-Octets -ediameter.Rating-Group  >clientPacketinfo.txt

#################################################
## Graph - MDN --> Session count
#################################################

mdnUniq=`cat clientPacketinfo.txt | awk '{print $1}' | sort | uniq`

rm -f graph-mdn-sessionCount.txt 2>/dev/null

for mdn in $mdnUniq
do
	sessionCount=`grep -w "$mdn" clientPacketinfo.txt | awk '{print $2}' | wc -l`
	validationCount=`grep -w $mdn clientPacketinfo.txt | awk '{print $7}' | grep -o 9005 | wc -l`
	flowCount=`grep -w $mdn clientPacketinfo.txt | awk '{print $7}' | grep -o 9002 | wc -l`
	echo "$mdn,$sessionCount,$validationCount,$flowCount" >>graph-mdn-sessionCount.txt
done

##################################################
## Cleaning tmp files
##################################################

#rm -f clientPacketinfo.txt ccfPacketinfo.txt
