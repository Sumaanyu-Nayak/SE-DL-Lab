from statistics import mode

n = int(input("Enter the no of students: "))
marks = []
for i in range(n):
    a = int(input("Enter the marks: "))
    marks.append(a)

# average marks


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
print("average marks: ", (avgSum/(n-absentCount)))
print("Highest marks: ", max(marks))
print("Lowest marks: ", lowestMark)
print("No of absent Students: ",absentCount)
passedFailed = 0
for i in range(n):
    if(marks[i]<35):
        passedFailed+=1
print("No of students failed: ", (passedFailed-absentCount))
print("No of students passed: ", (n-passedFailed))
print("Marks with highest frequency", mode(marks))

