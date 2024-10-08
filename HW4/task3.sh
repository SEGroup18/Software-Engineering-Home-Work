#!/bin/bash

# Task a: Extract passengers from 2nd class who embarked at Southampton.
# Task b: Replace male/female with M/F.
# Task c: Calculat e the average age of the filtered passengers.

cat titanic.csv | grep ".*,.*,2,.*,.*,.*,.*,.*,.*,.*,.*,S" | sed 's/female/F/g; s/male/M/g' | gawk -F, '
    BEGIN { sum=0; count=0 }
    $7 != "" { sum += $7; count++ }
    END { if (count > 0) print "Average Age: " sum/count; else print "No data" }
'
