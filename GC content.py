
def gc_content(txt_file):
    with open(txt_file, 'r') as file:
        content = file.read()
        lines = content.split('\n')
    gc_num = 0
    gc_percent_list = []
    id = []
    sequence_length = 0
    for item in lines:
        if item and item[0] == '>': # Adding the Rosalind ID to the id list
            if sequence_length > 0:
                gc_percent = (gc_num / sequence_length) * 100
                gc_percent_list.append(gc_percent)
            id.append(item)
            gc_num = 0
            sequence_length = 0
        else:
            for c in item:
                sequence_length += 1 # Totalling the sequence length
                if c == 'G' or c == 'C': # Counting how many GCs are in that sequence
                    gc_num += 1
                else:
                    continue
    gc_percent = (gc_num / sequence_length) * 100
    gc_percent_list.append(gc_percent) # Need to do it one more time for the final string

    id_gc = {id[i]: gc_percent_list[i] for i in range(len(id))} # Creates dictionary of id: GC percent
    max_percent = max(id_gc.values()) # Finds max percent
    max_percent_id = max(id_gc, key=id_gc.get) # ID associated with max_percent

    print('The highest GC content is ' + max_percent_id + ': ' + str(max_percent))

gc_content('rosalind_gc2.txt')