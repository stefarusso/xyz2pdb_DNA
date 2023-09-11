#!/bin/bash
#DNA
N_BIOMOL=378
#ARC file
N_PRE_LINES=2

#BOX
N_TOT_MOL=378

TRAJECTORY=$1

echo "INDICI DA ELIMINARE PER IL SOLVENTE"
head -n $(($N_TOT_MOL + N_PRE_LINES)) $TRAJECTORY | tail -n $(( N_TOT_MOL - N_BIOMOL - N_PRE_LINES )) | awk '{print $6" "}' | sort | uniq | tr -d '\n'
echo ""
echo "INDICI DA ELIMINARE PER GLI IDROGENI"
head -n $(($N_BIOMOL + N_PRE_LINES)) $TRAJECTORY | tail -n $(( N_BIOMOL )) | grep H | awk '{print $6}' | sort | uniq | awk '{$1=$1}1' RS= OFS=' '

