#!/bin/bash

if [ -n "$VIRTUAL_ENV" ]; then
  "deactivate"
  echo "Venv deactivated."
else
  source "./venv/Scripts/activate"
  echo "Venv activated."
fi
