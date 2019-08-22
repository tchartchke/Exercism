def slices(series, length):
  series = str(series)
  if len(series) < length:
    raise ValueError("string not long enough")
  if length < 1:
    raise ValueError("not valid length")

  print(series)
  print(type(series))
  print(len(series))
  strings = []
  i = 0
  while i+length <= len(series):
    print(i+length)
    strings.append(series[i:i+length])
    print(series[i:i+length])
    i+=1

  return strings