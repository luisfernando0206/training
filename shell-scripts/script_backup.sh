#!/bin/bash

#RM86693

#Entra no diretório 
cd /backup

#Cria o backup do mysql
mysqldump feirinha -u feirinha_backup -pnFUFaLAkA%@rK9eKQYQfB31nI --single-transaction --no-tablespaces >> feirinha_mysql_$(date +%Y-%m-%d).dump 

#Cria a compactação do aquivo de backup do mysql
tar cvfj feirinha_mysql_$(date +%Y-%m-%d).dump.tar.bz2 feirinha_mysql_$(date +%Y-%m-%d).dump

#Remove o arquivo de backup do mysql que está descompactado
rm -f feirinha_mysql_$(date +%Y-%m-%d).dump

#Cria o backup do wordpress
tar cvfj feirinha_$(date +%Y-%m-%d).tar.bz2 /var/www/html/wordpress/


