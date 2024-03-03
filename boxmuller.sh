#!/bin/bash

echo "Enter the number of numbers to generate:"
read count
echo "Enter the length of each number:"
read length

start=$(date +%s%N)

generate_number() {
  numDigitsGenerated=0
  while [ $numDigitsGenerated -lt $length ]; do
    if [ $(($length - $numDigitsGenerated)) -eq 1 ]; then
      # 1 digit
      awk -v seed=$RANDOM 'BEGIN {
        srand(seed);
        u1 = rand();
        z0 = sqrt(-2 * log(u1)) * cos(2 * atan2(0, -1) * u1);
        z0 = int(((z0 / 3) + 1) * 4.5);
        if (z0 < 0) z0 = 0; else if (z0 > 9) z0 = 9;
        printf "%d", z0;
      }'
      let numDigitsGenerated+=1
    else
      # two digits
      awk -v seed=$RANDOM 'BEGIN {
        srand(seed);
        u1 = rand();
        u2 = rand();
        z0 = sqrt(-2 * log(u1)) * cos(2 * atan2(0, -1) * u2);
        z1 = sqrt(-2 * log(u1)) * sin(2 * atan2(0, -1) * u2);
        z0 = int(((z0 / 3) + 1) * 4.5);
        z1 = int(((z1 / 3) + 1) * 4.5);
        if (z0 < 0) z0 = 0; else if (z0 > 9) z0 = 9;
        if (z1 < 0) z1 = 0; else if (z1 > 9) z1 = 9;
        printf "%d%d", z0, z1;
      }'
      let numDigitsGenerated+=2
    fi
  done
  echo
}

totalDigits=$((count * length))
for ((j=0; j<count; j++)); do
  generate_number
done

end=$(date +%s%N)
elapsed=$((end - start))
total_ms=$((elapsed / 1000000))

echo "Time taken to generate ${totalDigits} normally distributed digits in $count numbers from uniformly distributed random numbers: $total_ms milliseconds"