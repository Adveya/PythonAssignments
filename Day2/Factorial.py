num=int(input("Whos factorial do u want?"))
def recur(num):
    if num==1:
      return num
    else:
      return num*recur(num-1)
print("The factorial is", recur(num))