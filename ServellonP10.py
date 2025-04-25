# ServellonP10
# Programmer: Mike Servellon
# Date : 11/14/2024
# Purpose: Demonstrate how to use files

# Working with 5 points instead of 2

# imports
from math import sin, cos, sqrt, radians, atan2
import fileinput


# Header function
def display_header():
  print('\nWelcome to my which-city-are-you-closest-to program!\n')
  print('This program will ask you to provide a set of latitude and longitude, both in decimal degrees.')
  print("The program will then output if you're closest to Los Angeles or New York.")

# Class for custom exception
class Incorrect(Exception):
    pass

# continue function
def continue_program():
  while True:
    try: 
      user_response = input('Want to try another set of coordinates? (y/n): ')
      check_letter = user_response.strip()[0].lower()
      check_number = user_response.isnumeric()
      another = check_letter =='y'

      if check_number == True:
        raise TypeError
      elif check_letter not in ('y', 'n'):
        raise Incorrect
      else:
        return another
      
    #exceptions for continue program
    except IndexError:
      print('\nPlease enter a letter or word.\n')
    except TypeError:
      print('\nNo integers are allowed.\n')
    except Incorrect:
      print("\nPlease confirm if you'd like to continue.\n")


# Define a class to keep track of a point in space, figure out distance from another point.
class Geopoint:

  # init self constructor with two attributes for the locaiton of the point, include a placeholder description 
  def __init__(self, lat=0, lon=0, description='TBD'):
    '''Initialize objects'''
    self.__lat = lat
    self.__lon = lon
    self.__description= description
  

  # set point method, using point property
  def set_point(self,point):
    '''Setting points'''
    self.__lat = point[0]
    self.__lon = point[1]

  # get point method to return tuple or list with lat and lon
  def get_point(self):
    '''Displaying points'''
    return self.__lat, self.__lon

  # point property
  point = property(get_point,set_point)
  

  # description set and get methods
  def set_description(self, description):
    '''Set description'''
    self.__description = description

  def get_description(self):
    '''Display provided description'''
    return self.__description

  # description property
  description = property(get_description, set_description)

  
  # Distance method, using the point property, that will calculate distance between 
  def distance(self, point):
    '''Calculation for the distance between two points, copied from my P6'''
    # import user and city coordinates

    lat_1 = radians(self.__lat)
    lon_1 = radians(self.__lon)

    lat_2 = radians(point.__lat)
    lon_2 = radians(point.__lon)


    t_lat = lat_2 - lat_1
    t_lon = lon_2 - lon_1
  

    # Distance calculation
    R = 6371

    A = sin(t_lat/2)**2 + cos(lat_1) * cos(lat_2) * sin(t_lon/2)**2

    C = 2 * atan2(sqrt(A), sqrt(1 - A))
    
    D = round(R * C, 2)

    return D



# Display header
display_header()


# program loop, allow for multiple calculations
while True:
  # empty the created lists
  display_list = []
  point_list = []

  try:
    # user input point
    print('\nPlease enter your set of coordinates')
    user_lat = float(input('Enter the latitude (decimal degrees): '))
    user_lon = float(input('Enter the longitude (decimal degrees): '))
    # pass in values using constructor
    user_point = Geopoint(user_lat, user_lon)

  except ValueError:
    print('\nPlease enter a numeric coordinate and try again.')
    continue
    
  # read file list, save in empty list created
  for line in fileinput.input('P10 Folder\points.txt'):
    replace_list = line.replace('\n', '')
    split_list = replace_list.split(',', 2)
    display_list.append(split_list)

  # loop to create points to add to points list
  for it in range(len(display_list)):

    # create new points, pass in lat lon and description to append the points into list
    new_point = Geopoint(float(display_list[it][0]), float(display_list[it][1]), display_list[it][2])

    # do the distance function, add the result to list
    new_point_distance = new_point.distance(user_point)
    point_list.append(new_point_distance)
  
  # Iterate through the point list and find the closest point
  lowest = min(point_list)

  # use the point to reference back to the points to display along with the description, use index method
  lowest_index = point_list.index(lowest)

  print(f'\n\nYou are closest to {display_list[lowest_index][2]}. They are located at {display_list[lowest_index][0]}, {display_list[lowest_index][1]}.\n\n')

  # ask user if they want to do it again
  if not continue_program(): break



# goodbye
print('\nThank you for using my program, goodbye.\n')
