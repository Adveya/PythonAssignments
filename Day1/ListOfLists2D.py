m=int(input("Enter no. of rows:"))
n=int(input("Enter no. of columns:"))

LsL=[]
Ls=[]

print("Enter elements one by one:")
for i in range(m):
    for j in range(n):
        Ls.append(int(input()))
    LsL.append(Ls)
    Ls=[]
for i in LsL:
    for j in i:
        print(j, end=' ')
    print()