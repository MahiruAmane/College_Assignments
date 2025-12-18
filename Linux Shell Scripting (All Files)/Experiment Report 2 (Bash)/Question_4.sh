# Write a Bash Script To Check For File Existence, Create If Not Exists & Display Contents If Exists.

#!/bin/bash

echo -n "Please Enter The File Name : "
read filename

if [ -e "$filename" ]; then
    echo "File '$filename' Exists."
    echo "Displaying Contents Of The File : "
    cat "$filename"
else
    echo "File '$filename' Does Not Exist."
    echo "Creating File '$filename'..."
    touch "$filename"
    echo "File '$filename' Created Successfully."
fi