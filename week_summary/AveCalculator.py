import statistics
import re

class AveCalculator:
  def __init__(self, data):
    self.data = re.split(r',\s*', data)

  def print_average(self):
    # if (data contains time in format of HH:MM), convert time to minutes, 
    #   get average in minutes, return average in format of HH:MM
    if self.isTime(self.data[0]):

      times = [self.convert_to_mins(time) for time in self.data]
      average_in_mins = int(statistics.fmean(times))
      print(f"Average time: {self.convert_to_HHMM(average_in_mins)}")
      

    # else (data contains only numbers), calculate average directly
    else:
      average = int(statistics.fmean([int(value) for value in self.data]))
      print(f"Average value: {average}")
  
  def isTime(self, str):
    return ':' in str

  def convert_to_mins(self, str):
    [hours, minutes] = str.split(":")
    return int(hours) * 60 + int(minutes)
    
  def convert_to_HHMM(self, num):
    hours = num // 60
    minutes = num % 60
    return f"{hours}:{minutes}"