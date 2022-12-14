#!/bin/bash

systemctl stop dovecot
systemctl stop postfix

for n in $(seq 1 $1);
do
  echo "adminbee$n"
  userdel "adminbee$n" -f -r
done

head -n -$1 /etc/hosts > /etc/hosts

systemctl start dovecot
systemctl start postfix