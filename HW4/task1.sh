#!/bin/bash

# get the process ID of the infinite.sh process
process_id=$(pgrep -f infinite.sh)

# If the process ID is found, terminate the process
if [ -n "$process_id" ]; then
    kill "$process_id"
    echo "Terminated infinite.sh (PID: $process_id)."
else
    echo "No running instance of infinite.sh was found."
fi
