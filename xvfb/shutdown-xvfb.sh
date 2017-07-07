#!/bin/sh
if [ -f "spid.txt" ]; then
	kill -9 $(cat spid.txt)
fi

pid=$( pgrep Xvfb)
kill -9 $pid

