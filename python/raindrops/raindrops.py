def convert(number):
    rainSound = ""
    
    if number%3==0:
      rainSound += "Pling"
    if number%5==0:
      rainSound += "Plang"
    if number%7==0:
      rainSound += "Plong"
    if rainSound == "":
      return str(number)
    
    return rainSound

