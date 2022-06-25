import sys
from process import (create_parking_Lot, park_Car, leave_Slot, reg_number_by_Age, slot_num_by_car_reg_Number, slot_num__by_Age)

def arg_Execution(parkingLot, arg):
    CREATE_PARKING_LOT = 'Create_parking_lot'
    PARK_CAR = 'Park'
    LEAVE_SLOT = 'Leave'
    SLOT_FOR_REG_NUMBER = 'Slot_number_for_car_with_number'
    REG_NUMBER_BY_AGE = 'Vehicle_registration_number_for_driver_of_age'
    SLOT_NUMBER_BY_AGE = 'Slot_numbers_for_driver_of_age'
    
    if arg[0] == CREATE_PARKING_LOT:
        return create_parking_Lot(arg[1])
    elif arg[0] == PARK_CAR:
        print (park_Car(parkingLot, arg[1], arg[2],arg[3]))
    elif arg[0] == LEAVE_SLOT:
        print(leave_Slot(parkingLot, arg[1]))
    elif arg[0] == SLOT_FOR_REG_NUMBER:
        print(slot_num_by_car_reg_Number(parkingLot, arg[1]).rstrip(', '))
    elif arg[0] == REG_NUMBER_BY_AGE:
        print(reg_number_by_Age(parkingLot, arg[1]).rstrip(', '))
    elif arg[0] == SLOT_NUMBER_BY_AGE:
        print(slot_num__by_Age(parkingLot, arg[1]).rstrip(', '))
    else:
        print('Invalid arguement ')
    return parkingLot

def parse_File(parkingLot, fileName):
    try:
        with open(fileName) as file:
            args = file.readlines()
            for arg in args:
                parkingLot = arg_Execution(
                    parkingLot, arg.replace('\n', '').split())
    except Exception as e:
        print(e)
      
def interactive_Mode(parkingLot):
    try:
        arg = input().split()
        while arg[0] != exit:
            parkingLot = arg_Execution(parkingLot, arg)
            arg = input().split()
    except Exception as e:
        print(e)

def main():
    parkingLot = None
    if len(sys.argv) > 1:
        parse_File(parkingLot, sys.argv[1])
    else:
        interactive_Mode(parkingLot)
        
if __name__ == '__main__':
    main()
