def to_rna(dna_strand):
    check_strand=dna_strand
    check_strand.replace('A','U')
    check_strand.replace('C','G')
    check_strand.replace('G','C')
    check_strand.replace('T','A')
    return check_strand