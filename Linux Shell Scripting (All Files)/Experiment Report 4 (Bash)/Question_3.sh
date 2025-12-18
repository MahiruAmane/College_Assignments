# Write a Bash Script To Concatenate Two Strings.

#!/bin/bash

echo -n "Please Enter The First String : "
read first_string

echo -n "Please Enter The Second String : "
read second_string

concatenated_string="$first_string$second_string"

echo "Concatenated String Is : $concatenated_string"