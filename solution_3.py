# Задача
# Поменять местами аминокислоты:


pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


# def DNA_strand(dna):
#     return ''.join([pairs[x] for x in dna])
#
#
# print(DNA_strand('ATTGC'))
# print(DNA_strand('GTAT'))


def DNA_strand(dna):
    new = ''
    pair = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for i in range(len(dna)):
        new += pair[dna[i]]
    return new


print(DNA_strand('ATTGC'))
