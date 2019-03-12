# Dictionaries

# Using strings, lists, tuples and dictionaries concepts, find the reverse
# complement of AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA
read = "AAAAATCCCGAGGCGGCTATATAGGGCTCCGGAGGCGTAATATAAAA"
dict = {'C': 'G', 'G': 'C', 'A': 'T', 'T': 'A'}

complement = [dict[base] for base in read]
complement.reverse()
reverse_complement = ''.join(complement)

print(reverse_complement)
