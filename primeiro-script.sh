

#!/bin/bash
###################################
#
# primeiro-script.sh
#
# Autor: Fabrizio
# Data de crição: 02 de maio de 2022
#
# Descrição: Primeiro Script de Criação da Aula de Big Data
###################################

echo 'Texto no console'

echo 'Criando pasta...'
mkdir -p diretorio-brq
# mkdir serve para criar uma pasta. 
# Se usarmos o parâmetro -p, permite criar
#   pastas não existentes ou não apresentar erros
#   quando a pasta já existe
# ex: mkdir -p diretorio-brq

ls -ls
# ls lista todas as pastas do diretório de interesse junto
#   com detalhes de horário de criação/modificação e suas permissões (parâmetro -l)

rm -r diretorio-brq
# rm deleta arquivos ou pastas de interesse.
# para deletar uma pasta, devemos passar o parâmetro -r (recursivo) 

#tail -f arquivo.txt
# serve para mostrar as últimas linhas de um aquivo
#   e deixar o mesmo aberto para vermos as novas linhas
#   inseridas no final do arquivo

#sleep 3
# serve para "dormir" (parar console) por x segundos

touch arquivo.txt
# touch serve para criar um arquivo vazio ou para atualizar
#   a data de modificação do arquivo

# defini uma variável com o nome CONTADOR e iniciei o valor com 0
CONTADOR_UM=0
#PASTA="/c/Users/ffbor/Desktop/brq"
PASTA="/home/virtual/Desktop/brq"

# imprimi o conteúdo da variável contador (não esquecer do $)
echo "O valor do CONTADOR é $CONTADOR_UM"

echo "usando LS"
ls $PASTA

DATAHORA=$(date +%Y-%m-%d---%H:%M)

echo "$DATAHORA usando PWD"
pwd


# man -> é o manual dos comandos linux
# Ex: man tail

# wc <arquivo>
# Conta a qtd de linhas, palavras e caracteres
# Saída:
# <linhas> <palavras> <caracteres>
#
# -l = Imprime só o número de linhas
# -w = Imprime só o número de palavras
# -c = Imprime só o número de caracteres

# pipe (|) serve para pegar o resultado de um comando e inserir como entrada
# em um proximo  comando

# comando  > arquivo --- coloca o resultado de um 


# grep serve para buscar uma  palavra dentro de um arquivo
#ex: grep frase arquivo.txt 
#ao passa o comando -R (recursivo), iiremos buscar uma palavra dentro
# dos arquivos de um diretorio

# wget faz download de  um arquivo

# Comandos em sequência
# command1 ; command2

# Comandos em sequência, apenas se ambos funcionarem 
# command1 && command2

# Comandos em sequência, com o 2º comando em background
# command1 & command2

echo "\n----------\tARGUMENTOS\t----------\n"
echo "Nome do script: \t$0" # $0 = nome do script
echo "Primeiro argumento: \t$1"
echo "Qtd. de arguemntos: \t$#"

echo "\n----------\tCONDICIONAIS\t----------\n"

# -eq <-- equals
# -ge <-- greater than
# -le <-- lower than

if [ $# -ge 0 ]; then
    echo "Informe um argumento"
    exit 1
fi