param($ip)
if(!$ip){
    echo "==========> MESSIAS - PORTSCAN <=========="
    echo "Remember to Input an IP address"
    echo "Exemplo: .\PortScan.ps1 192.169.0.0"
} else{
    $topports = 21,22,3306,80,443
    #$yourports = 1111
    #$allports = 1..65535
    try {foreach($port in $topports){
            if (Test-NetConnection $ip -Port $port -WarningAction SilentlyContinue -InformationLevel Quiet) {
            echo "Port $port is Open"
       }} else {
            echo "Port $port is Closed"
        }
    } catch{}   
}

