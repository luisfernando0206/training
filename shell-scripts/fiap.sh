#!/bin/bash

#Adicionando uma variável do tipo string
var="Meu nome é Luis Fernando"

#Printando o resultado da variável na tela
echo "Olá" $var

#Testando a variável $num com um input de dados pelo usuário
echo "Me informe um número:"
read num

#Expondo o conteúdo da váriavel dentro de um echo
echo "O número digitado foi: $num"

#Testando o caractere aspas simples com o crase (exibe o conteúdo independente do valor que tiver dentro)
echo 'O diretório atual é o `pwd`'

#Testando o echo com a crase e aspas duplas, vai mostrar o conteúdo do comando
echo "O diretório atual é o `pwd`"

#Testando o echo com aspas duplas, crase e ponto e virgula, que fará a quebra de linha dentro do comando
echo "Vamos listar o diretório... `ls -l;`"
