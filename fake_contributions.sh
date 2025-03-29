#!/bin/bash

for i in {1..10}
do
    echo "Fake contribution $i" >> fake_file.txt
    git add fake_file.txt
    GIT_AUTHOR_DATE="2025-03-28T12:0${i}:00" GIT_COMMITTER_DATE="2025-03-28T12:0${i}:00" git commit -m "Backdated commit #$i"
done

git push origin main --force
