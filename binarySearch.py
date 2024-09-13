import random
import os

def main():
    arr = [random.randint(0,200) for x in range(10)]
    arr.sort()
    score = 0
    print("There are 10 items in the array, try to guess the items\n")
    while len(arr) > 0:
        print(f"The score is {score} and there are {len(arr)} items left")
        print(arr)
        value = int(input("Guess the Value :"))
        index = binarySearch(arr,value)
        if index is not None:
            removeItem(arr, index)
            score +=1
            os.system('clear')   
        else:
            if score>0:
                score-=1
            print(f"The {value} is not in the array")
            os.system('clear')

   

def removeItem(arr, indx):
    item = arr[indx]
    arr.remove(item)
    print(f"{item} has been removed")


def binarySearch(arr, searchValue):
    # find the upper and lower limit
    lower = 0
    upper = len(arr) - 1
    while lower<=upper:
        midPoint = (lower+upper)//2
        midValue = arr[midPoint]
        # print(f"midpoint and midvalue {midPoint}, {midValue}")
        if midValue == searchValue:
            return midPoint
        elif midValue>searchValue:
            upper=midPoint-1
            # print(f"upper {upper}")
        else:
            lower = midPoint+1
            # print(f"lower {lower}")
    return None

main()