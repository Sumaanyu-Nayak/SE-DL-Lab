def chigh(mat,m,ind):
    high = 0
    for i in range(m):
        for j in range(1):
            if mat[i][ind]>high:
                high = mat[i][ind]
    return high

def rlow(mat,n,ind):
    low=9999999999999999999999999999999999999999
    for i in range(n):
        for j in range(1):
            if mat[ind][i] < low:
                low = mat[ind][i]
    return low

def Q1(mat1,mat2,m1,n1,m2,n2):      # Add
    ret = []
    if(m1==m2 and n1==n2):
        for i in range(m1):
            tempMat = []
            for j in range(n1):
                c = mat1[i][j]+mat2[i][j]
                tempMat.append(c)
            ret.append(tempMat)
    else:
        ret = {
            "displayItem":"Operation not Possible"
        }
    return ret

def Q2(mat1,mat2,m1,n1,m2,n2):     # Subtract
    ret = []
    if(m1==m2 and n1==n2):
        for i in range(m1):
            tempMat = []
            for j in range(n1):
                c = mat1[i][j]-mat2[i][j]
                tempMat.append(c)
            ret.append(tempMat)
    else:
        ret = {
            "displayItem":"Operation not Possible"
        }
    return ret

def Q3(mat1,mat2,m1,m2,n1,n2):    # Multiply
    ret = []
    for i in range(len(mat1)):
        tempMat = []
        for j in range(len(mat2[0])):
            result = 0
            for k in range(len(mat2)):
                result+= mat1[i][k] * mat2[k][j]
            tempMat.append(result)
        ret.append(tempMat)
    return ret

def Q4(mat,m,n):   # Diagonal Sum
    ret = 0
    for i in range(m):
        for j in range(n):
            if i == j:
                ret += mat[i][j]
    ret = {
        "displayItem": ret
    }
    return ret

def Q5(mat,m,n):   # Check Upper Triangular
    ret = False
    for i in range(m):
        for j in range(n):
            if(i>j and mat[i][j]==0):
                ret=True
            else:
                ret=False
                break
    if ret:
        ret = {
            "displayItem":"It is an Upper Triangular Matrix"
        }
    else:
        ret = {
            "displayItem":"It's not an Upper Triangular Matrix"
        }
    return ret   

def Q6(mat,m,n):  # Saddle Point
    ret={}
    for i in range(m):
        for j in range(n):
            r_low = rlow(mat,n,i)
            c_high = chigh(mat,m,j)
            if(mat[i][j]==r_low and mat[i][j]==c_high):
                ret = {
                    "displayItem": f'Element no ({i},{j})',
                    "value": f'Value {mat[i][j]}'
                }
                break
            else:
                ret = {
                    "displayItem" : 'No such Element Found'
                }
    return ret

def Q7(mat,m,n): #Transpose
    ret = []
    j=0
    for i in range(n):
        tempMat = []
        for k in range(m):
            tempMat.append(mat[k][j])
        j+=1
        ret.append(tempMat)
    return ret

def display(mat):
    if isinstance(mat,list):
        for i in mat:
            for j in i:
                print(j,end=" ")
            print()
    else:
        for i in mat:
            print(mat[i])

# def saddle(mat,m,n):
#     ret=[]
#     for i in range(m):                               
#         low = min(mat[i])                            
#         low = mat[i].index(low)                       
#         for j in range(n):
#             if mat[i][low] < mat[j][i]:
#                 print("break")
#                 break
#             else:
#                 print("append")
#                 print(mat[i][low],mat[j][i])
#                 ret.append({"value":mat[i][low],"index":{"i":low,"j":j}})
#     print(ret)
#     return ret

# def newSaddlepoint(mat,m,n):
#     ret = []
#     flg =False
#     for i in range(n):
#         low = mat[i][0]
#         curr_j = 0
#         for j in range(n):
#             if low>mat[i][j]:
#                 low=mat[i][j]
#                 curr_j = j
#         print(low,curr_j)
#         for j in range(0,m):
#             if low<mat[j][curr_j]:
#                 print(low, mat[j][curr_j])
#                 flg=False
#                 break
#             else:
#                 flg=True
                    
#         if flg:
#             ret.append({"value":low,"index":{"i":i,"j":j}})
#         print(ret)

#         if j==m:
#             return ret
#     return {
#         "displayItem" : 'No such Element Found'
#     }


def is_magic_square(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    # Early exit for non-square matrices (not traditional magic squares)
    if m != n:
        return False
    
    # Calculate the magic constant for an n x n matrix
    magic_constant = n * (n * n + 1) // 2
    
    # Check if all elements are distinct and in the range 1 to n^2
    elements = set()
    for row in matrix:
        for num in row:
            if num < 1 or num > n * n or num in elements:
                return False
            elements.add(num)
    
    # Check the sums of all rows
    for row in matrix:
        if sum(row) != magic_constant:
            return False
    
    # Check the sums of all columns
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_constant:
            return False
    
    # Check the sum of the main diagonal
    if sum(matrix[i][i] for i in range(n)) != magic_constant:
        return False
    
    # Check the sum of the anti-diagonal
    if sum(matrix[i][n - 1 - i] for i in range(n)) != magic_constant:
        return False
    
    return True

m = int(input("Enter the no rows: "))
n = int(input("Enter the no of cols: "))
matrix = []
matrix2 = []
for i in range(0,m):
    tempMat = []
    for j in range(0,n):
        a = int(input(f'Enter the {j+1} element of the row {i+1}: '))
        tempMat.append(a)
    matrix.append(tempMat)

menu = "Enter One of the operation to apply:\n \
    1. Add\n \
    2. Subtract\n \
    3. Multiply\n \
    4. Diagonal Sum\n \
    5. Check Upper Triangular\n \
    6. Sadddle point\n \
    7. Transpose\n \
    8. Magic Check\n"

print(menu)
option = int(input("Enter your option: "))

if option==1:
    m2 = int(input("Enter the no rows: "))
    n2 = int(input("Enter the no of cols: "))
    for i in range(0,m2):
        tempMat = []
        for j in range(0,n2):
            a = int(input(f'Enter the {j+1} element of the row {i+1}: '))
            tempMat.append(a)
        matrix2.append(tempMat)
    display(Q1(matrix,matrix2,m,n,m2,n2))
elif option==2:
    m2 = int(input("Enter the no rows: "))
    n2 = int(input("Enter the no of cols: "))
    for i in range(0,m2):
        tempMat = []
        for j in range(0,n2):
            a = int(input(f'Enter the {j+1} element of the row {i+1}: '))
            tempMat.append(a)
        matrix2.append(tempMat)
    display(Q2(matrix,matrix2,m,n,m2,n2))
elif option==3:
    m2 = int(input("Enter the no rows: "))
    n2 = int(input("Enter the no of cols: "))
    for i in range(0,m2):
        tempMat = []
        for j in range(0,n2):
            a = int(input(f'Enter the {j+1} element of the row {i+1}: '))
            tempMat.append(a)
        matrix2.append(tempMat)
    display(Q3(matrix,matrix2,m,n,m2,n2))
elif option == 4:
    display(Q4(matrix,m,n))
elif option == 5:
    display(Q5(matrix,m,n))
elif option == 6:
    display(Q6(matrix,m,n))
elif option == 7:
    display(Q7(matrix,m,n))
elif option == 8:
    print(is_magic_square(matrix)) 