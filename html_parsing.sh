#!/bin/bash
# Código de escape ANSI para cor amarela
amarelo='\e[1;33m'
verde='\e[32m'
azul='\e[94m'
rosa='\e[95m'
vermelho='\e[91m'
reset='\e[0m'
indice='0'
dominio='arquivado'

#rm index.html

if [ "$1" == "" ];
then
	echo -e "${amarelo}#########################################"
	echo "|->            PARSING HTML           <-|"
	echo "|->   Desec Security - Rhuan Messias  <-|"
	echo "|-> ./html_parsing.sh www.alvo.com.br <-|"
	echo -e "#########################################${reset}"
else
	wget -qO- $1 | grep http | cut -d "/" -f 3 | cut -d '"' -f1 > cache.txt
	for domain in $(cat cache.txt); do host $domain|grep -v "not found"| grep "has address" | cut -d ' ' -f4 | sed "s/,//" >> $1.ip.txt 
	done

	for domain in $(cat cache.txt); do host $domain|grep -v "not found"| grep "has address" | cut -d ' ' -f1  >> $1.domains.txt 
	done

	echo -e "${amarelo}================================================================${reset}"
	echo -e "${amarelo}#########################################"
	echo "|->            PARSING HTML           <-|"
	echo "|->   Desec Security - Rhuan Messias  <-|"
	echo -e "#########################################${reset}"
	echo -e "${azul}[+] Resolvendo URLs em:${reset} ${verde}$1${reset}"
	echo -e "${amarelo}================================================================${reset}"
	echo ""
	echo -e "${azul}[+] Concluído Salvando os resultados em: ${verde}$1.ip.txt${reset}"
	echo ""
	echo -e "${amarelo}================================================================${reset}"
	echo -e "     ${azul} LINE                   IP                ADDRESS${reset}"
	echo -e "${amarelo}================================================================${reset}"
	paste "$1.ip.txt" "$1.domains.txt" | while IFS=$'\t' read -r id nome; do
    	echo -e "${azul}IP:${verde} $id     ${azul} Domain: ${verde}$nome"
	done
	echo -e "${amarelo}================================================================${reset}"
fi

#precisa comentar as opções abaixo para conseguir manter os arquivos salvos
rm $1.ip.txt
rm $1.domains.txt
rm cache.txt
