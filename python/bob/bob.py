def response(hey_bob):
  heybob = hey_bob.translate( { ord(c):None for c in ' \n\t\r' })
  if heybob == '':
    return 'Fine. Be that way!'
  if heybob[len(heybob)-1] == '?' and heybob.isupper():
    return "Calm down, I know what I'm doing!"
  if heybob.isupper():
    return "Whoa, chill out!"
  if heybob[len(heybob)-1] == '?':
    return "Sure."
  return "Whatever."
