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
        if ret[i] == maxVal and ret[i]>1:
            modearr.append(i)
    modearr.sort()
    return modearr

#input area
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


# variables
absentCount = 0
avgSum = 0
passedFailed = 0
#variables
print("Marks of students:", marks)
lowestMark = marks[0]
for i in range(n):
    if(marks[i]>=0 and marks[i]<lowestMark):    #lowest marks
        lowestMark=marks[i]
    if(marks[i]<0):                             #absent students
        absentCount+=1
    if(marks[i]>0):                             #average marks
        avgSum += marks[i]
    if(marks[i]<35 and marks[i]>=0):            #passed and failed students
        passedFailed+=1



#Print statements

print("average marks:", (avgSum/(n-absentCount)))                   #average marks
print("Highest marks:", max(marks))                                 #highest marks
print("Lowest marks:", lowestMark)                                  #lowest marks
print("No of absent Students:",absentCount)                         #absent students
print("No of students failed:", (passedFailed-absentCount))         #failed students
print("No of students passed:", (n-passedFailed))                   #passed students



#mode
if len(mode3(marks))>0:
    if len(mode3(marks))>2:
        print("Mode: ", mode3(marks))
    else:
        print("Mode:", ", ".join(map(str,mode3(marks))))
else:
    print("No mode found")

