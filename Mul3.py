#Accept 3 numbers and return the multiplicatioon.


def mul(no1,no2,no3):
	if(no1==0 or no2==0 or no3==0):
		return 0;
	if(no1==0):
		no1=1
		
	if(no2==0):
		no2=1
	
	if(no3==0):
		no3=1
		
	ret=no1*no2*no3
	
	return ret

def main():
	#print("Accept three number from user")
	n1=int(input())
	n2=int(input())
	n3=int(input())
	
	ret=mul(n1,n2,n3)
	print("multiplication is ",ret)

if __name__=="__main__":
	main()
