# Write a Bash Script To Rename All Files In a Directory By Adding a Prefix or Suffix.

#!/bin/bash

echo -n "Please Enter The Directory Path : "
read dir
 
if [ ! -d "$dir" ]; then
  echo "Invalid Directory."
  exit 1
fi
 
echo -n "Please Enter Prefix Or Suffix (p For Prefix, s For Suffix) : "
read choice
 
echo -n "Please Enter Text To Add As Prefix Or Suffix : "
read text
 
cd "$dir" || exit

for file in *; do
  if [ -f "$file" ]; then
    if [ "$choice" = "p" ]; then
      mv "$file" "$text$file"
    else
      mv "$file" "${file%}$text"
    fi
  fi
done

echo "Renaming Files Successfully Completed."