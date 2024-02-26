file = open('rosalind_rna.txt', 'r')
sequence = file.read()

RNA = []

for c in sequence:
    if c == 'T':
        RNA.append('U')
    else:
        RNA.append(c)

rna_sequence = ''.join(RNA)

print(rna_sequence)