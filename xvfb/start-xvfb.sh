#!/bin/sh

protector=pro-xvfb.sh
rm spid.txt >/dev/null 2>&1
nohup $PWD/$protector >> running.log 2>&1 &
echo $! > spid.txt

