#!/bin/bash

echosleep() {
    local TIME="$1" 
    sleep "$TIME" 
    echo "$TIME"
}

while [ -n "$1" ]
do
    echosleep "$1" &
    shift
done
wait
