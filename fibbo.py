def fib(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fib(n-1) + fib(n-2) 

i=0
while(1):
	if fib(i)>50:
		break
	print fib(i)
	i += 1



