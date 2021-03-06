import re
# Let's return to our earlier exercise: calculating %GC content.
# In this exercise:
#   Write a function percentageGC that calculates the GC content of a DNA
#   sequence. The function should return the %GC content
#   The Function should return a message if the provided sequence is not DNA
#   (This should be checked by a different function, called by your function)

def not_dna(sequence):
    # Find a character that is not A, T, C or G
    non_base_regex = re.compile("[^ATCG]")
    return non_base_regex.search(sequence) ##Since you are re-using this, \
    #it should return True or False, may add position for message -2

def gc_content(sequence):
    if not_dna(sequence): ##CK the return is NoneType -1
        print("Not a DNA sequence")
        return; 
    read_length = len(sequence)
    GC_content = list(filter(lambda base: base == 'G' or base =='C', sequence))
    return len(GC_content)/read_length*100

trna="AAGGGCTTArGCTTAATTAAAGTGGCTGATTTGCGTTCAGTTGATGCAGAGTGGGGTTTTGCAGTCCTTA"
gc_percentage = gc_content(trna)
print("GC content is: %.4f" % gc_percentage) ## This makes and assumption that you will get a float as output
## Throws an error when a non-base is in your sequence -1

##CK: Your script fails when I add a none-base -1
## 