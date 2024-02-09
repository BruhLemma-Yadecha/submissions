#include <iostream>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    int contestants[n];
    for(int i = 0; i < n; i++){
        cin >> contestants[i];
    }
    int reference = contestants[k - 1];
    int result = 0;
    for (int i : contestants)
        if (i > 0 && i >= reference)
            result++;
    cout << result << endl;
}