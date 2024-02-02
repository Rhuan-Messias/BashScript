#!/bin/bash

wordlist="admin desafio dev documentacao ftp infrasecreta intranet mail ns1 ns2 parsingok piloto rh srvkey trello wordpress www app _restrito uploads login home css js prog acesso _docs AcessoRestrito robots.txt senha key index _bkp filesarquivos img upload img cadastro"

filetypes="php asp aspx do js phps txt doc docx pdf xls xlsx ppt ovpn sql bak old"

echo "looking for Directories"

for word in ${wordlist};do 
	response=$(curl -s -H "User-agent: disguised" -o /dev/null -w "%{http_code}" $1/$word/) #here it look for directory because of the "/"
	if [ $response == "200" ];  then
		echo "directory found: $1/$word/"
	fi
done

echo "looking for archives" 
for word in ${wordlist};do
       for file in ${filetypes};do
		response=$(curl -s -H "User-agent: disguised" -o /dev/null -w "%{http_code}" $1/$word.$file) #here it look for files with the extention $2
		if [ $response == "200" ];  then
		echo "file found: $1/$word.$file"
		fi
	done
done
