# Rosalind problem - overlap graphs

def overlap_graphs(txt_file):
    with open(txt_file, 'r') as file:
        content = file.read()
        lines = content.split('\n')

    rosalind_id = []
    unjoined_sequences = []
    sequences = []
    iddict_list = []
    firstThreeLetters = []
    lastThreeSeqLetters = []

    # Adding the rosalind IDs and the sequences to seperate lists
    for line in lines:
        if line and line[0] == '>':
            rosalind_id.append(line[1:])
        else:
            unjoined_sequences.append(line)

    # Joining the sequence lines so that the indexes match the id because right now sequences are on
    # seperate lines
    for i in range(0, len(unjoined_sequences), 2):
        if unjoined_sequences[i] == '':
            break
        sequences.append(unjoined_sequences[i] + unjoined_sequences[i + 1])

    # Simplifying this a lot by just adding the last three letters and first three letters
    # to a list
    for sequence in sequences:
        lastThreeSeqLetters.append(sequence[-3:])

    for sequence in sequences:
        firstThreeLetters.append(sequence[:3])

    i = 0

    while i != len(lastThreeSeqLetters):
        letterCheck = lastThreeSeqLetters[i]
        for a in range(0, len(lastThreeSeqLetters)):
            if letterCheck == firstThreeLetters[a]:
                iddict_list.append(rosalind_id[i])
                iddict_list.append(rosalind_id[a])
        i += 1

    for j in range(0, len(iddict_list), 2):
        if iddict_list[j] != iddict_list[j+1]:
            print(iddict_list[j] + ' ' + iddict_list[j+1])


overlap_graphs('rosalind_grph.txt')
