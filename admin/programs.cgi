#!/usr/bin/env sh

echo "Content-type: text/html\n\n";
echo "<html>"
echo "<head>"
echo "<title>RC 2 - Programas</title>"
echo "<link rel='stylesheet' href='../css/bulma.css'"
echo "</head>"
echo "<body>"
echo "<div class='container'>"
echo "<h1 class='title has-text-centered'>Programas</h1>"
echo "<form method=\"POST\" action=\"actionPrograms.cgi\">"

echo "<b>Nome do programa: </b> 
<input class='input' type='text' size=40 name=name value=\"\">"

echo "<br/><br/>"

echo '<input type="radio" name="action" value=start> Iniciar<br>
  <input type="radio" name="action" value=stop> Finalizar'

echo "<br/><br/>"

echo "<a href='http://localhost/redes2/admin.sh' class='button is-danger'>Voltar</a>"
echo "<input class='button is-link' type='submit' value='Enviar'>"

echo "</form>"
echo "</div>"
echo "</body>"
echo "</html>"
