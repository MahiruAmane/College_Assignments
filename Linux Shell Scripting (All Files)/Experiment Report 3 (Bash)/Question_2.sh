# Write a Bash Script To Perform String Operations (Concatenation, Length & Comparison).

#!/bin/bash

concatenate_strings() 
{
    local str1="$1"
    local str2="$2"
    echo "Concatenated String : ${str1}${str2}"
}

string_length() 
{
    local str="$1"
    echo "Length of String : ${#str}"
}

compare_strings()
{
    local str1="$1"
    local str2="$2"
    if [ "$str1" == "$str2" ]; then
        echo "The Two Strings Are Equal."
    else
        echo "The Two Strings Are Not Equal."
    fi
}   

echo -n "Please Enter The First String : "
read string1

echo -n "Please Enter The Second String : "
read string2

concatenate_strings "$string1" "$string2"
string_length "$string1"
string_length "$string2"
compare_strings "$string1" "$string2"