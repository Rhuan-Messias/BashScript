#!/bin/bash

domain_list="intranet extranet ns1 ns2 mail webmail admin api vpn ftp ssh backup portal proxy monitor firewall gateway" 

for item in ${domain_list}; do 
	host $item.$1 
done | grep -v "NXDOMAIN"
