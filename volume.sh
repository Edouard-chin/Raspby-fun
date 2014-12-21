#/bin/sh

index=$(pacmd list-sink-inputs | grep index | awk '/index/{print $NF}')
if ! [ -z "$index" ]; then
	pacmd set-sink-input-volume $index $1
fi
