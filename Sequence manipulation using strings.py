# Assign variables
dna = "AGCTCCGAG"
print(dna)
dna2 = "agtccta"
print(dna2)

# Convert DNA sequence to lower or upper case
dna_l = dna.lower()
print(dna_l)
dna_u = dna2.upper()
print(dna_u)

# Find the length of sequence
dnaX = "ACCGTTTAGGCTTATATATAGCCCCGATTTAGAGGATCCTAGAGCTATAGCTAGATCGATCGTAGCTAG"
dnaX_length = len(dnaX)
print(dnaX_length)

# Check for the presence or absence of characters / nucleotides
dna = "ATGCATGCGGTTAC"
if 'A' in dna:
    print("A is present in dna")
else:
    print("A is not present in dna")

# Count the number of nucleotides in a sequence
a_count = dnaX.count('A')
g_count = dnaX.count('G')
t_count = dnaX.count('T')
c_count = dnaX.count('C')
print(a_count)
print("The number of G =", g_count)

# Let's find the GC content of dnaX
# To calculate the GC content, we first count the occurrences of G and C
gc_count = dnaX.count('G') + dnaX.count('C')
# Now we calculate the GC content as a percentage
gc_content = (gc_count / dnaX_length) * 100
print("GC content is =", gc_content)

# Amazing job so far! Now let's combine strings/sequences
dna1 = "ATGC"
dna2 = "CGTA"
combined_sequences = dna1+dna2
print("The combined sequence is", combined_sequences)
# To give space between the combined sequence, do this:
combined_sequences = dna1 + ' ' + dna2
print("The spaced combined sequence is", combined_sequences)

# More string manipulations
# Function	        Action
# string.find('a')	Find the first position where 'a' occurs in the string
# string.count('s')	Counts how many 's' characters are in the string
# string.lower()	Copy of string with all characters converted to upper case
# string.upper()	Copy of string with all characters converted to upper case
# string.isdigit()	Checks if string contains only digits. Returns True or False
# string.isalpha()	Checks if string contains only alphabets. Returns True or False
# string.alnum()	Checks if the string contains alphanumeric characters only. Returns True or False
# string.strip()	Strips a character from both sides of the string
# string.split()	Splits the string into a list of substrings
# string.replace('s','t')	Replaces all 's' in the string with 't'
# string.join(list)	Joins all members of list into a single striing object
