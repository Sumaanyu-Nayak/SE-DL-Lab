def selectionSort(a):
    changeCount = 0
    compCount = 0
    for i in range(len(a)):
        minIndex = i
        for j in range(i+1, len(a)):
            if a[j] < a[minIndex]:
                compCount += 1
                minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i]
        changeCount += 1
    return (a,compCount,changeCount)

def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def bubbleSort(a):
    for i in range(len(a)):
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


arr = [837, 221, 827, 884, 221, 923, 319, 582, 190, 317,
 116, 201, 301, 4, 764, 528, 297, 714, 292, 443,
 425, 460, 116, 860, 86, 989, 71, 156, 688, 334,
 868, 133, 18, 730, 755, 583, 568, 580, 978, 740,
 423, 443, 573, 329, 648, 637, 273, 504, 236, 700,
 370, 360, 68, 327, 166, 315, 117, 651, 547, 856,
 73, 943, 187, 262, 427, 900, 482, 279, 82, 320,
 284, 321, 440, 142, 897, 520, 410, 782, 2, 394,
 665, 688, 624, 398, 926, 478, 591, 749, 340, 872,
 30, 456, 506, 283, 382, 244, 21, 345, 709, 530]


print("Selection Sort: ", selectionSort(arr.copy()))
print(arr)