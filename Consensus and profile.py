# Rosalind Problem 10
# Consensus and profile

def consensus(filename):
    with open(filename, 'r') as file:
        content = file.read()
        lines = content.split('\n')

    sequences = []
    temp_sequences = []
    for line in lines:
        if line and line[0] == '>':
            print(temp_sequences)
            sequences.append(''.join(temp_sequences))
            if len(temp_sequences) > 0:
                temp_sequences = []
        else:
            sequences.append(line)

    matrix = [[0] * len(sequences[0]) for _ in range(4)]


    print(sequences)


consensus('rosalind_cons2.txt')
