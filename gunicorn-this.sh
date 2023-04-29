#!/usr/bin/env bash
THISPATH=$(realpath $0)
THISDIR=$(dirname $THISPATH)
cd $THISDIR
gunicorn -w 4 -b viniciusmacielf.pythonanywhere.com:80 flask-pybrcode:app --daemon
echo "server running"
