p1 = [[2,0],[3,1],[1,2]]
p2=[[1,0],[1,1]]

n1=3
n2=2

def addPolynomial(p1,p2,n1,n2):
    c1 =0
    c2=0
    p3=[]
    while(c1<n1 and c2<n2):
        if p1[c1][1] == p2[c2][1]:
            c0 = p1[c1][0]+p2[c2][0]
            exp = p1[c1][1]
            p3.append([c0,exp])
            c1+=1
            c2+=1
        elif p2[c2][1] > p1[c1][1]:
            p3.append([p2[c2][0],p2[c2][1]])
            c1+=1
        elif p1[c1][1] > p2[c2][1]:
            p3.append([p1[c1][0],p1[c1][1]])
            c2+=1
    while c1<n1:
        p3.append([p1[c1][0],p1[c1][1]])
        c1+=1
    while c2<n2:
        p3.append([p2[c2][0],p2[c2][1]])
        c2+=1
    return p3

def multiplyPolynomial(p1,p2,n1,n2):
    ret=[]
    p3 = [0]*(n1+n2-1)
    for i in range(0,n1):
        for j in range(0,n2):
            p3[p1[i][1]+p2[j][1]] += p1[i][0]*p2[j][0]
    for ind,val in enumerate(p3):
        ret.append([val,ind])
        
    del(p3)
    return ret


print(addPolynomial(p1,p2,n1,n2))

print(multiplyPolynomial(p1,p2,n1,n2))