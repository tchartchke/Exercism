def is_armstrong_number(number):
    num_string = str(number)
    digits = len(num_string)
    sum=0

    for i in range(digits):
      sum += int(num_string[i])**digits

    return sum == number