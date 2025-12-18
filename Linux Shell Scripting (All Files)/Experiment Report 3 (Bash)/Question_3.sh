# Write a Bash Script To Search For a Pattern In a File.

#!/bin/bash

echo -n "Please Enter The File Name : " 
read filename


if [ ! -e "$filename" ]; then 
  echo "File Does Not Exist." 
  exit 1 
fi 
 
echo -n "Enter Pattern To Search For : " 
read pattern 
 
echo "Lines Matching Pattern Are As Follows : " 
grep "$pattern" "$filename"