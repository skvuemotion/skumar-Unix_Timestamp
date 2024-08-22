#!/bin/bash

# Define the number of files to create
num_files=9

# Loop to create files
for i in $(seq 1 $num_files)
do
    touch "C3-01-171885131357$i-SN-171996697435$i-3F5AE472.MP4"
done

echo "$num_files .mp4 files created successfully."

