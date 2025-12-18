# Write a Bash Script To Check Voting Eligibility.

#!/bin/bash

echo -n "Please Enter Your Age : "
read age

if [ $age -ge 18 ]; then
    echo "You Are Eligible To Vote."
else
    echo "You Are Not Eligible To Vote."
fi