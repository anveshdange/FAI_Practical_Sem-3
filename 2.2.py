p : bool = True 
 
num : int = int(input("Give a number: " )) 
i : int = num-1 

while(i>=2):
	if(num%i==0):p=False
	i -= 1
if(p):print(f"{num} is prime")
else:print(f"{num} is composite")
