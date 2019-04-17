#!/bin/bash
  
echo "content-type: text/plain"
echo
echo
echo "<html> <head> <title> CGI script </title> </head>
<body>"

VAR=$(sed -n '1p')

name=$(echo $VAR | sed 's/\(name=\)\(.*\)\(\&action=.*\)/\2/;s/+/ /g')
action=$(echo $VAR | sed 's/.*\&action=//')

if [ "$action" = "start" ]; then
	echo "startou" $name
	$name &
else
	echo "finalizou"
	killall $name
fi

service $name $action


echo "</body>"
echo "</html>"
