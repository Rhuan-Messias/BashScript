#/bin/bash

for ip in $(seq $1 $2); do # first parameter is the start point and second is the final range
       host -t ptr $3.$ip # ptr shows the IP related name, the third parameter is the network part of IP 
done
