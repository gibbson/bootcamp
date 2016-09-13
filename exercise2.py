import bioinfo_dicts

def gc_blocks(seq, block_size):
    """Divides a sequence into blocks and computes the GC content for each block"""

    l = len(seq)

    # Initialize list of open parens and list of base pairs
    bps = []

    i = 0
    while i+block_size<l:
        seq_temp = seq[i:i+block_size]
        num = 0
        for base in seq_temp:
            if base in 'GgCc':
                num += 1
        bps.append(num/block_size)
        i += block_size

    return tuple(bps)


def gc_map(seq, block_size, gc_thresh):
    """Get GC threshold and make uppercase and lowercase"""

    block_value = gc_blocks(seq, block_size)
    l = len(block_value)

    tempstr = ''

    for i in range(l):
        if block_value[i] < gc_thresh:
            tempstr += seq[i * block_size:(i + 1) * block_size].lower()
        else:
             tempstr += seq[i * block_size:(i + 1) * block_size].upper()

    return tempstr

def longest_orf(seq):
    """Find the longest ORF"""

    l = len(seq)
    longest_num = 0
    longest_left = 0
    longest_right = 0
    for i in range(l):
        if seq[i:i+3] == 'ATG':
            k = i+3
            is_find = False
            while k+3 < l:
                if seq[k:k+3] in 'TGA TAG TAA':
                    is_find = True
                    num = k+3-i
                    break
                k += 3

            if is_find and num > longest_num:
                     longest_num = num
                     longest_left = i
                     longest_right = k+3

    return seq[longest_left:longest_right]

def orf(seq):
    """Find the longest ORF"""

    l = len(seq)
    longest_num = 0
    longest_left = 0
    longest_right = 0
    bps = []
    orf_length = []

    # Find all orfs
    for i in range(l):
        if seq[i:i+3] == 'ATG':
            k = i+3
            is_find = False
            while k+3 < l:
                if seq[k:k+3] in 'TGA TAG TAA':
                    is_find = True
                    num = k+3-i
                    break
                k += 3

            if is_find and num > longest_num:
                    orf_left = i
                    orf_right = k+3
                    bps.append((orf_left, orf_right))

    # Select 5 longest orf
    for orff in bps:
        orf_length.append(orff[1]-orff[0])

    orf_length_sort = sorted(orf_length)

    orf_length_sort_reverse = orf_length_sort[::-1]

    orf_seq = []
    for j in range(5):
        a = 0
        while bps[a][1]-bps[a][0] != orf_length_sort_reverse[j]:
            a += 1
        orf_seq.append((seq[bps[a][0]:bps[a][1]]))

    return orf_seq

def dnatoaa(seq):
    # Transfer DNA sequence to aa sequence
    aaseq = ''
    for i in range(int(len(seq)/3)):
        aaseq += (bioinfo_dicts.codons[seq[i * 3:(i + 1) * 3]])

    return aaseq
