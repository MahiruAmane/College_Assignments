# Write a Bash Script To Calculate Length Of a String.

#!/bin/bash

echo -n "Please Enter a String : "
read input_string

length=${#input_string}

echo "The Length Of The String Is : $length"