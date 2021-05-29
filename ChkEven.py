#Problem statement : Accept number from user and check whether the number is even or odd.

def chkEven(no1):
	if no1%2==0:
		return True
	else:
		return False
	
def main():
	print("Accept no from user")
	no1=int(input())
	
	result=chkEven(no1)
	if(result==True):
		print("Even no")
	else:
		print("Odd no")
	

if __name__=="__main__":
	main()