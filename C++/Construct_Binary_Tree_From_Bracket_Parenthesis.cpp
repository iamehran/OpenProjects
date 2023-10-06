#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    Node *treeFromString(string str){
        string cur = "";
        int i = 0, num, n = str.length();
        while (i < n && str[i] != '(' && str[i] != ')') {
            cur += str[i++];
        }
        num = stoi(cur);
        Node *root = new Node(num);
        stack<Node*> st;
        st.push(root);
        for (; i < n; i++) {
            if (str[i] == '(') {
                cur = "";
                while (str[i + 1] != '(' && str[i + 1] != ')') {
                    i++;
                    cur += str[i];
                }
                num = stoi(cur);
                Node *temp = new Node(num);
                if (!st.top()->left)
                    st.top()->left = temp;
                else
                    st.top()->right = temp;
                st.push(temp);
            }
            else if (str[i] == ')')
                st.pop();
        }
        return root;
    }
};

int main(){
  int t;cin>>t;
  while(t--){
    string s;cin>>s;
    Solution obj;
    Node *root = obj.treeFromString(s);
  }
  return 0;
}
