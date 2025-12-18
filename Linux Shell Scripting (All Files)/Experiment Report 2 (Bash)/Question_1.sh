# Write a Bash Script To Check Whether A Given Number Is a Palindrome Or Not.

#!/bin/bash

echo -n "Please Enter a Number : "
read number

original_number=$number
reversed_number=0

while [ $number -gt 0 ]; do
    digit=$(( number % 10 ))
    reversed_number=$(( reversed_number * 10 + digit ))
    number=$(( number / 10 ))
done

if [ $original_number -eq $reversed_number ]; then
    echo "$original_number Is a Palindrome Number."
else
    echo "$original_number Is Not a Palindrome Number."
fi