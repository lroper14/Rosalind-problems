# Rosalind problem 6
# Calculating Hamming Distance

def hamming(txt_file):
    distance = 0
    bases1 = []
    bases2 = []
    with open(txt_file, 'r') as file:
        content = file.read()
        lines = content.split('\n')
    for c in lines[0]:
        bases1.append(c)
    for c in lines[1]:
        bases2.append(c)
    for i in range(len(bases1)):
        if bases1[i] != bases2[i]:
            distance += 1

    print("Hamming distance: " + str(distance))

hamming('rosalind_hamm3.txt')