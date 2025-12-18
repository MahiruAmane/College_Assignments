# Write a Bash Script To Split a Sentence Into Words.

#!/bin/bash

echo -n "Please Enter a Sentence : "
read sentence

for word in $sentence; do
    echo $word
done