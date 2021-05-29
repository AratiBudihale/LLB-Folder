
//Addition of factor
import java.util.*;

class Hello
{
	public int SumFactor(int no)
	{
		int sum=0;
		for(int i=1;i<=no/2;i++)
		{
			if(no%i==0)
			{
				sum=sum+i;
			}
		}
		return sum;
	}
}

class SumFactor
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.prinln("Enter no");
		int no=sc.nextInt();
		
		Hello obj=new Hello();
		int result=obj.SumFactor(no);
		System.out.prinln(result);
	}
}