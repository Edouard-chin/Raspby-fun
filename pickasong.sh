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

pico2wave --lang "fr-FR" -w play.wav "La chanson espagnole du jour" && aplay play.wav
declare -a args
count=0
for arg in "Mais laisser moi dabord baisser cette musique nulle"; do
  args[count]=$(printf '%q' "$arg")
  count=$((count+1))
done
ssh dudek@192.168.0.11 'bash -s' < volume.sh -- "-50%" "${args[@]}"
mpc -q clear
mpc -q findadd "any" "spanish"
mpc -q shuffle
mpc -q play 10
mpc -q crop
sleep 10
mpc idle
ssh dudek@192.168.0.11 'bash -s' < volume.sh -- "+50%" ""
exit
