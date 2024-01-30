#!/bin/bash 

search = "firefox"
target = "$1"

echo "Searching in Pastebin"
$search "https:google.com/search?q=site:pastebin.com+$target" 2> /dev/null

echo "Searching in Trello"
$search "https:google.com/search?q=site:trello.com+$target" 2> /dev/null

echo "Searching for extensions"
$search "https:google.com/search?q=site:$target+OR+ext:txt+OR+ext:php" 2> /dev/null
