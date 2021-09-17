#code not working, for some reason

def searchBi(arr, num):
    low = 0
    high = len(arr) -1
    midIndex = (high + low) // 2
    midNumber = arr[midIndex]
    #defines essencial parameters
    if(midNumber == num):
        print(midNumber, "was found in index", midIndex)
    #if the mid number is already num, simply returns it
    elif(midNumber < num):
        low = midIndex
        high = len(arr) -1
        midIndex = (high + low) // 2
        midNumber = arr[midIndex]
    #if is num is greater than mid, start dividing and comparing upper part of array
    elif(midNumber > num):
        low = 0
        high = midIndex
        midIndex = (high + low) // 2
        midNumber = arr[midIndex]
    #if is num is lower than mid, start dividing and comparing lower part of array
    else:
        print(num, "is not in this array")

numberElements = int(input("Enter number of elements in array : "))
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:numberElements]
#collects array
x = int(input("Search number:"))
searchBi(a, x)