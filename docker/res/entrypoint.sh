#!/bin/sh

rm /var/run/xrdp.pid
/usr/sbin/xrdp
rm /var/run/xrdp-sesman.pid
/usr/sbin/xrdp-sesman

# Necesssary for docker
exec "$@"
