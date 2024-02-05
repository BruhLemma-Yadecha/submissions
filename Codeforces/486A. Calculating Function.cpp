#include <iostream>

using namespace std;

int main(){
    int n;
    cin >> n;
    
    int result = 0;
    for (int i = -1; i >= -n; i -= 2)
    {
        result += i;
    }
    for (int j = 2; j <= n; j += 2){
        result += j;
    }
    cout << result << endl;
}