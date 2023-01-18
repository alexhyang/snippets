import statistics

class AveCalculator:
  def __init__(self, n, data):
    self.n = n
    self.data = data

  def print_average(self):
    # if (data contains time in format of HH:MM), convert time to minutes, 
    #   get average in minutes, return average in format of HH:MM
    if ':' in self.data[0]:

      times = [self.convert_to_mins(time) for time in self.data]
      average_in_mins = int(statistics.fmean(times))
      print(f"Average time: {self.convert_to_HHMM(average_in_mins)}")
      

    # else (data contains only numbers), calculate average directly
    else:
      average = int(statistics.fmean([int(value) for value in self.data]))
      print(f"Average value: {average}")

  def convert_to_mins(self, str):
    hours = int(str.split(":")[0])
    minutes = int(str.split(":")[1])
    return hours * 60 + minutes
    
  def convert_to_HHMM(self, num):
    hours = num // 60
    minutes = num % 60
    return f"{hours}:{minutes}"