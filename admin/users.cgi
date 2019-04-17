#!/usr/bin/env sh

echo "Content-type: text/html\n\n";
echo "<html>"
echo "<head>"
echo "<title>RC 2 - Usuarios</title>"
echo "<link rel='stylesheet' href='../css/bulma.css'"
echo "</head>"
echo "<body>"
echo "<div class='container'>"
echo "<h1 class='title has-text-centered'>Usuarios</h1>"
echo "<a class='button is-link buttons' href='http://localhost/redes2/admin/controllerUsers.cgi'>Novo Usuario</a>"
echo "<a class='button is-link buttons' href='http://localhost/redes2/admin/controllerUsers
.cgi'>Listar Usuarios</a>"
echo "<a class='button is-link buttons' href='http://localhost/redes2/admin/controllerUsers
.cgi'>Excluir Usuario</a>"
echo "<br /><br />"
echo "<a href='http://localhost/redes2/admin.sh' class='button is-danger buttons'>Voltar</a>"
echo "</div>"
echo "</body>"
echo "</html>"
