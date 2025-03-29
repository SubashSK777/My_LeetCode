#!/bin/bash

for i in {1..6}
do
    export GIT_COMMITTER_DATE="2025-03-27T12:0${i}:00"
    export GIT_AUTHOR_DATE="2025-03-27T12:0${i}:00"

    echo "commit $i" > execute.txt
    git add execute.txt
    git commit -m "Restore streak - commit $i"
done

git push origin main  # Change 'main' if needed

# Clean up
rm execute.txt
