# Write a Bash Script To Sort Multiple Numbers In Ascending Or Descending Order.

#!/bin/bash

echo -n "Enter Numbers Separated By Spaces : "
read -a numbers

echo "Choose Sorting Order : "
echo "(1) - Ascending"
echo "(2) - Descending"
read order

if [ $order -eq 1 ]; then
    for ((i = 0; i < ${#numbers[@]}; i++)); do
        for ((j = i + 1; j < ${#numbers[@]}; j++)); do
            if [ ${numbers[i]} -gt ${numbers[j]} ]; then
                temp=${numbers[i]}
                numbers[i]=${numbers[j]}
                numbers[j]=$temp
            fi
        done
    done
    echo "Numbers In Ascending Order Are : ${numbers[@]}"
elif [ $order -eq 2 ]; then
    for ((i = 0; i < ${#numbers[@]}; i++)); do
        for ((j = i + 1; j < ${#numbers[@]}; j++)); do
            if [ ${numbers[i]} -lt ${numbers[j]} ]; then
                temp=${numbers[i]}
                numbers[i]=${numbers[j]}
                numbers[j]=$temp
            fi
        done
    done
    echo "Numbers In Descending Order Are : ${numbers[@]}"
else
    echo "Invalid Option Selected."
fi