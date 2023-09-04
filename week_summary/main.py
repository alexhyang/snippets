from AveCalculator import AveCalculator

def main():
  while True:
    try:
      data = input('Enter your data ("q" to quit): ')
      if data == "q":
          break
      else:
          calculator = AveCalculator(data)
          calculator.print_average()
          print()
    except ValueError:
      print('Error! Please enter a valid number.\n')

# Execute main() function:
if __name__ == '__main__':
  main()
