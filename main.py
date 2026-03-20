import sys


def ReadLines(PathName):
    lines = []
    file = open(PathName,"r")
    for line in file:
        lines.append(int(line.strip()))
    file.close()
    return lines


def FindIncrease(lines):
    max = 0
    for i in range(len(lines)-1):
        tmp = lines[i+1]-lines[i]
        if tmp>max:
            max = tmp
    return max



def main():
    file = sys.argv[1]
    print(FindIncrease(ReadLines(file)))



main()
