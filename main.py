# Pénicaut Théodore


import sys


def ReadLines(PathName): #this function return a list that contain each line as an element of the list
    lines = []
    file = open(PathName,"r") #we open the file in read mode
    for line in file:
        lines.append(int(line.strip()))#cut the line on the \n
    file.close() #we close the file
    return lines


def FindIncrease(lines):
    current_min = lines[0]
    max_increase =0
    for i in range(len(lines)):
        if lines[i] < current_min: #if a new min is found, we update the current min
            current_min = lines[i]
        if (lines[i]-current_min) > max_increase: #if a bigger increase is found, we update the biggest we found
            max_increase = lines[i]-current_min
    return max_increase


def main():
    file = sys.argv[1]
    print(FindIncrease(ReadLines(file)))
   


main()


#to use this algorithm, just execute the python file with the TestFile path in second arguent of the python command.

#for example : python main.py TestFile.txt
# I'm not sure but I think that the complexity of this algorithm id O(n) as we make only one pass on all the lines.
