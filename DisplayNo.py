#Problem statement : Write a program which display 1 to 5 on screen.

def Display(no):
	for i in range(1,no+1,1):
		print(i,end=" ")

def main():
	
	no=5
	Display(no)
	

if __name__=="__main__":
	main()