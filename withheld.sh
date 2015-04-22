#!/bin/bash

# Prints the total number of points being withheld
ls | grep -o "_[0-9]\+-WITHHELD" | cut -c2- | cut -d "-" -f 1 | paste -sd+ - | bc
