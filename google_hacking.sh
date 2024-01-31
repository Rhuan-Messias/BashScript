#!/bin/bash

engine="$1"
files="php asp aspx do js txt doc docx pdf xls ppt ovpn sql bak old"

for extension in $files; do 
	$engine "https://google.com/search?&q=site:$2.br+ext:$extension"
done
