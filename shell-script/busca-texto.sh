#!/bin/bash
###################################
#
# busca-texto.sh
#
# Autor: Gabriel Magalhães
# Data de crição: 04 de maio de 2022
#
# Descrição: Recebe 2 argumentos sendo o 1º o nome de um arquivo e o 2º o texto a ser procurado dentro do arquivo
###################################

if [ $# -le 1 ]; then
    echo "Nome do arquivo e texto a ser procurado são obrigatórios"
    exit 1
fi

echo "Procurando \"$2\" no arquivo \"$1\""

CONTADOR=$(grep -ic -n $2.* $1)
echo "CONTADOR $CONTADOR"

if [ $CONTADOR -eq 0 ]; then
    echo "Nenhuma ocorrência da palavra \"$2\"."
    exit 1
elif [ $CONTADOR -ge 3 ]; then
    echo "Há muitas ocorrências da palavra \"$2\"."    
else 
    echo "$CONTADOR ocorrência(s) da palavra \"$2\""
fi