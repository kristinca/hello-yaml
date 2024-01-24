#!/bin/bash

read -p "Enter your branch name: " branch_name
read -p "Enter number of commits: " number_of_commits
git reset HEAD~$number_of_commits
git commit -m "Undo last $number_of_commits commits"
git push --force origin $branch_name