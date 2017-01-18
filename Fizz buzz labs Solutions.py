Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def fizz_buzz(number):
  
  if number%15 == 0: 
    return "FizzBuzz"

  elif number%3==0:
    return "Fizz"

  elif number%5==0:
    return "Buzz"

  else:
    return number
