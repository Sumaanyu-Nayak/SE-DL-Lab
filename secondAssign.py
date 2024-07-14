def union3(s1=[],s2=[],s3 = []):                      # Function to find the union of at most 3 sets
    unionSet = s2.copy() or []
    for i in s1:
        if i not in s2:
            unionSet.append(i)
    for i in s3:
        if i not in unionSet:
            unionSet.append(i)
    return unionSet

def intersection(s1, s2):                               # Function to find the intersection of 2 sets only
    ret=[]
    for i in s1:
        if i in s2:
            ret.append(i)
    return ret

def intersection3(s1,s2,s3):                            # Function to find the intersection of 3 sets only
    ret = []
    for i in s1:
        if i in s2 and i in s3:
            ret.append(i)
    return ret

def q1(s1,s2):                                          # Function to find the who play both cricket and badminton
    return intersection(s1,s2)

def q2(s1,s2):                                          # Function to find the who play either cricket or badminton but not both
    ret = []
    inter = intersection(s1,s2)
    uni = union3(s1,s2)
    for i in uni:
        if i in inter:
            continue
        else:
            ret.append(i)
    return ret

def q3(s1,s2,n):                                        # Function to find the number of students who play neither cricket nor badminton
    uni2 = union3(s1,s2)
    return n-len(uni2)

def q4(s1,s2,s3):                                       # Function to find the number of students who play cricket and football but not badminton
    inter3 = intersection3(s1,s2,s3)
    inter2 =intersection(s1,s2)
    return len(inter2)-len(inter3)

def q5(s1,s2,s3,n):                                      # Function to find the number of students who play none of the three sports
    uni3 = union3(s1,s2,s3)
    return n-len(uni3)

def q6(s1,s2,s3):                                         # Function to find list of students who play at least one of the three sports
    return sorted(union3(s1,s2,s3))

def q7(s1,s2,s3):                                         # Function to find list of students who play all the three sports
    return intersection3(s1,s2,s3)



t = int(input("Enter the no of test cases: "))           # Taking no of test cases as input
while (t):
    nT = int(input("Enter to total no of students: "))  # Taking total no of students as input
    input_str_a = input("Enter elements of the Cricket separated by space:")    # Taking input of the students who play cricket
    a = input_str_a.split()  
    a = [int(num) for num in a] 
    input_str_b = input("Enter elements of the Badminton separated by space:")  # Taking input of the students who play badminton
    b = input_str_b.split()  
    b = [int(num) for num in b] 
    input_str_c = input("Enter elements of the Football separated by space:")   # Taking input of the students who play football
    c = input_str_c.split()  
    c = [int(num) for num in c] 

    print("i) ",q1(a,b))                         # Printing the output of first question
    print("ii) ",q2(a,b))                        # Printing the output of second question
    print("iii) ",q3(a,b,nT))                    # Printing the output of third question
    print("iv) ",q4(a,b,c))                      # Printing the output of fourth question
    print("v) ",q5(a,b,c,nT))                    # Printing the output of fifth question
    print("vi) ",q6(a,b,c))                      # Printing the output of sixth question
    print("vii) ",q7(a,b,c))                     # Printing the output of seventh question
    t=t-1