import time
import math
import csv
import tempfile
import pandas as pd

# Question 1

#resource: https://www.w3resource.com/python-exercises/python-conditional-exercise-10.php
#resource: https://www.geeksforgeeks.org/python-measure-time-taken-by-program-to-execute/

def FizzBuzz():
  begin = time.time()
  for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
      print("FizzBuzz")
    elif x % 3 == 0:
      print("Fizz")
    elif x % 5 == 0:
      print("Buzz")
    else:
      print(x)
  end = time.time()
  print("time: ", end - begin)
  
#FizzBuzz()

#Question 2

#resource: https://www.geeksforgeeks.org/how-to-take-integer-input-in-python/
#resource: https://www.w3schools.com/python/ref_math_pi.asp
def Volume():
  radius = input("Enter the radius: ")
  radius = int(radius)
  radiusCubed = radius * radius * radius
  volume = (4/3) * math.pi * radiusCubed
  print ("Volume: ", volume)

#Volume()

#Question 3

#https://stackoverflow.com/questions/46787806/python-dictionary-to-csv-in-required-format

def writeCSV():
  data = {
    'Title': ['1984', 'Animal Farm', 'Brave New World', 'Fahrenheit 451', 'Jane Eyre', 'Wuthering Heights', 'Agnes Grey', 'Walden', 'Walden Two', 'Eats, Shoots & Leaves'],
    'Author': ['George Orwell', 'George Orwell', 'Aldous Huxley', 'Ray Bradbury', 'Charlotte Brontë', 'Emily Brontë', 'Anne Brontë', 'Henry David Thoreau', 'B. F. Skinner', 'Lynee Truss'],
    'ISBN13': ['978-0451524935', '978-0451526342', '978-0060929879', '978-0345342966', '978-0142437209', '978-0141439556', '978-1593083236', '978-1420922615', '978-0872207783', '978-1592400874'],
   'Pages': ['268', '144', '288', '208', '532', '416', '256', '156', '301', '209']
  }

  header = data.keys()
  num_rows = len(data[list(header)[0]])

  with open ('books.csv', 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ',')
    csvwriter.writerow(header)
    for row in range(num_rows):
     csvwriter.writerow([data[key][row] for key in header])

writeCSV()
# REturn file name??? print("File name: 'books.csv'")

#Question 4

#resource: https://stackoverflow.com/questions/45198869/create-dictionary-from-csv-with-headers
#resource: https://thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/

def CSVtoDict():
  with open('books.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    dictionary = {col: [] for col in reader.fieldnames}
    for row in reader:
      for col in reader.fieldnames: 
        dictionary[col].append(row[col])

    for key, value in dictionary.items():
      print(key, ':', value)

#CSVtoDict()

#Question 5

def Temp():
  data = {
    'Title': ['1984', 'Animal Farm', 'Brave New World', 'Fahrenheit 451', 'Jane Eyre', 'Wuthering Heights', 'Agnes Grey', 'Walden', 'Walden Two', 'Eats, Shoots & Leaves'],
    'Author': ['George Orwell', 'George Orwell', 'Aldous Huxley', 'Ray Bradbury', 'Charlotte Brontë', 'Emily Brontë', 'Anne Brontë', 'Henry David Thoreau', 'B. F. Skinner', 'Lynee Truss'],
    'ISBN13': ['978-0451524935', '978-0451526342', '978-0060929879', '978-0345342966', '978-0142437209', '978-0141439556', '978-1593083236', '978-1420922615', '978-0872207783', '978-1592400874'],
   'Pages': ['268', '144', '288', '208', '532', '416', '256', '156', '301', '209']
  }
  
  header = data.keys()
  with tempfile.NamedTemporaryFile(mode='r+') as csvfile:
    b = pd.DataFrame(data, columns=header)
    b.to_csv(csvfile.name, index=False)
    
    reader = csv.DictReader(csvfile, delimiter=',')
    dictionary = {col: [] for col in reader.fieldnames}
    for row in reader:
      for col in reader.fieldnames: 
        dictionary[col].append(row[col])

    for key, value in dictionary.items():
      print(key, ':', value)
Temp()