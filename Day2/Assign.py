mahList=[ [111,'AAAA', 5123.43,'female'],
          [123,'AAbb', 4123.43,'male'],
          [121,'AAcc', 6123.43,'female'],
          [131,'AddA', 7123.43,'male'] ]
print(*mahList,sep='\n')

print("This is the original list", mahList)

M=len(mahList)

for i in range(M):
    for j in range(3):
        if(mahList[j][0] > mahList[j+1][0]):
            mahList[j][0],mahList[j+1][0]=mahList[j+1][0],mahList[j][0]

for i in range(M):
    if(mahList[i][3]=="male"):
        mahList[i][1]="Mr." + mahList[i][1]

    elif(mahList[i][3]=="female"):
       mahList[i][1]="Ms." + mahList[i][1]

    mahList[i][2]=mahList[i][2] +  (mahList[i][2]*0.1)



print("This is the list after SORTING, PREFIXING AND ADDING 10% TO SALARY",*mahList,sep='\n')
