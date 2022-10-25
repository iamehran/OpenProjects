#include<bits/stdc++.h>
#include<stack>
using namespace std;
bool isValid(char*s)
{

stack<char> s1;

	int i;
	for(i=0;s[i]!='\0';i++)
	{
		char ch=s[i];
		if(ch=='(')
		{
			s1.push(ch);
		}
		else if(ch==')')
		{
			if(s1.empty() || s1.top()!='(')
			{
				return false;
			}
			s1.pop();
		
		}
		
	}
	return s1.empty();
}

int main()
{
	char s[100]="()";
	if(isvalid(s))
	{
		cout<<"yes";
	}
	else
	cout<<"no";
	
}
