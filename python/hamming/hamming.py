def distance(strand_a, strand_b):
  if len(strand_b) != len(strand_a):
    raise ValueError("unequal lengths")

  ham_err = 0

  for i in range(len(strand_b)):
    if strand_a[i] != strand_b[i]:
      ham_err += 1

  return ham_err
