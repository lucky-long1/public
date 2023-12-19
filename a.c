#include<stdio.h>

int main()
{
	//printf("hello world !\n");
	int a, j;
	for (a=1;a>10;a++)
	{
		for (j=1;j>=a;j++)
		{
		printf("%d * %d = %d",j,a,j*a);
		if (a == j)
			printf("\n");
		}
	}
}
