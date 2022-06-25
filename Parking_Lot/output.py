# It would create an output.txt file with all the commands executed from the input file (input.txt)
import subprocess
with open("output.txt", "w+") as output:
    subprocess.call(["python", "car_parking.py",'input.txt'], stdout=output)