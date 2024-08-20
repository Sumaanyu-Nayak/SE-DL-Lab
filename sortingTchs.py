def selectionSort(A):
    for i in range(len(A)-1):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]

    print ("Selection Sorted array")
    for i in range(len(A)):
        print(A[i],end=" ")

def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    count=0
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            print(f"{i}th and {j}th pass {arr}")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count+=1
                swapped = True
        print(f"{i}th and {j}th pass {arr}")
        if (swapped == False):
            break
    print(f"No of changes {count}")
    # print ("Bubble Sorted array")
    # for i in range(len(arr)):
    #     print(arr[i],end=" ")
    
input_str_a = input("Enter elements of the list separated by space: ")
a = list(map(int, input_str_a.split()))

# selectionSort(a)
bubbleSort(a)