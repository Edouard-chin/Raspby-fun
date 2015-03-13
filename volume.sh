#!/bin/bash

say() {
	local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?tl=en&q=$1";
}

sinkIndexes=($(pacmd list-sink-inputs | grep index | awk '/index/{print $NF}'))
if [ ! -z "{$sinkIndexes[0]}" ]; then
	say "$2"
fi
for i in "${sinkIndexes[@]}"; do
    pactl set-sink-input-volume -- $i $1
done
