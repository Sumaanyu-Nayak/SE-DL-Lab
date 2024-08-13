import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Execution time of {func.__name__}: {execution_time:.4f} milliseconds")
        return result
    return wrapper

a=[]


def linearSearch(lst,ele):
    ret=-1
    count=0
    for i in range(len(lst)):
        count+=1
        if lst[i]==ele:
            ret=i
            break
    return ret,count


def binarySearch(lst,s,e,ele,count = 0):
    if s>e:
        return (-1,count)
    else:
        s=s
        e=e
        m=int((s+e)/2)
        if lst[m]==ele:
            return (m,count)
        elif ele>lst[m]:
            return binarySearch(lst,m+1,e,ele,count+1)
        elif ele<lst[m]:
            return binarySearch(lst,s,m-1,ele,count+1)


def binarySearch2(lst,ele):
    s=0
    e=len(lst)-1
    while(s<e):
        m=(s+e)//2
        if lst[m]==ele:
            return m
        elif ele>lst[m]:
            s=m+1
        elif ele<lst[m]:
            e=m-1
    pass

def sentinalSearch(lst,ele):
    lst2 = lst.copy()
    lst2.append(ele)
    i=0
    count = 0
    while lst2[i]!=ele:
        i+=1
        count+=1
    if i<len(lst2)-1:
        return i,count
    else:
        return -1,count
    

def fibonacciSearch(arr,ele):
    count = 0
    offset = 0
    fibm = 1
    fibm1 = 0
    fibm2 = 0
    while fibm < len(arr):
        fibm2 = fibm1
        fibm1 = fibm
        fibm = fibm1 + fibm2
    while fibm > 1:
        i = min(offset + fibm2, len(arr)-1)
        if arr[i] < ele:
            fibm = fibm1
            fibm1 = fibm2
            fibm2 = fibm - fibm1
            offset = i
            count += 1
        elif arr[i] > ele:
            fibm = fibm2
            fibm1 = fibm1 - fibm2
            fibm2 = fibm - fibm1
            count += 1
        elif arr[i] == ele:
            return i,count
    return -1,count


# input_str_a = input("Enter elements the list: ")
input_str_a = "1852 1290 572 1431 1324 1835 716 986 928 50 1398 1673 441 786 1873 621 1679 1197 858 1533 1547 1085 896 1659 435 1913 763 1056 1377 1912 575 1286 1303 868 877 1677 1176 1590 1175 78 870 1013 1532 1390 732 1666 1864 1593 1268 51 1830 41 1642 425 1834 1917 1786 1574 849 1476 1177 1920 1628 1099 1858 1773 1156 44 1332 1037 789 1641 73 1365 1218 1366 825 679 66 1438 470 1615 2000 1210 65 1618 945 1625 1420 863 622 1089 1342 1571 907 30 779 1346 698 1637 1206 1457 846 1281 1212 907 1142 727 65 1601 1195 54 1471 43 1675 1974 1748 1782"
a = input_str_a.split()  
a = sorted([int(num) for num in a])
ele=int(input("Enter the element to search: "))

@measure_time
def binaryCheck():
    print()
    print("Using Binary Search")
    ans = binarySearch(a,0,len(a),ele)
    if ans[0]<0:
        print("Element not found")
        print("The no of comparisions:",ans[1])
        
    else:
        print("Element found at", ans[0])
        print("The no of comparisions:",ans[1])
@measure_time
def linearCheck():
    print()
    print()
    print("Using linear search")
    ans = linearSearch(a,ele)
    if ans[0]<0:
        print("Element not found")
        print("The no of comparisions:",ans[1])
    else:
        print(f"Element found at", ans[0])
        print("The no of comparisions:",ans[1])
@measure_time
def sentinalCheck():
    print()
    print()
    print("Using sentinal search")
    ans = sentinalSearch(a,ele)
    if ans[0]<0:
        print("Element not found")
        print("The no of comparisions:",ans[1])
    else:
        print(f"Element found at", ans[0])
        print("The no of comparisions:",ans[1])
@measure_time
def fibonacciCheck():
    print()
    print()
    print("Using fibonacci search")
    ans = fibonacciSearch(a,ele)
    if ans[0]<0:
        print("Element not found")
        print("The no of comparisions:",ans[1])
    else:
        print(f"Element found at", ans[0])
        print("The no of comparisions:",ans[1])


linearCheck()
sentinalCheck()
binaryCheck()
fibonacciCheck()
