$link = Read-Host "Type your website: "
try{$web = Invoke-WebRequest -uri "$link" -Method Options
echo "O servidor roda: "
$web.headers.server
echo ""
echo "O servidor aceita os métodos: "
$web.headers.allow} catch{}
echo ""
echo "Links: "
$web2 = Invoke-WebRequest -uri "$link"
$web2.links.href | Select-String http://
