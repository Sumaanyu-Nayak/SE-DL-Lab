from statistics import mode

def mode3(marks):
    ret = {}
    for i in marks:
        if i in ret:
            ret[i] += 1
        else:
            ret[i] = 1
    maxVal = max(ret.values())
    modearr = []
    for i in ret:
        if ret[i] == maxVal:
            modearr.append(i)
    modearr.sort()
    return modearr


n = int(input("Enter the no of students: "))
marks = []
i=0
while i<n:
    a = int(input(f"Enter mark no. {i+1}: "))
    if(a>100):
        print("Invalid marks")
    else:
        marks.append(a)
        i+=1
# n=5
# marks = [10,27,10,27,5]
# average marks

print("Marks of students:", marks)
lowestMark = marks[0]
for i in range(n):
    if(marks[i]>=0 and marks[i]<lowestMark):
        lowestMark=marks[i]

absentCount = 0
for j in range(n):
    if(marks[j]<0):
        absentCount+=1
avgSum = 0
for j in range(n):
    if(marks[j]>0):
        avgSum += marks[j]
print("average marks:", (avgSum/(n-absentCount)))
print("Highest marks:", max(marks))
print("Lowest marks:", lowestMark)
print("No of absent Students:",absentCount)
passedFailed = 0
for i in range(n):
    if(marks[i]<35):
        passedFailed+=1
print("No of students failed:", (passedFailed-absentCount))
print("No of students passed:", (n-passedFailed))

if len(mode3(marks))>0:
    if len(mode3(marks))>2:
        print("Mode: ", mode3(marks))
    else:
        print("Mode:", ", ".join(map(str,mode3(marks))))
else:
    print("No mode found")

