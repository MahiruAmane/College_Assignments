# Write a Bash Script To Find Fibonacci Series Using Recursion.

#!/bin/bash

fibonacci() 
{
    if [ $1 -le 0 ]; then
        echo 0
    elif [ $1 -eq 1 ]; then
        echo 1
    else
        local prev1=$(fibonacci $(( $1 - 1 )))
        local prev2=$(fibonacci $(( $1 - 2 )))
        echo $(( prev1 + prev2 ))
    fi
}

echo -n "Please Enter The Number Of Terms In The Fibonacci Series : "
read number

echo -n "Fibonacci Series up to $number Terms : "

for (( i=0; i<number; i++ )); do
    fib_num=$(fibonacci $i)
    echo -n "$fib_num "
done
echo