nlist = 10
n1 = 0
n2 = 1
count = 0
if nlist <= 0:
   print("Please enter a positive integer")
elif nlist == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       
