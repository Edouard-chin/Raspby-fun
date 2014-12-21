#!/bin/bash
index=$(pacmd list-sink-inputs | grep index | awk '/index/{print $NF}')
if ! [ -z "$index" ]; then
	pacmd set-sink-input-volume $index 0x1000
fi
pico2wave -w lookdave.wav "$*" && aplay lookdave.wav
echo 'good'
if ! [ -z "$index" ]; then
	pacmd set-sink-input-volume $index 0x10000
fi
