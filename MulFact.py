#Accept number from user and display multiplication of factor

def MulFact(no):
	
	for i in range(1,no,1):
		if(i%no==0):
			mul=mul*i
	
	return mul;
	
def main():

	print("Enter number")
	no=int(input())
	
	ret=MulFact(no)
	print(ret)
	
if __name__=="__main__":
	main()