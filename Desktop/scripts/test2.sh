#!/bin/bash

count=10

if [ $count -eq 10 ]
then
	echo  "the numberr is 10"

elif (( $count <= 9 )) && [ $count >29 ]
then
	echo "the number is lower than 9"
else
	echo "the number is not 10"
fi
