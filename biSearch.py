def searchBi(arr):
    low = 0
    high = len(arr) -1
    midIndex = (high + low) // 2
    midNumber = arr[midIndex]
    #defines essencial parameters
    print("The middle number of this array is:", midNumber)

numberElements = int(input("Enter number of elements in array : "))
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:numberElements]
#collects array
searchBi(a)