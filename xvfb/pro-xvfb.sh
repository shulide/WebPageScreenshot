#!/bin/bash

while :
do
	running=$(ps -ef |grep "Xvfb" | grep -v "grep")
	if [ -z "$running" ] ; then
               	echo -n `date +'%Y-%m-%d %H:%M:%S'`
               	echo "----[Xvfb] service was not started."
               	echo -n `date +'%Y-%m-%d %H:%M:%S'`
               	echo "----Starting [Xvfb] service ."
        	Xvfb :7 -ac -screen 0 1024x768x8 & #>>/dev/null
	fi

	sleep 4s
done
