# Write a program which accept number from user and display below patternwill display b:
 
# Input :    5
#Output :   1   *   2    *   3      *    4   *   5   *
 
 
def Display(no):
	for i in range(1,no+1,1):
		print(i,"*",end=" ")

def main():
	print("Accept no from user")
	no=int(input())
	
	Display(no)

if __name__=="__main__":
	main()