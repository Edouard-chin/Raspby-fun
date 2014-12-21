#!/bin/bash
#host="dudek@192.168.0.11"
#ssh $host 'PATH 0x1000'
aplay jingle.wav
pico2wave --lang $2 -w play.wav "$1" && aplay play.wav
#ssh $host 'PATH 0x10000'
