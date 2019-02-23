'''
  I originally wrote this program in Python 2.7, on an older account which I no longer use. I like the program though, so I ported it to Python 3 and brought it to this account. Enjoy.

  Development for version 3.0 has begun. Coming soon.
'''

from termcolor import cprint
import replit
import time

#variables
letterCount = 0
totalCount = {}
letterValue = {'A':3, 'B':20, 'C':13, 'D':10, 'E':1, 'F':12, 'G':16, 'H':9, 'I':7, 'J':23, 'K':22, 'L':11, 'M':14, 'N':5, 'O':4, 'P':18, 'Q':25, 'R':6, 'S':8, 'T':2, 'U':15, 'V':21, 'W':19, 'X':24, 'Y':17, 'Z':26}
values = []
#variables

#functions
def letterCounter(string, letterValue):
  letterCount = 0.0
  totalLetterValue = 0.0
  histogram = {}
  for i in list(string):
    if i.isalpha():
      i = i.upper()
      letterCount += 1
      totalLetterValue += letterValue[i]
      if i in histogram:
        histogram[i]+=1
      else:
        histogram[i]=1
  textValue = totalLetterValue/letterCount
  return histogram, letterCount, totalLetterValue, textValue

#functions
def writeFile(text, value):
  file = open("pastTexts.txt","at")
  file.write(text+": "+value+"\n")
  file.close()
#functions

def calculate():
  cprint('LETTER EVALUATOR','yellow')
  cprint('HOW TO USE','cyan')
  cprint('Input the text you want to be evaluated, then press enter.','magenta')
  cprint('The value of the text is determined by dividing the total letter value by the number of letters. The rarer the letter is in the English language, the higher its value.','magenta')
  cprint('This evaluator records all text it evaluates, and its value.','magenta')
  string = str(input("\nInput text\n >> "))
  print ("\nWorking, please wait...")
  values = readFile(string, 0)
  if values == "nil":
    values = []
    values.append(letterCounter(string, letterValue))
    print("\n\nHistogram: ", values[0][0])
    print("\nLetter Count: ", values[0][1])
    print("\nTotal Letter Value: ", values[0][2])
    print("\nText Value: ", values[0][3])
    writeFile(string, str(values[0][3]))
  time.sleep(0.5)
  returnToMain()

def readFile(string, fromRead):
  found = False
  file = open('pastTexts.txt','r')
  y = file.read().splitlines()
  for line in y:
    if ''.join(filter(str.isalpha, string)) == ''.join(filter(str.isalpha, line)):
      print("\n } "+line)
      found = True
  if found != True:
    if fromRead == 1:
      print("Failed to find.")
      returnToMain()
    elif fromRead == 0:
      return "nil"
  file.close()
  returnToMain()

def mainMenu():
  cprint('Version 2.3.2.1','red')
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

def validate(x,extender,numOne,numTwo):
  if any(c.isalpha() for c in x) == True:
    x = subValidate(x,extender,numOne,numTwo)
  print(x,type(x))
  if int(x) < numOne or int(x) > numTwo:
      x = subValidate(x,extender,numOne,numTwo)
  return x

def subValidate(x,extender,numOne,numTwo):
  replit.clear()
  print("You must input " + extender)
  x = input("\n >> ")
  return validate(x,extender,numOne,numTwo)

def returnToMain():
  x = str(input("\nEnter 1 to return to the main menu \n >> "))
  validate(x,"1.",1,1)
  replit.clear()
  mainMenu()

#program
mainMenu()
