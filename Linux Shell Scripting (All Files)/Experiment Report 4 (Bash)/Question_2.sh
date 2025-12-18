# Write a Bash Script To Print The Reverse Of A Given String.

#!/bin/bash

echo -n "Please Enter a String : "
read input_string

reversed_string=$(echo "$input_string" | rev)

echo "Reversed String : $reversed_string"