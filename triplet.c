#include<stdio.h>
int main()
{
	int a,b,c;
	for(c=1;c<=23;c++)
	{
		for(b=1;b<=23;b++)
		{
			for(a=1;a<=23;a++)
			{
				if(a*a + b*b + c*c == 546 )
				{
					printf("a=%d b=%d c=%d\n",a,b,c);
				}
			}
		}
	}
			return 0;
}

