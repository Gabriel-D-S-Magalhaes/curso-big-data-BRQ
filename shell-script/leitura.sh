#!/bin/bash

echo "Entre o primeiro número: "
read num1

echo "Entre o segundo número: "
read num2

if [ $num1 -eq $num2 ]; then 
    echo "Os números são iguais"
else
    echo "Os números são diferentes"
fi