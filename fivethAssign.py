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


input_str_a = input("Enter elements the list: ")
a = input_str_a.split()  
a = sorted([int(num) for num in a])
ele=int(input("Enter the element to search: "))


print()
print("Using Binary Search")
if binarySearch(a,0,len(a),ele)[0]<0:
    print("Element not found")
    print("The no of comparisions:",binarySearch(a,0,len(a),ele)[1])
    
else:
    print("Element found at", binarySearch(a,0,len(a),ele)[0])
    print("The no of comparisions:",binarySearch(a,0,len(a),ele)[1])

print()
print()
print("Using linear search")
if linearSearch(a,ele)[0]<0:
    print("Element not found")
    print("The no of comparisions:",linearSearch(a,ele)[1])
else:
    print(f"Element found at", linearSearch(a,ele)[0])
    print("The no of comparisions:",linearSearch(a,ele)[1])