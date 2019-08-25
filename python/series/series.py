def slices(series, length):
  series = str(series)
  if len(series) < length:
    raise ValueError("string not long enough")
  if length < 1:
    raise ValueError("not valid length")

  strings = []
  i = 0
  
  for i in range(0, len(series)-length+1):
    strings.append(series[i:i+length])

  return strings