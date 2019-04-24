#!/bin/bash
  
echo "content-type: text/html"
echo
echo

VAR=$(sed -n '1p')

name=$(echo $VAR | sed 's/\(name=\)\(.*\)\(\&action=.*\)/\2/;s/+/ /g')
action=$(echo $VAR | sed 's/.*\&action=//')

sudo service $name $action

echo $name
echo $action
