# Write a Bash Script To Check Whether A Number Is Prime Or Not.

#!/bin/bash

echo -n "Please Enter A Number : "
read number

is_prime=1

if [ $number -le 1 ]; then
    is_prime=0
else
    for (( i=2; i*i<=number; i++ )); do
        if [ $((number % i)) -eq 0 ]; then
            is_prime=0
            break
        fi
    done
fi

if [ $is_prime -eq 1 ]; then
    echo "$number Is a Prime Number."
else
    echo "$number Is Not a Prime Number."
fi