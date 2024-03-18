# Rosalind problem finding a protein motif
# Specificially N-glycosylation motif N{P}[ST]{P}
# Program finds all the positions in an amino acid sequence that has the
# N-glycosylation motif N{P}[ST]{P}

import requests

# Obtaining all the sequences that correspond to the uniprot codes
def fetch_protein_sequences(filename):
    with open(filename, 'r') as file:
        content = file.read()
        lines = content.split('\n')

    # Split the string to just obtain the code, everything after first '_'
    # doesn't work as a uniprot code
    uniprot_ids = []
    for id in lines:
        if '_' in id:
            temp_list = id.split('_')
            uniprot_ids.append(temp_list[0])
        elif id == '':
            break
        else:
            uniprot_ids.append(id)

    sequences = {}
    base_url = "https://www.ebi.ac.uk/proteins/api/proteins/{}"

    for uniprot_id in uniprot_ids:
        url = base_url.format(uniprot_id)
        response = requests.get(url, headers={"Accept": "application/json"})

        if response.ok:
            data = response.json()
            sequence = data.get("sequence", {}).get("sequence")
            sequences[uniprot_id] = sequence
        else:
            print(f"Failed to fetch sequence for {uniprot_id}")

    return sequences

sequences = fetch_protein_sequences('rosalind_mprt.txt')

def protein_motif(sequences, filename):

    #Obtain the IDs for printing later
    with open(filename, 'r') as file:
        content = file.read()
        lines = content.split('\n')

    sequences_letters = []

    # Splits the sequences up into individual letters in a list
    # maybe unnecessary?
    for sequence in sequences.values():
        temp_list = [char for char in sequence]
        sequences_letters.append(temp_list)
        temp_list = []

    # Finding the motif
    temp_list2 = []
    indexes = []
    for sequence in sequences_letters:
        for x, element in enumerate(sequence):
            if x == len(sequence)-3: # Break when at 3rd from last index
                break
            elif (element == 'N' and sequence[x+1] != 'P'
                and (sequence[x+2] == 'S' or sequence[x+2] == 'T')
                and sequence[x+3] != 'P'):
                    temp_list2.append(x+1) # This is the bit that finds N{P}[ST]{P}
        indexes.append(temp_list2) # Appends the list to the indexes list
        temp_list2 = []

    # Printing the Uniprot IDs and the aa sequence position
    for x, line in enumerate(lines):
        if x == len(sequences):
            break
        index_string = indexes[x]
        if index_string == []:
            continue
        else:
            print(line)
            print(' '.join([str(elem) for elem in index_string ]))

protein_motif(sequences, 'rosalind_mprt.txt')

