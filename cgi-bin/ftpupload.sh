#!/bin/bash
#Param:
# $1 --local file directory
# $2 --upload file name

ftp_svr_addr=192.168.1.28
ftp_svr_port=2122
ftp_username=webserver
ftp_password=tangyibo

cd $1
ftp -inv $ftp_svr_addr $ftp_svr_port <<eof
user $ftp_username $ftp_password
binary
cd /
put $2
bye
eof

