# Rosalind Problem 10
# Consensus and profile

def consensus(filename):
    global sequence
    with open(filename, 'r') as file:
        content = file.read()
        lines = content.split('\n')

    sequences = []
    sequence_line = []
    A, C, G, T = 0, 0, 0, 0
    aCount, cCount, gCount, tCount = [], [], [], []
    comparison_list = []


    # Combining the sequences into strings then adding them to sequences list
    for line in lines:
        if line and line[0] == '>':
            sequences.append(''.join(sequence_line))
            sequence_line = []
            continue
        else:
            sequence_line.append(line)
    for sequence in sequences:
        if sequence == '':
            sequences.remove(sequence)
    sequences.append(''.join(sequence_line))

    i = 0

    # Counting the number of each base at each position
    while i != len(sequence):
        for sequence in sequences:
            if sequence[i] == 'A':
                A += 1
            elif sequence[i] == 'C':
                C += 1
            elif sequence[i] == 'G':
                G += 1
            else:
                T += 1
            # Adding each count to a list
            if sequences.index(sequence) == len(sequences) - 1:
                aCount.append(A)
                cCount.append(C)
                gCount.append(G)
                tCount.append(T)
                i += 1
                A, C, G, T = 0, 0, 0, 0

    #Finding all the highest values in each of the counts
    counts = [aCount, cCount, gCount, tCount]
    pos_values = []
    highest_values = []
    i = 0
    while i != len(counts[0]):
        for count in counts:
            pos_values.append(count[i])
        max_value = max(pos_values)
        highest_values.append(max_value)
        pos_values = []
        i += 1

    # Getting the bases of the highest values
    consensus_base = []
    i = 0
    while i != len(highest_values):
        for value in highest_values:
            if aCount[i] == value:
                consensus_base.append('A')
            elif cCount[i] == value:
                consensus_base.append('C')
            elif gCount[i] == value:
                consensus_base.append('G')
            else:
                consensus_base.append('T')
            i += 1

    # Joining the consensus into a string
    consensus = ''.join(consensus_base)

    # Turning the list of counts into strings
    aCountStr = [str(i) for i in aCount]
    cCountStr = [str(i) for i in cCount]
    gCountStr = [str(i) for i in gCount]
    tCountStr = [str(i) for i in tCount]

    print(consensus)
    print('A: ' + ' '.join(aCountStr))
    print('C: ' + ' '.join(cCountStr))
    print('G: ' + ' '.join(gCountStr))
    print('T: ' + ' '.join(tCountStr))

consensus('rosalind_cons.txt')
