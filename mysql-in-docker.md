# Usando MySQL no Docker 

## Baixa Imagem
`docker pull mysql:5.7`

## Executa Container 
`docker run -d --name=mysql -p 3306:3306 --env="MYSQL_ROOT_PASSWORD=root" mysql:5.7`

## Executa o Container com "Volume"
`docker run -d --name=mysql -p 3306:3306 --env="MYSQL_ROOT_PASSWORD=root" -v ${PWD}/volume/mysql:/var/lib/mysql mysql:5.7`

O valor do parâmetro "-v" é separado com ":".
O que vier antes é o caminho para um diretório no Host, o que vier depois é o caminho para um diretório no Container.
Em nosso caso, estamos mapeando a pasta que contém tudo o que é necessário para a estrutura das Bases de Dados. Portanto é como se fosse feito um backup das bases de dados do container para o host.

## Acessa o Bash do container 
`docker exec -it mysql /bin/bash`

## Conectar-se ao MySQL Solicitando a Senha
`mysql -u root -p`

## Lista o nome de todos os usuários
`SELECT user FROM mysql.user;`

## Criar Usuário
`create user 'user1'@'localhost' IDENTIFIED BY 'user1';`

## Conceder Privilégios 
`GRANT ALL PRIVILEGES ON *.* TO 'user1'@'localhost' WITH GRANT OPTION;`

## Listas Base de Dados
`show databases;`

## Criar Base de Dados
`create database <name_db>;`


