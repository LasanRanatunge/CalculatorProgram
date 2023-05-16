# Online Python compiler (interpreter) to run Python online.
last_calculation = []

def history():
  global last_calculation
  if last_calculation == []:
    print("No past calculations to show")
  else:
    for i in last_calculation:
        print(*i)   

def Add(a, b):
    return a + b
  
# Function to subtract two numbers 
def Subtract(a, b):
    return a - b
  
# Function to multiply two numbers
def Multiply(a, b):
    return a * b
  
# Function to divide two numbers
def Divide(a, b):
    return a / b

# Function to power two numbers
def Power(a, b):
    return a ** b

# Function to remaind two numbers
def Remainder(a, b):
    return a % b


while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("8.History  : ? ")
  
  # take input from the user
  
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  if choice in ('+', '-', '*', '/', '^', '%', '#', '$',):
      if choice == '#':
          print("Done. Terminating")
          break
      a = input('Enter first number: ')
      print(str(a))
      if a.endswith('$'): continue
      b = input('Enter second number: ')
      print(str(b))
      if b.endswith('#'):
        print("Done. Terminating")
        break
      if b.endswith('$'): continue

      
      


      
  if choice == '+':
     result = float(a), "+" ,float(b), "=", Add(float(a), float(b))
     last_calculation.append(result)
     print(float(a), "+" ,float(b), "=", Add(float(a), float(b)))
  elif choice=='?':
       history()
       continue
  elif choice == '-':
      result = float(a), "-", float(b), "=", Subtract(float(a), float(b))
      last_calculation.append(result)
      print(float(a), "-", float(b), "=", Subtract(float(a), float(b)))
  elif choice == '*':
      result = float(a), "*",float(b), "=", Multiply(float(a), float(b))
      last_calculation.append(result)
      print(float(a), "*",float(b), "=", Multiply(float(a), float(b)))
  elif choice == '/':
      if float(b) != 0:
          result = float(a), "/", float(b), "=", Divide(float(a), float(b))
          last_calculation.append(result)
          print(float(a), "/", float(b), "=", Divide(float(a), float(b)))
          
      else:
          print("float division by zero")
          result = float(a), "/", float(b), "=", "None"
          last_calculation.append(result)
          print(float(a), "/", float(b), "=", "None")
  elif choice == '^':
      result = float(a), "**",float(b), "=", Power(float(a), float(b))
      last_calculation.append(result)
      print(float(a), "**",float(b), "=", Power(float(a), float(b)))
  elif choice == '%':
      result = float(a), "%",float(b), "=", Remainder(float(a), float(b))
      last_calculation.append(result)
      print(float(a), "%",float(b), "=", Remainder(float(a), float(b)))
      break
      

  else:
      print('Not a valid number,please enter again.')
      
