
# Problem statement : Accept two numebrs from user and return its addition.

def Add(no1,no2):
	ans=no1+no2
	return ans

def main():
	print("Accept two number from user")
	n1=int(input())
	n2=int(input())
	
	ret=Add(n1,n2)
	print("Addition is ",ret)

if __name__=="__main__":
	main()

    