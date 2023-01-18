from AveCalculator import AveCalculator

def take_raw_values(n):
  arr = []
  for i in range(0, n):
    value = input('Enter value: ')
    arr.append(value)
  return arr

def main():
  q = "a"
  while q != 'q':
    try:
      n = int(input('How many values do you have: '))
      arr = take_raw_values(n)
      calculator = AveCalculator(n, arr)
      calculator.print_average()
      q = input('press q to exit, any other key to continue: ')
      print()
    except ValueError:
      print('Error! Please enter a valid number.\n')

# Execute main() function:
if __name__ == '__main__':
  main()
