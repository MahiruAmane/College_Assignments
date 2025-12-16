# Write a Bash Script To Perform Basic Arithmetic Operations.

#!/bin/bash

echo -n "Please Enter The First Number : "
read num1

echo -n "Please Enter The Second Number : "
read num2

echo "Select The Arithmetic Operation You Want To Perform : "
echo "(1) - Addition"
echo "(2) - Subtraction"
echo "(3) - Multiplication"
echo "(4) - Division"
echo -n "Please Enter Your Choice (1 To 4) : "
read choice

case $choice in
    1)
        result=$(($num1 + $num2))
        echo "The Sum Of $num1 And $num2 Is : $result"
        ;;
    2)
        result=$(($num1 - $num2))
        echo "The Difference Between $num1 And $num2 Is : $result"
        ;;
    3)
        result=$(($num1 * $num2))
        echo "The Product Of $num1 And $num2 Is : $result"
        ;;
    4)
        if [ $num2 -ne 0 ]; then
            result=$(($num1 / $num2))
            echo "The Quotient When $num1 Is Divided By $num2 Is : $result"
        else
            echo "Division By Zero Is Not Allowed."
        fi
        ;;
    *)
        echo "Invalid Choice! Please Select A Valid Option (1 To 4)."
        ;;
esac