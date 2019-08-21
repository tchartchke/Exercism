from textwrap import wrap

protein_map = {
  'AUG':'Methionine',
  'UUU':'Phenylalanine',
  'UUC':'Phenylalanine',
  'UUA':'Leucine',
  'UUG':'Leucine',
  'UCU':'Serine',
  'UCC':'Serine',
  'UCA':'Serine',
  'UCG':'Serine',
  'UAU':'Tyrosine',
  'UAC':'Tyrosine',
  'UGU':'Cysteine',
  'UGC':'Cysteine',
  'UGG':'Tryptophan',
  'UAA':'STOP',
  'UAG':'STOP',
  'UGA':'STOP'
}

def proteins(strand):
  seq = []
  if isinstance (strand, str):
    strand = wrap(strand, 3)
  for p in strand:
    if protein_map[p] == 'STOP':
      break
    seq.append(protein_map[p])
  return seq