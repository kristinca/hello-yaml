#!/bin/bash

if [ "$(find .. -maxdepth 1 -type f -name '*.py' | wc -l)" -gt 0 ]
then
  find .. -maxdepth 1 -type f -name '*.py' -exec mv {} . \;
  echo "Files moved successfully."
else
  echo "No .py files found in the upper directory. Skipping..."
fi