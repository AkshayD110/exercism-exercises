import re
def to_rna(dna_strand):
    rna_list = []
    dna_to_rna = {'G':'C',
                  'C':'G',
                  'T':'A',
                  'A':'U'
                  }
    for n in dna_strand:
        try:
            rna_list.append(dna_to_rna[n])
        except:
            raise ValueError("No such nucleotide")
    print(''.join(rna_list))
    return ''.join(rna_list)