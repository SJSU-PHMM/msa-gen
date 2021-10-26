from Bio import pairwise2

# Import format_alignment method
from Bio.pairwise2 import format_alignment

# Define two sequences to be aligned
X = "FGGDKNBBHBBBBFFBBFHWDG"
Y= "FGGDKNBBHBBBBHWDG"

# Get a list of the global alignments between the two sequences FGGDKNBBHBBBBFFBBFHWDG and FGGDKNBBHBBBBHWDG satisfying the given scoring
# A match score is the score of identical chars, else mismatch score.
# Same open and extend gap penalties for both sequences.
alignments = pairwise2.align.globalms(X, Y, 10, -10, -5, -5)

# Use format_alignment method to format the alignments in the list
for a in alignments:
    print(format_alignment(*a))