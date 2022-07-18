#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;
void lowercase(string &);
int main()
{
    string a, b, word;
    auto x = "";
    int counter = 0;
    getline(cin, a);
    getline(cin, b);
    lowercase(a);
    lowercase(b);
    for (auto x : a)
    {
        if (x == ' ' || x == '-' || x == ',' || x == '!' || x == '`' || x == '@' || x == '#' || x == '$' || x == '%' || x == '^' || x == '&' || x == '*' || x == '(' || x == ')' || x == '_' || x == '+' || x == '|' || x == ':' || x == ';' || x == '>' || x == '<' || x == '~' || x == '/' || x == '.' || x == '[' || x == ']' || x == '"')
        {
            if (word == b)
            {
                counter++;
            }
            word = "";
        }
        else
        {
            word += x;
        }
    }
    if (word == b)
    {
        counter++;
    }
    reverse(b.begin(), b.end());
    word = "";
    for (auto x : a)
    {
        if (x == ' ' || x == '-' || x == ',' || x == '!' || x == '`' || x == '@' || x == '#' || x == '$' || x == '%' || x == '^' || x == '&' || x == '*' || x == '(' || x == ')' || x == '_' || x == '+' || x == '|' || x == ':' || x == ';' || x == '>' || x == '<' || x == '~' || x == '/' || x == '.' || x == '[' || x == ']' || x == '"')
        {
            if (word == b)
            {
                counter++;
            }
            word = "";
        }
        else
        {
            word += x;
        }
    }
    if (word == b)
    {
        counter++;
    }
    cout << counter;
}
void lowercase(string &s)
{
    int n = s.size();
    for (int i = 0; i < n; ++i)
    {
        if ((int)s[i] >= 65 && (int)s[i] <= 90)
        {
            s[i] = (char)((int)(s[i]) + 32);
        }
    }
}
// Mohammad YousefiPour - Github.com/myp79
