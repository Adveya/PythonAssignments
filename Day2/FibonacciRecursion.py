def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2)) 

num = int(input("How many Fibonacci numbers do u wish to print?"))  

if num <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("The Fibonacci sequence is:")  
   for i in range(num):  
       print(recur_fibo(i))