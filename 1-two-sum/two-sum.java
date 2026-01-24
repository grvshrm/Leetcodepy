class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> m = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            if(m.containsKey(target-nums[i])){
                return new int[]{i, m.get(target-nums[i])};
            }
            else{
                m.put(nums[i], i);
            }
        }
        return new int[]{};
    }
    // public int[] twoSum(int[] nums, int target) {
    //     int[] ans = new int[2];
    //     for(int i=0; i<nums.length-1; ++i){
    //         for(int j=i+1; j<nums.length; ++j){
    //             if(nums[i]+nums[j] == target){
    //                 ans[0] = i;
    //                 ans[1] = j;
    //             }
    //         }
    //     }
    //     return ans;
    // }
}