# IP or domain name to be pinged
$IP = "8.8.8.8"

# Get the computers name
$pcname = Get-Item env:USERDOMAIN | select -ExpandProperty "Value"

$filename = $pcname + "_PING-TEST.txt"

# where to write the files - preferable to a UNC path for domain logging
$filepath = ".\" + $filename

# Ping and write output to filepath
ping.exe $IP | Out-File $filepath