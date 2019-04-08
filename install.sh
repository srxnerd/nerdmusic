#!/bin/bash

if [ $EUID != 0 ];then
        echo "please run as root"
        exit
fi
while read line;do
$line
done < requirements.txt
