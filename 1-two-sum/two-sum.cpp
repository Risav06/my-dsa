#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> numMap; // stores: {number, index}

        for (int i=0; i < nums.size(); ++i) {
            int complement = target - nums[i];

            // if the complement exists in the map,return the indices
            if (numMap.find(complement) != numMap.end()) {
                return {numMap[complement], i};
            }

            //otherwise, store the current number and its index
            numMap[nums[i]] = i;
        }   

        return {}; // Return empty if no solution is found (though constraints guarantee one)
    }
};