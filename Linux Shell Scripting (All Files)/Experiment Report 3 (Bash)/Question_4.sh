# Write a Bash Script To Display System Information.

#!/bin/bash

echo "Host Name : $(hostname)"
echo "Operating System : $(uname -o)"
echo "Kernel Version : $(uname -r)"
echo "Uptime : $(uptime -p)"
echo "Current Users : $(who | wc -l)"
echo "Report Generated On : $(date)"
