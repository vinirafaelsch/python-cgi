#!/usr/bin/env sh

echo "Content-type: text/html\n\n";
echo "<html>"
echo "<head>"
echo "<title>RC 2 - Servicos</title>"
echo "<link rel='stylesheet' href='../css/bulma.css'"
echo "</head>"
echo "<body>"
echo "<div class='container'>"
echo "<h1 class='title has-text-centered'>Controle de servicos</h1>"
echo "<form method=\"GET\" action=\"actionServices.cgi\">"

echo "<b>Nome do servico: </b> 
<input class='input' type='text' size=40 name=name value=\"\">"


echo "<br/><br/>"

echo '<input type="radio" name="action" value=create> Iniciar<br>
  <input type="radio" name="action" value=restart> Reiniciar<br>
  <input type="radio" name="action" value=finish> Finalizar'

echo "<br/><br/>"

echo "<input class='button is-link' type='submit' value='Enviar'>"
echo "<a href='http://localhost/redes2/admin.sh' class='button is-danger'>Voltar</a>"

echo "</form>"
echo "</div>"
echo "</body>"
echo "</html>"
