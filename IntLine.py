#Write a program which accept number from user and display below patternwill display b:
 
 #Input :    4
#Output :   -4   -3  -2  -1  0   1   2   3   4


def LineInt(no):
	for i in range(-no,no+1,1):
		print(i,end=" ")

def main():
	print("Accept no from user")
	no=int(input())
	
	LineInt(no)

if __name__=="__main__":
	main()