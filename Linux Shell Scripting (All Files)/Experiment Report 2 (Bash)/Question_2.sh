# Write a Bash Script To Find GCD & LCM Of Two Numbers.

#!/bin/bash

echo -n "Please Enter The First Number : "
read first_number

echo -n "Please Enter The Second Number : "
read second_number

gcd() 
{
    a=$1
    b=$2
    while [ $b -ne 0 ]; do
        temp=$b
        b=$(( a % b ))
        a=$temp
    done
    echo $a
}

lcm() 
{
    a=$1
    b=$2
    gcd_value=$(gcd $a $b)
    lcm_value=$(( (a * b) / gcd_value ))
    echo $lcm_value
}

gcd_value=$(gcd $first_number $second_number)
lcm_value=$(lcm $first_number $second_number)

echo "GCD of $first_number and $second_number is: $gcd_value"
echo "LCM of $first_number and $second_number is: $lcm_value"