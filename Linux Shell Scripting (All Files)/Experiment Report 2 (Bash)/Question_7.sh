# Write a Bash Script To Compute Factorial Of A Number Using a Function.

#!/bin/bash

factorial() 
{
    if [ $1 -le 1 ]; then
        echo 1
    else
        local temp=$(( $1 - 1 ))
        local result=$(factorial $temp)
        echo $(( $1 * result ))
    fi
}

echo -n "Please Enter a Number To Compute It's Factorial : "
read number

if ! [[ "$number" =~ ^[0-9]+$ ]]; then
    echo "Please Enter a Valid Non Negative Integer."
    exit 1
fi

result=$(factorial $number)
echo "Factorial of $number Is : $result"