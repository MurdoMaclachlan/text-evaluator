  cprint('PROGRAM VERSION 3.0 CURRENTLY IN DEVELOPMENT. WILL LIKELY NOT WORK.','red')
  cprint('LETTER EVALUATOR','yellow')
  cprint('Do you wish to, 1: Calculate a value, or 2: Search for an already calculated value?','magenta')
  x = input("\n >> ")
  x = int(validate(x,"either 1 or 2.",1,2))
  if x == 1:
    replit.clear()
    calculate()
  elif x == 2:
    replit.clear()
    readFile(str(input("Please input the text to search for: \n >> ")), 1)
