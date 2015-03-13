#!/bin/bash

# function adjustVolume {
# 	sinkIndexes=($(pacmd list-sink-inputs | grep index | awk '/index/{print $NF}'))
# 	if [ ! -z "{$sinkIndexes[0]}" ]; then
# 		pico2wave --lang "fr-FR" -w play.wav "$2" && aplay play.wav
# 	fi
# 	for i in "${sinkIndexes[@]}"; do
# 	    pactl set-sink-input-volume -- $i $1
# 	done
# }

ssh dudek@192.168.0.11 'bash -s' < volume.sh -- "-50%" "Salut les copains comment ca va"
mpc findadd "any" "spanish"
mpc shuffle
mpc play 10
mpc crop
while : ; do
    mpc idle
	ssh dudek@192.168.0.11 'bash -s' < volume.sh -- "+50%" "Ok je vous remets le son"
	exit
done
