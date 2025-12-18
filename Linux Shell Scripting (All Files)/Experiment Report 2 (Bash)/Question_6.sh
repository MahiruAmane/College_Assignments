# Write a Bash Script To Count Lines, Words & Characters In A File.

#!/bin/bash

echo -n "Please Enter The File Name : "
read filename

if [ -f "$filename" ]; then
    lines=$(wc -l < "$filename")
    words=$(wc -w < "$filename")
    characters=$(wc -c < "$filename")
    echo "Lines: $lines"
    echo "Words: $words"
    echo "Characters: $characters"
else
    echo "File Does Not Exist."
fi