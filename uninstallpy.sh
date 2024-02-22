#!/bin/bash

read -p "Enter your requirements txt file name: " req_txt

if [ ! -f "$req_txt" ]; then
    echo "File not found!"
    exit 1
fi

# asking which libs to keep
echo "Enter the libraries to keep installed (separated by space, press ENTER if none/done):"
read -a keep_libs

# pip ---> in the keep list
keep_libs+=("pip")

# check if an item is in the keep list
containsElement () {
  local e match="$1"
  shift
  for e; do [[ "$e" == "$match" ]] && return 0; done
  return 1
}

start_time=$(date +%s%3N)

# iterating each line in the requirements txt file
while IFS= read -r line; do
    # get library name
    lib_name=$(echo "$line" | cut -d'=' -f1)
    
    # check if the library is in the keep list
    if containsElement "$lib_name" "${keep_libs[@]}"; then
        echo "$lib_name is kept installed."
    else
        echo "Uninstalling $lib_name..."
        pip uninstall -y "$lib_name"
        if [ $? -eq 0 ]; then
            echo "Uninstalled $lib_name."
        else
            echo "Failed to uninstall $lib_name."
        fi
    fi
done < "$req_txt"

end_time=$(date +%s%3N)
time_diff=$((end_time - start_time))
echo "Time taken to uninstall libraries: $time_diff milliseconds"
