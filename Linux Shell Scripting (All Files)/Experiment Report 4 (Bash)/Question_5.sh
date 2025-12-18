# Write a Bash Script To Check If a Given String Is a Palindrome Or Not.

#!/bin/bash

echo -n "Please Enter a String : "
read str

rev_str=$(echo "$str" | rev)
 
if [ "$str" = "$rev_str" ]; then
  echo "The Given String is a Palindrome."
else
  echo "The Given String is Not a Palindrome."
fi