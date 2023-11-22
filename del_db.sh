#!/bin/bash

if [ ! -f *.db ]
then
  echo ".db file was not found. Skipping..."
else
  rm *.db
  echo "removed all .db files."
fi
