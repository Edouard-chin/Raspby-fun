#!/bin/bash
index=$(pacmd list-sink-inputs | grep index | awk '/index/{print $NF}')
if ! [ -z "$index" ]; then
	#pacmd set-sink-input-volume $index 0x1000
	sleep 10
fi
aplay jingle.wav
pico2wave --lang $2 -w play.wav "$1" && aplay play.wav
# if ! [ -z "$index" ]; then
# 	pacmd set-sink-input-volume $index 0x10000
# fi
