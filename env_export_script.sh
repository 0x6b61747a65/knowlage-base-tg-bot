#!/bin/bash

# export script for list of needed env variables

if [ "$1" ]
then
    for line in $(cat $1)
    do 
        export $line
    done
else
    echo 'There were no file supported to script'
fi
