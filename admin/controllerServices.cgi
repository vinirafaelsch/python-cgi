#!/bin/bash
  
echo "content-type: text/html"
echo
echo
echo "<html> <head>"
echo "<link rel='stylesheet' href='../css/bulma.css'/>"
echo "<title> CGI script </title> </head><body>"
  
echo "<h1 class='title has-text-centered'>Controle de servicos</h1>"
echo "<form method=\"GET\" action=\"actionServices.cgi\">"

echo "<b>Nome do servico: </b> 
<input class='input' type='text' size=40 name=name value=\"\">"

action=$(echo $VAR | sed 's/\(action=\)\(.*\)')
echo $action
if [ "$QUERY_STRING" = "action=create"]; then
	echo '<input type="hidden" name="action" value="create">'
elif [ "$QUERY_STRING" = "action=restart"]; then
	echo "<input type='hidden' name='action' value='restart'>"
else
	echo "<input type='hidden' name='action' value='finish'>"
fi
echo "<br/><br/>"
echo "<input class='button' type='submit' value='Enviar'>"

echo "</form><br/></body><br/></html>"
