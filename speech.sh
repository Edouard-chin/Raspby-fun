#!/bin/bash
index=$(pacmd list-sink-inputs | grep index | awk '/index/{print $NF}')
pacmd set-sink-input-volume $index 0x1000
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols -volume 100 "http://translate.google.com/translate_tts?tl=$2&q=Alexander+you+have+one+niou+poule+requeste"; }
say $*
sleep 2
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols -volume 100 "http://translate.google.com/translate_tts?tl=fr&q=$1"; }
say $*
pacmd set-sink-input-volume $index 0x10000
