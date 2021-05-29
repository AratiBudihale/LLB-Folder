//Ckeck Palindrome
import java.util.*;

class Hello
{
	public boolean Palindrome(int no)
	{
		int temp=no;
		int iDigit=0;
		int Rev=0;
		
		while(no>0)
		{
			iDigit=no%10;
			Rev=Rev*10+iDigit;
			no=no/10;
		}
		
		if(temp==Rev)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
}

class ChkPalindrome
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter no");
		int no=sc.nextInt();
		
		Hello obj=new Hello();
		boolean result=obj.Palindrome(no);
		if(result==true)
		{
			System.out.println("palindrome no");
		}
		else
		{
			System.out.println("Not Palindrome no");
		}
	}
}