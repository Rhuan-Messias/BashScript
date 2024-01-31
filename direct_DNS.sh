#!/bin/bash

domain_list="firewall monitoring monitoramento intranet ns1 ns01 mail ns2 webmail rh sistema system admin logs devs documentos server api docs doc"

for item in ${domain_list}; do 
	host $item.$1 
done | grep -v "NXDOMAIN"
