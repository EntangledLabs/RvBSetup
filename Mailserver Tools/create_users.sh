#!/bin/bash

systemctl stop dovecot
systemctl stop postfix

for n in $(seq 1 $1);
do
  echo "adminbee$n"
  useradd "adminbee$n" -m -N -G adminbees -s /bin/bash
done

for i in $(seq 1 $1);
do
  echo "adminbee$i:buzzbuzz!" > passwd.txt
  chpasswd < passwd.txt
done

rm passwd.txt

for i in $(seq 1 $1);
do
  echo "172.16.$i.3 adminbee$i" >> /etc/hosts
done

systemctl start dovecot
systemctl start postfix