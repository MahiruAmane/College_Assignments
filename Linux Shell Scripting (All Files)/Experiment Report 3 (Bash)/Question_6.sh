# Write a Bash Script To Search For Files In a Given Directory And Its Sub Directories.

#!/bin/bash

echo -n "Please Enter The Directory Path : "
read dir
 
echo -n "Please Enter The File Extension : "
read ext
 
echo -n "Please Enter The Minimum File Size In Bytes (0 For No Restriction) : "
read size
 
if [ ! -d "$dir" ]; then           
  echo "Invalid Directory."
  exit 1
fi
 
if [ "$size" -gt 0 ]; then
  find "$dir" -type f -name "*.$ext" -size +"$size"c
else
  find "$dir" -type f -name "*.$ext"
fi