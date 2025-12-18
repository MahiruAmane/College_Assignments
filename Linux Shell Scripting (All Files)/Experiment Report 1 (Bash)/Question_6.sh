# Write a Bash Script To Find Sum Of Digits In A Given Number.

#!/bin/bash

echo -n "Please Enter a Number : "
read number

sum=0

while [ $number -gt 0 ]; do
    digit=$((number % 10))
    sum=$((sum + digit))
    number=$((number / 10))
done

echo "The Sum Of The Digits Is : $sum"