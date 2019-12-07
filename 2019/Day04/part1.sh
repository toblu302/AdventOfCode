#!/bin/bash

fulfills_criteria () {
	local ok=1

	for i in {0..4}
	do
		if [ "${1:i:1}" -eq "${1:i+1:1}" ]; then
			ok=0
		fi
	done

	for i in {1..5}
	do
		if [ "${1:i:1}" -lt "${1:i-1:1}" ]; then
			ok=1
		fi
	done

	return $ok
}

result=0
for i in {246515..739105}
do
	if fulfills_criteria $i; then
		((result = result+1))
	fi
done
echo "$result"
