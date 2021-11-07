from Bio import pairwise2

# Import format_alignment method
from Bio.pairwise2 import format_alignment


#Update values sections start

#Update family name of viurs to generate the filename appropriately.
virusFamily = "consolidated"

#Update sequences to generate pairwise alignment against that sequence.
seqs = [
"FGGDKNBB3BBBBBBBBBB**FFHGDDH*BDRHHRRDRDMBGBGBBGCOORRIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIDAIIDAI",
"FGGDKNFFBBHBFFDNEXBBBB9DHHBBGBB*GDDGFDDFFSSSSSSSSSSSSSSF2*6",
"FGGDKNBHBBBBB9DBHHBBGB3MBGB3***FFGDDBGDBIF8BHZ7QD26",
"FGGDKNBHHBBFHBBBBHGDDW*FFUMBGB5555555555555555555555555555555555555555555555555555555555555555555555",
"FGGDKNEBPBBBBB8C0DDGBBBVVBBHDEJNFGGDKNCCCBDBBBBEV*VB9DFBHFDBDDTFV4DI4DAAAHDDIYDADAHBNDMBAAAAAAAAAAAA",
"FGGDKNBBBBBBBBHHEFFFFFFFFFFFFHGDD*H*UUVFBB1FHBLVVDCEJN**LVDJN26FGGDKNBBEEEBBBBBBFEKEHHBBEBFFFEFFFFFF",
"FGGDKNB80DDGBBBBBHDEJNFGGDKNBBBBDBEB9DFBHFDBDDTF4DI4DHDDIYDDHBNDMBBGDDDHWW3BHDEBDBBBHBBBBBBBBBBBBBBB",
"FGGDKNVVBBHBBBBBBFFBBFDDH3HW*G36",
"FGGDKNHB80DDGBBBVBVBBHDEJNFGGDKNCCCBDBEV*VB9DFBHFDBDDTFV4DBBBI4DAAAHDDIYDADAHBNDMBAAAAAAAAAAAAAAAAAA",
"FGGDKNH8C0DDGBBBVVBFBBHFFBDEJNFGGDKNCCCBDBEV*VB9DFBHFDBDDTFV4DBBBI4DAAAHDDIYDADAHBNDMBAAAAAAAAAAAAAA"
]

#Update values sections end

def alignPairwise(seq1, seq2,fileName):
# Define two sequences to be aligned
# A match score is the score of identical chars, else mismatch score.
# Same open and extend gap penalties for both sequences.
    alignments = pairwise2.align.globalms(seq1, seq2, 10, -10, -5, -5)

# Use format_alignment method to format the alignments in the list
    for a in alignments:
     fileName.write(format_alignment(*a))
     break
 
count=0
seq1index=0
seq2index=0
pairwiseAlignFile = open("./scripts/results/pairwiseAlign_"+virusFamily+".txt","w")

for seq1 in seqs:
    seq1index=seq1index+1
    seq2index=0
    for seq2 in seqs:
        seq2index=seq2index+1
        if(seq1index >= seq2index):
            continue
        else:
            pairwiseAlignFile.write("\n"+str(seq1index-1)+","+str(seq2index-1)+"\n")
            alignPairwise(seq1,seq2,pairwiseAlignFile)
            count=count+1
        if(count==(len(seqs)*(len(seqs)-1))/2):
            break