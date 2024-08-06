def add(p1,p2,n):
    ret = p1.copy()
    for ind,val in enumerate(p2):
        ret[ind]+=val
    return ret


def multiply(p1,p2,n1,n2):
    ret = [0]*(n1+n2+1)
    for i in range(0,n1+1):
        for ind, val in enumerate(p2):
            ret[i+ind]+= p1[i]*val
    return ret

#Input polynomial

n1 = int(input("Enter the degree of the polynomial"))
p1 = [0]*(n1+1)
for i in range(n1+1):
    a=int(input(f"Enter the coefficient of {i}th degree term: "))
    p1[i]=a
n2 = int(input("Enter the degree of the polynomial"))
p2 = [0]*(n2+1)
for i in range(n2+1):
    a=int(input(f"Enter the coefficient of {i}th degree term: "))
    p2[i]=a

menu = "Enter one of the following option: \n \
1. Add\n \
2. Multiply"
print(menu)
print()
option = int(input("Enter the option: "))

if option==1:
    if n1>n2:
        print(add(p1,p2,n1))
    else:
        print(add(p2,p1,n2))
elif option==2:
    if n1>n2:
        print(multiply(p1,p2,n1,n2))
    else:
        print(multiply(p2,p1,n2,n1))