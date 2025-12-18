# Write a Bash Script To Find Fibonacci Series Using Loop.

#!/bin/bash

echo -n "Please Enter The Number Of Terms You Want In The Fibonacci Series : "
read number

a=0
b=1

echo -n "Fibonacci Series Upto $number Terms : "
for (( i=0; i<number; i++ )); do
    echo -n "$a "
    fn=$((a + b))
    a=$b
    b=$fn
done
echo