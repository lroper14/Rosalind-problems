# Rosalind problem 8
# Translating RNA to protein

codon_to_aa = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F', 'CUC': 'L',
               'AUC': 'I', 'GUC': 'V', 'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
               'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V', 'UCU': 'S', 'CCU': 'P',
               'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
               'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'UCG': 'S', 'CCG': 'P',
               'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
               'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'UAA': 'Stop', 'CAA': 'Q',
               'AAA': 'K', 'GAA': 'E', 'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
               'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R',
               'AGC': 'S', 'GGC': 'G', 'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
               'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}

def translate(filename):
    file = open(filename, 'r')
    seq = file.read()

    bases = [c for c in seq]
    amino_acids = []
    triplet = []
    i = 0
    for base in bases:
        triplet.append(base)
        i += 1
        if i == 3:
            print(triplet)
            triplet_string = ''.join(triplet)
            for codon in codon_to_aa:
                if triplet_string == codon:
                    aa = codon_to_aa.get(codon)
                    if aa == 'Stop':
                        break
                    amino_acids.append(aa)
                    i = 0
                    triplet = []



    final_aa_seq = ''.join(amino_acids)
    print(amino_acids)
    print(final_aa_seq)

translate('rosalind_prot.txt')