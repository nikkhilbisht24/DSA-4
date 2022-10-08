#include<bits/stdc++.h>

using namespace std;

class Solution{
    public:

    vector<int>twoSums(vector<int>&nums,int target){
        vector<int> ans;
        unordered_map<int,int> mpp;
        for(int i=0; i<nums.size(); i++){
            if(mpp.find(target-nums[i]!=mpp.end())){
                ans.push_back(mpp[target-nums[i]]);
                ans.push_back(i);
                return ans;
            }
            mpp[nums[i]]=i;
        }
        return ans;
    }
};
int main(){
    Solution();
}
//tc - O(N)
//sc - O(N)
