#!/bin/bash
  
echo "content-type: text/html"
echo
echo


VAR=$(sed -n '1p')

name=$(echo $VAR | sed 's/\(name=\)\(.*\)\(\&action=.*\)/\2/;s/+/ /g')
action=$(echo $VAR | sed 's/.*\&action=//')

if [ "$action" = "adduser" ]; then
	sudo $action --disabled-password --gecos "" $name
else
	echo "Usuario $name deletado com sucesso!"
	sudo $action $name
fi

