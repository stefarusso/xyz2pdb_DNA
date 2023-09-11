#!/bin/bash
TRAJECTORY=$1
N_MOL=240
N_PRELINE=2


#Strip the trajectory 1:100

mkdir splitted
cd splitted
gsplit -a 10 -d -l $(( $N_MOL + $N_PRELINE )) ../$TRAJECTORY
for i in $(ls | sort)
do
VAR=$( echo $i | sed 's/x//g'| sed 's/^0*//g')
if [[ ! $((VAR % 100)) -eq 0 ]]
then
printf "x%010d" $VAR | xargs rm
fi
done

#xyz to PDB conversion
for i in $(ls)
do 
python3 ../xyz2pdb.py $i
rm $i
cat ../curve.sh | sed "s/FILENAME/$i/g" > curve.sh
./curve.sh
done


