
# creating a function 
def fib(n: int) -> int :
	if(n == 0 or n == 1):return n;
	else: return fib(n-1)+fib(n-2);

if __name__ == "__main__":
	num : int = int(input("give a number: "))
	print(f"The {num} fibonacci number is : {fib(num)}");
	
