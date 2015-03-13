#!/bin/bash

sinkIndexes=($(pacmd list-sink-inputs | grep index | awk '/index/{print $NF}'))
if [ ! -z "{$sinkIndexes[0]}" ]; then
	pico2wave --lang "fr-FR" -w play.wav "$2" && aplay play.wav
fi
for i in "${sinkIndexes[@]}"; do
    pactl set-sink-input-volume -- $i $1
done
