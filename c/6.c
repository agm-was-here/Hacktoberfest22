#include <stdio.h>
int main()
{
int x,y;
for (int i=0;i<5;i++){
printf("Enter coordinates ");
scanf("%d %d",&x,&y);
if (x>0&&y>0)
{printf("Coordinates(%d,%d) are in Q1\n",x,y);}
else if (x<0 && y>0)
{printf("Coordinatest(%d,%d) are in Q2\n",x,y);}
else if (x<0 && y<0)
{printf("Coordinates(%d,%d) are in Q3\n",x,y);}
else if (x>0 && y<0)
{printf("Coordinates(%d,%d) are in Q4\n",x,y);}
else {printf("Coordinates(%d,%d)are in the center\n",x,y);}
}
return 0;
}
