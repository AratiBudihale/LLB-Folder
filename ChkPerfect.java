
//Check perfect no
import java.util.*;

class Hello
{
	public boolean ChkPerfect(int no)
	{
		int sum=0;
		for(int i=1;i<=no/2;i++)
		{
			if(no%i==0)
			{
				sum=sum+i;
			}
		}
		if(sum==no)
		{
			return true;
		}
		else
		{
			return false;
		}
	}
}

class ChkPerfect
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter no");
		int no=sc.nextInt();
		
		Hello obj=new Hello();
		boolean result=obj.ChkPerfect(no);
		if(result==true)
		{
			System.out.println("Perfect no");
		}
		else
		{
			System.out.println("Not Perfect no");
		}
	}
}