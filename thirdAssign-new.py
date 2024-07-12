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
    if m!=n:
        ret = "Operation"
        for i in range(m):
            ret += mat[i][i]
        ret = {
            "displayItem": ret
        }
    return ret

def Q5(mat,m,n):   # Check Upper Triangular
    ret = False
    if m!=n:
        ret=False
    else:
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

def saddle(mat,m,n):
    ret=[]
    for i in range(m):
        low = min(mat[i])
        low = mat[i].index(low)
        for j in range(n):
            if mat[i][low] < mat[i][j]:
                break
            else:
                ret.append({"value":mat[i][low],"index":{"i":low,"j":j}})
        print("hello")
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

m = int(input("Enter the no rows: "))
n = int(input("Enter the no of cols: "))
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# matrix2=[[1,2,3],[4,5,6],[7,8,9]]
# m,n,m2,n2 = 3,3,3,3
matrix = []
matrix2 = []
for i in range(0,m):
    tempMat = []
    for j in range(0,n):
        a = int(input(f'Enter the ${j+1} element of the row ${i+1}: '))
        tempMat.append(a)
    matrix.append(tempMat)

menu = "Enter One of the operation to apply:\n \
    1. Add\n \
    2. Subtract\n \
    3. Multiply\n \
    4. Diagonal Sum\n \
    5. Check Upper Triangular\n \
    6. Sadddle point\n \
    7. Transpose\n"

print(menu)
option = int(input("Enter your option: "))

if option==1:
    m2 = int(input("Enter the no rows: "))
    n2 = int(input("Enter the no of cols: "))
    for i in range(0,m2):
        tempMat = []
        for j in range(0,n2):
            a = int(input(f'Enter the ${j+1} element of the row ${i+1}: '))
            tempMat.append(a)
        matrix2.append(tempMat)
    display(Q1(matrix,matrix2,m,n,m2,n2))
elif option==2:
    m2 = int(input("Enter the no rows: "))
    n2 = int(input("Enter the no of cols: "))
    for i in range(0,m2):
        tempMat = []
        for j in range(0,n2):
            a = int(input(f'Enter the ${j+1} element of the row ${i+1}: '))
            tempMat.append(a)
        matrix2.append(tempMat)
    display(Q2(matrix,matrix2,m,n,m2,n2))
elif option==3:
    m2 = int(input("Enter the no rows: "))
    n2 = int(input("Enter the no of cols: "))
    for i in range(0,m2):
        tempMat = []
        for j in range(0,n2):
            a = int(input(f'Enter the ${j+1} element of the row ${i+1}: '))
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
    a = saddle(matrix,m,n)
    for i in a:
        print(i["value"],i["index"])