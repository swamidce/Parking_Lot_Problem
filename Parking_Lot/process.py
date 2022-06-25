# Class Parking_Lot to define the size of parking lot & count for the number of parked car
class Parking_Lot:
  
    def __init__(self, size):
      
      # Counter for parked cars
      self.parkedVehicles = 0
      
      # Declaring a dictionary of slots of the given size
      self.slots = dict.fromkeys([i for i in range(1,int(size)+1)])

    # Get count of cars parked in the parking lot
    def count_parked_vehicles(self):
      return self.parkedVehicles

    # Set the number of cars parked in the lot (Assign slots)
    def get_slots(self):
      return self.slots                                             

    # Retrieve slots
    def set_slots(self, slot, value):
      self.slots[slot] = value

      
# Class Vehicle to initialize the vehicle details (registration_number,driver_age)
class Vehicle:
  
  def __init__(self, registrationNumber, random, age):
    
    # Initialising registration number
    self.carRegistrationNumber = registrationNumber
    
    # For handling dummy string driver age
    self.random = random
    
    # Initialising driver age
    self.driv_age = age
    
    self.carSlot = None

  # Returning driver age
  def get_age(self):
    return self.driv_age

  # Returning vehicle registration number
  def get_registration_number(self):
    return self.carRegistrationNumber

  # Setting slot for the parked car
  def set_slot(self, slot):    
    self.carSlot = slot

  # Returning slots of the cars
  def get_slot(self):
    return self.carSlot               

# Creating parking lot of the given size
def create_parking_Lot(size):
  
  # Initiate Parking_Lot class constructor to create a dictionary of the given size
  lot = Parking_Lot(int(size))
  
  print('Created parking of {} slots'.format(size))
  return lot


# Function to park a car
def park_Car(lot, registrationNumber,random, age):
  
  result = ''
  if lot:
    if len(lot.get_slots()) <= lot.count_parked_vehicles():
      result = 'Cannot park a car since parking lot is full'
            
    else:
      # Creating an instance of the dictionary
      parkingSlot = lot.get_slots()
      
      # Iterating through the keys of dict
      for slot in parkingSlot.keys():

        # If particular slot is available
        if parkingSlot[slot] is None:

          # Creating an instance of the class Vehicle by initializing the command(PB_1234,driver_age,21)
          car = Vehicle(registrationNumber,random, age)

          # Assigning the slots
          lot.set_slots(slot, car)                
          car.set_slot(slot)  

          # Incrementing the parked car
          lot.parkedVehicles += 1
          
          result = 'Car with vehicle registration number {} has been parked at slot number {}' .format(registrationNumber,str(slot))
          break
  else:
    result = 'Parking lot has not been allocated a particular size'
  return result


# Function to leaving a particular slot
def leave_Slot(lot, inputSlot):

  result = ''
  res=''
  age=''

  parkingSlot = lot.get_slots()  
  for parkedCar in parkingSlot.values():
    if parkedCar is not None:
      if parkedCar.get_slot()==int(inputSlot):
        res+=parkedCar.get_registration_number()+ ''
        age+=parkedCar.get_age()
                      
  if lot:

    # If no parked vehicles available then parking lot is empty
    if not lot.count_parked_vehicles():
      result = 'No car is available at the particular slot since parking lot is empty'
    elif int(inputSlot) >= 1 and int(inputSlot) <= len(lot.get_slots()): 
      
      # Creating an instance of the dictionary 
      parkingSlot = lot.get_slots()

      # To fetch the slot inputted by the user
      value = parkingSlot.get(int(inputSlot), None)
      if value is not None:                                                 
        # Set the slot i.e. key's value in dictionary to None
        lot.set_slots(int(inputSlot), None)

        # Decrementing parked car counter
        lot.parkedVehicles -= 1
        result = 'Slot number {} vacated, the car with vehicle registration number {} left the space, the driver of the car was of age {}' .format(inputSlot,res,age) 
      else:
        result = 'No available car at Slot number ' + inputSlot
    else:
      result = 'Cannot exit slot number: ' + inputSlot + ' since it\'s not available!'
  else:
    result = 'Parking lot has not been allocated a particular size'
  return result

  
# Function to retrieve car registration number from car_driver_age
def reg_number_by_Age(lot, inputAge):
  
  res = ''
  if lot:
    if not lot.count_parked_vehicles():
      res = 'No car is available at the particular slot since parking lot is empty'
    else:
      ptr = False

      # Creating an instance of the dictionary 
      parkingSlot = lot.get_slots()

      # Iterating through values of the dictionary
      for parkedVehicle in parkingSlot.values():
        if parkedVehicle is not None:

           # Invoking method get_age from vehicle class to check any such existing age 
          if parkedVehicle.get_age() == inputAge:
            
            ptr = True
            res += parkedVehicle.get_registration_number() + ', '
      if not ptr:
        res = ' '
  else:
    res = 'Parking lot has not been allocated a particular size'
  return res


# Function to retrieve slot number from vehicle registration number
def slot_num_by_car_reg_Number(parkingLot, number):
  
  result = ''
  if parkingLot:
    if not parkingLot.count_parked_vehicles():
      result = 'No car is available at the particular slot since parking lot is empty'
    else:
      flag = False

      # Creating an instance of the dictionary 
      parkingSlot = parkingLot.get_slots()

      # Iterating through values of the dictionary
      for parkedCar in parkingSlot.values():
        if parkedCar is not None:

          # Invoking method get_registration_number from vehicle class to check any such existing registration number
          if parkedCar.get_registration_number() == number:

            flag = True
            result += str(parkedCar.get_slot()) + ', '
            
            break
      if not flag:
        result = 'no such car parked with registration number {}' .format(number)
  else:
    result = 'Parking lot has not been allocated a particular size'
  return result

  
# Function to retrieve slot number from car_driver_age
def slot_num__by_Age(lot, inputage):                                                           
  result = ''
  if lot:
    if not lot.count_parked_vehicles():
      result = 'No car is available at the particular slot since parking lot is empty '
    else:
      ptr = False

      # Creating an instance of the dictionary
      parkingSlot = lot.get_slots() 

      # Iterating through values of the dictionary
      for parkedVehicle in parkingSlot.values():
        if parkedVehicle is not None:

          # Invoking method get_age from vehicle class to check any such existing driver_age
          if parkedVehicle.get_age() == inputage:
            ptr = True
            result += str(parkedVehicle.get_slot()) + ',' 
            
      if not ptr:
        result = 'No such car parked with driver\'s age {}'.format(inputage)
  else:
    result = 'Parking lot has not been allocated a particular size'
  return result