#!/usr/bin/env sh

echo "Content-type: text/html\n\n";
echo "<html>"
echo "<head>"
echo "<title>RC 2 - Admin</title>"
echo "<link rel='stylesheet' href='css/bulma.css'"
echo "</head>"
echo "<body>"
echo "<div class='container'>"
echo "<h1 class='title has-text-centered'>Admin</h1>"
echo "<a class='button is-link buttons' href='http://localhost/redes2/admin/users.cgi'>Gerenciamento de Usuarios</a>"
echo "<a class='button is-link buttons' href='http://localhost/redes2/admin/programs
.cgi'>Gerenciamento de Programas</a>"
echo "<a class='button is-link buttons' href='http://localhost/redes2/admin/services
.cgi'>Gerenciamento de Servicos</a>"
echo "<br /><br />"
echo "<a href='http://localhost/redes2/index.py' class='button is-danger buttons'>Voltar</a>"
echo "</div>"
echo "</body>"
echo "</html>"
