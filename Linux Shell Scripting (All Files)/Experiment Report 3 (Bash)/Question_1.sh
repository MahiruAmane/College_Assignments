# Write a Bash Script To Check For File Permissions (Read, Write & Execute).

#!/bin/bash

check_permissions() 
{
    local file=$1
    echo "Checking Permissions For File : $file"
    if [ -e "$file" ]; then
        if [ -r "$file" ]; then
            echo "Read Permission : Yes"
        else
            echo "Read Permission : No"
        fi

        if [ -w "$file" ]; then
            echo "Write Permission : Yes"
        else
            echo "Write Permission : No"
        fi

        if [ -x "$file" ]; then
            echo "Execute Permission : Yes"
        else
            echo "Execute Permission : No"
        fi
    else
        echo "File Does Not Exist."
    fi
}

echo -n "Please Enter The File Name : "
read file_name

check_permissions "$file_name"