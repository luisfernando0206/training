#!/bin/bash

# Script de exemplo de controle de fluxo IF

echo "Vamos verificar a data corrente..."
sleep 2
echo " "

if date | grep Sun
then
	echo "Aproveite o Dia"

elif date | grep Sat
then
	echo "Você está de home Office"

else
	echo "Vá estudar"
fi	
