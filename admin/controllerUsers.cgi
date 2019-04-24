#!/bin/bash
  
echo "content-type: text/html"
echo
echo
echo "<html> <head>"
echo "<link rel='stylesheet' href='../css/bulma.css'/>"
echo "<title> CGI script </title> </head><body>"
echo "<h1 class='title has-text-centered'>Controle de usuarios</h1>"

action="$(echo $QUERY_STRING | sed 's/.*\&action=//')"

if [ "$action" = "action=create" ]; then
	echo "<form method=\"GET\" action=\"actionUsers.cgi\">"
		echo "<b>Nome do usuario: </b> 
		<input class='input' type='text' size=40 name=name value=\"\">"
		echo "<br/>"
		echo "<b>Senha do usuario: </b>
		<input class='input' type='password' size=40 name=password value=\"\">"
		echo "<br/><br/>"
		echo "<input type='hidden' id='action' name='action' value='create'>"
		echo "<input class='button' type='submit' value='Enviar'>"
	echo "</form>"
elif [ "$action" = "action=list" ]; then
		cut -d: -f1 /etc/passwd
else
	echo "<form method=\"POST\" action=\"actionUsers.cgi\">"
		echo "<input type='hidden' id='action' name='action' value='delete'>"
		echo "<b>Nome do usuario: </b> 
		<input class='input' type='text' size=40 name=name value=\"\">"
		echo "<br/><br/>"
		echo "<input class='button' type='submit' value='Enviar'>"
	echo "</form>"
fi

echo "<br/></body><br/></html>"
