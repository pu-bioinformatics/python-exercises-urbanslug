# Working with strings

def at_gc_content(sequence):
    read_length = len(sequence)
    AT_content = list(filter(lambda base: base == 'A' or base =='T', sequence))
    GC_content = list(filter(lambda base: base == 'G' or base =='C', sequence))

    GC_percentage = len(GC_content)/read_length*100
    AT_percentage = len(AT_content)/read_length*100
    print("AT percentage is: %.4f" % AT_percentage)
    print("GC percentage is: %.4f" % GC_percentage)

def amino_sequence_finder(sequence, indices):
    for index in indices:
        print("%dth base is: %s" % (index, sequence[index]))

# Calculate the % GC and % AT content in the trna sequence
trna="AAGGGCTTAGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA"
at_gc_content(trna)

# Given the following amino acid sequence (MNKMDLVADVAEKTDLSKAKATEVIDAVFA),
# find the first, last and the 5th amino acids in the sequence.
amino_acid_sequence = "MNKMDLVADVAEKTDLSKAKATEVIDAVFA"
amino_sequence_finder(amino_acid_sequence, [0, 4, -1])

# The above amino acid is a bacterial restriction enzyme that recognizes
# "TCCGGA". Find the first restriction site in the following sequence:
# AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA
dna = "AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"
kmer="TCCGGA"
print("Index of first %s is: %d" % (kmer, dna.find(kmer)))
