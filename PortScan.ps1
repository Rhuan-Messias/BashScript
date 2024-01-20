param($ip,$port)

if (Test-NetConnection $ip -Port $port -WarningAction SilentlyContinue -InformationLevel Quiet) {
    echo "Port is Open"
} else {
    echo "Port is Closed"
}