def to_rna(dna_strand):
  table = dna_strand.maketrans('GCTA', 'CGAU')
  return dna_strand.translate(table)