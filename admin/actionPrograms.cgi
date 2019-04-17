#!/bin/bash
  
echo "content-type: text/html"
echo
echo


VAR=$(sed -n '1p')

name=$(echo $VAR | sed 's/\(name=\)\(.*\)\(\&action=.*\)/\2/;s/+/ /g')
action=$(echo $VAR | sed 's/.*\&action=//')

if [ "$action" = "start" ]; then
	#echo "startou" $name
	#sh $name
        #echo "senha" | su -S 
        touch /tmp/teste.txt
else
	echo "finalizou"
	echo $(killall $name)
fi

