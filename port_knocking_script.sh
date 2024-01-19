#!/bin/bash

# Informações de IP e Portas para o Knocking 
ip="37.59.174.235"
ports="3000 30000 37 13"


green='\033[0,32m'
vermelho="\e[91m"
nc='\033[0m'

#executa o comando knock responsável pelo port knocking
knock -v $ip $ports

#Teste para saber se o comando funcionou
if [ $? -eq 0 ]; then
	echo -e "${green}[+] Port knocking funciou corretamente!${nc}"
else
	echo "${vermelho}[-]Port Knocking falhou! Verifique as informações.${nc}" 
fi
