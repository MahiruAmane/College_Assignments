# Write a Bash Script To Check Whether A Given Number Is An Armstrong Number Or Not.

#!/bin/bash

echo -n "Please Enter a Number : "
read number

sum=0
temp=$number

num_digits=${#number}
while [ $temp -gt 0 ]; do
    digit=$((temp % 10))
    sum=$((sum + digit ** num_digits))
    temp=$((temp / 10))
done

if [ $sum -eq $number ]; then
    echo "$number Is An Armstrong Number."
else
    echo "$number Is Not An Armstrong Number."
fi