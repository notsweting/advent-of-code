#include<bits/stdc++.h>
using namespace std;

string k;
int ans;
vector<char> nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
int main() {
    cin.sync_with_stdio(0);
    cin.tie(0);
    while(cin >> k){
        if(k == "end") break;
        int cur = 0;
        bool flag = true;
        for(int i=0; flag; i++){
            if(find(nums.begin(), nums.end(), k[i]) == nums.end()) continue;
            cur += (k[i] - '0')*10;
            flag = false;
        }

        flag = true;
        for(int i=k.size()-1; flag; i--){
            if(find(nums.begin(), nums.end(), k[i]) == nums.end()) continue;
            cur += k[i] - '0';
            flag = false;
        }

        ans+=cur;
    }

    cout << ans << endl;
    return 0;
}