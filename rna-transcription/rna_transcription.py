def to_rna(dna_strand):
    list_of_char = []
    list_of_char = dna_strand
    for i in list_of_char:
        if i not in ('C','G','T','A'):
            raise ValueError("Invalid nucliotide")
    trans = str.maketrans('GCTA', 'CGAU')
    newString = (dna_strand.translate(trans))
    return newString



