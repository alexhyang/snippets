from AveCalculator import AveCalculator

def main():
  q = "a"
  while q != 'q':
    try:
      data = input('Enter your data: ')
      calculator = AveCalculator(data)
      calculator.print_average()
      q = input('press q to exit, any other key to continue: ')
      print()
    except ValueError:
      print('Error! Please enter a valid number.\n')

# Execute main() function:
if __name__ == '__main__':
  main()
