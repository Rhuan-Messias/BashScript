#!/bin/bash

if [ "$#" -eq 2 ]; #if the number of parameter are equal 2, then execute the code, else, give some explanation
then 
	lynx --dump "https://google.com/search?&q=site:$1+ext:$2" |grep ".pdf"
else
	echo "-------------------------------------------"
	echo "Support /pdf/doc/docx/xls/xlsx/ppt/pptx/"
	echo "-------------------------------------------"
	echo "Example: ./metanalyzer.sh target.com docx"
	echo "-------------------------------------------"
fi
