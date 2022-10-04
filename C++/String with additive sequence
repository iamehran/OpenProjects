// C++ program to check whether a string
// makes an additive sequence or not
#include <bits/stdc++.h>
using namespace std;

// Checks whether num is valid or not, by
// checking first character and size
bool isValid(string num)
{
	if (num.size() > 1 && num[0] == '0')
		return false;
	return true;
}

// returns int value at pos string, if pos is
// out of bound then returns 0
int val(string a, int pos)
{
	if (pos >= a.length())
		return 0;

	// converting character to integer
	return (a[pos] - '0');
}

// add two number in string form and return
// result as a string
string addString(string a, string b)
{
	string sum = "";
	int i = a.length() - 1;
	int j = b.length() - 1;
	int carry = 0;

	// loop until both string get processed
	while (i >= 0 || j >= 0)
	{
		int t = val(a, i) + val(b, j) + carry;
		sum += (t % 10 + '0');
		carry = t / 10;
		i--; j--;
	}
	if (carry)
		sum += (carry + '0');
	reverse(sum.begin(), sum.end());
	return sum;
}

// Recursive method to check c = a + b
bool checkAddition(list<string>& res, string a,
							string b, string c)
{
	// both first and second number should be valid
	if (!isValid(a) || !isValid(b))
		return false;
	string sum = addString(a, b);

	// if sum is same as c then direct return
	if (sum == c)
	{
		res.push_back(sum);
		return true;
	}

	/* if sum size is greater than c, then no
		possible sequence further OR if c is not
		prefix of sum string, then no possible
		sequence further */
	if (c.size() <= sum.size() ||
		sum != c.substr(0, sum.size()))
		return false;
	else
	{
		res.push_back(sum);
		
		// next recursive call will have b as first
		// number, sum as second number and string
		// c as third number after removing prefix
		// sum string from c
		return checkAddition(res, b, sum,
							c.substr(sum.size()));
	}
}

// Method returns additive sequence from string as
// a list
list<string> additiveSequence(string num)
{
	list<string> res;
	int l = num.length();

	// loop until l/2 only, because if first
	// number is larger,then no possible sequence
	// later
	for (int i = 1; i <= l/2; i++)
	{
		for (int j = 1; j <= (l - i)/2; j++)
		{
			if (checkAddition(res, num.substr(0, i),
							num.substr(i, j),
							num.substr(i + j)))
			{
				// adding first and second number at
				// front of result list
				res.push_front(num.substr(i, j));
				res.push_front(num.substr(0, i));
				return res;
			}
		}
	}

	// If code execution reaches here, then string
	// doesn't have any additive sequence
	res.clear();
	return res;
}

// Method to print result list
void printResult(list<string> res)
{
	for (auto it = res.begin(); it != res.end(); it++)
		cout << *it << " ";
	cout << endl;
}

// Driver code to test above methods
int main()
{
	string num = "235813";
	list<string> res = additiveSequence(num);
	printResult(res);

	num = "199100199";
	res = additiveSequence(num);
	printResult(res);
	return 0;
}
