#!/usr/bin/bash

((a=1+6))
((b=a-1))
((c=a+b))

echo "a=${a}, b=${b}, c=${c}"

a=$((1+6))
b=$((a-1))
c=$((a+b))

((a=1+6,b=a-1,c=a+b))

echo "1+6=$((1+6))"

if ((a>7 && b==c))
then
	echo "a>7 && b==c True"
else
	echo "a>7 && b==c Flase"
fi

