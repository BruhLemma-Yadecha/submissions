#include <iostream>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    cout << "----------------------------" << cases << endl;
    for(; cases > 0; cases--){
        int boxes = getline(cin)
        string init_pos, fin_pos;
        cin >> init_pos >> fin_pos;

        // actual work
        int init_cats = count(init_pos.begin(), init_pos.end(), '1');
        int fin_cats = count(fin_pos.begin(), fin_pos.end(), '1');

        int add = 0;
        int move = 0;
        int retire = 0;
        if (init_cats > fin_cats)
            retire = init_cats - fin_cats;
        else if (fin_cats > init_cats)
            add = fin_cats - init_cats;
        for(int i = 0; i < boxes; i++){
            if(init_pos[i] != fin_pos[i]){
                move++;
            }
        }
        move -= retire + add;
        cout << move + retire + add << endl;
    }
}