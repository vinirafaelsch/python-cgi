#!/usr/bin/python3

from db.get_protocols import get_protocols

print('Content-type: text/html\n\n')
print('<html>')
print('<head>')
print('<title>RC 2 - PostgreSQL</title>')
print('<link rel="stylesheet" href="css/bulma.css"')
print('</head>')
print('<body>')
print('<div class="container">')
print('<h1 class="title has-text-centered">Listagem dos Dados</h1>')
print('<table class="table is-striped is-hoverable" style="width:100%">')
print('<tr>')
print('<th>ID</th>')
print('<th>Name</th>')
print('<th>Description</th>')
print('</tr>')

for p in get_protocols():
    print('<tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(p[0], p[1], p[2]))

print('</table>')
print('<a href="http://localhost/redes2/index.py" class="button is-danger">Voltar</a>')
print('</div>')
print('</body>')
print('</html>')


# create table protocolo (
# 	id serial primary key,
# 	nome varchar(10),
# 	descricao text
# );

# INSERT INTO protocolo(nome, descricao) VALUES ('FTP', 'FTP e uma forma de transferir arquivos.')
# INSERT INTO protocolo(nome, descricao) VALUES ('SSH', 'SSH e um protocolo de rede criptografico.')