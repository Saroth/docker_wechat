#!/bin/sh

/usr/sbin/xrdp
/usr/sbin/xrdp-sesman

# Necesssary for docker
exec "$@"
