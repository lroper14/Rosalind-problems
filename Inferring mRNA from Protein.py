# Rosalind problem: Inferring mRNA from Protein
# This tells you all the mRNA combinations for a given amino acid sequence modulo 1000000

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

def mRNA_from_protein(txt_file):

    # Open the file, split lines into list
    with open(txt_file, 'r') as file:
        content = file.read()
        lines = content.split('\n')

    # Create a list of each amino acid
    sequence_str = ''.join(lines)
    sequence = [x for x in sequence_str]

    # Convert the dictionary values into a list of the dictionary values
    list_values = list(codon_to_aa.values())

    combinations = list_values.count(sequence[0]) #Initialise combinations with first aa

    # Calculate the number of combinations
    for x, element in enumerate(sequence):
        if x == 0: # This is just to skip the first aa since it's been done
            continue
        else:
            combinations = combinations * list_values.count(sequence[x])

    combinations = combinations * 3 # Accounting for the stop codons

    print(combinations % 1000000)

mRNA_from_protein('rosalind_mrna.txt')