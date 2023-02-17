
# defining a factorial function (recursive)
def factorial(num : int) -> int :
	if(num == 1): return 1;
	p = num * factorial(num - 1)
	return p

# driver code 
if __name__ == "__main__":
	inp : int = int(input("Give a number: "))
	print(f"The Factorial of {inp} is {factorial(inp)}")
