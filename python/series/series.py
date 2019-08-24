def slices(series, length):
  series = str(series)
  if len(series) < length:
    raise ValueError("string not long enough")
  if length < 1:
    raise ValueError("not valid length")

  strings = []
  i = 0
  while i+length <= len(series):
    strings.append(series[i:i+length])
    i+=1

  return strings


  # for loop len(series)-length for range