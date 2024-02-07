#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
    int len;
    cin >> len;
    string s;
    cin >> s;
    unordered_set<char> set;
    for(char c : s){
        if(!set.contains(tolower(c)))
            set.insert(tolower(c));
    }
    if(set.size() == 26){
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

}