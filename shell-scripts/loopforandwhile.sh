#!/bin/bash

#Para a variável 1 faça, conte até 5 e depois exponha a variável i
for i in $(seq 5); do
	echo $i
done

echo "Este foi o comando for"
echo " "

#loop while para contar até 5
CONTADOR=0

#Enquanto a variável contador for menor que (lt = lower then) 6 faça, exponha o valor do contador, incremente o contador com +1
while [ $CONTADOR  -lt 6 ]; do
	echo $CONTADOR
	let CONTADOR=CONTADOR+1;
done
echo "Este foi o comando while"
